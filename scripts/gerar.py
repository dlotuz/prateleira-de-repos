#!/usr/bin/env python3
"""Gera o README.md e o site (docs/index.html) a partir de data/ferramentas.json.

Uso: python3 scripts/gerar.py
"""
import html
import json
import re
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = json.loads((RAIZ / "data" / "ferramentas.json").read_text(encoding="utf-8"))
HOJE = date.today().strftime("%d/%m/%Y")
REPO_URL = "https://github.com/dlotuz/prateleira-de-repos"
SITE_URL = "https://www.productweekly.com.br/prateleira"

TIPOS = [
    ("app", "App", "Programa com tela própria. Roda no computador, no navegador ou num servidor seu."),
    ("skill", "Skill", "Instruções que ensinam o Claude Code (ou outro agente) a fazer um trabalho. Instala com um comando e vira um /comando."),
    ("terminal", "Terminal", "Ferramenta sem tela, usada por comando. Dá para pedir ao Claude Code rodar por você."),
    ("lib", "Biblioteca", "Código para usar dentro de um projeto de programação."),
    ("modelo", "Modelo", "Modelo de IA que roda no seu computador, sem serviço externo."),
    ("mcp", "MCP", "Ponte que deixa o Claude controlar outro programa."),
    ("comp", "Componentes", "Peças de interface prontas para copiar num site ou app."),
    ("plugin", "Plugin", "Extensão que muda o próprio Claude Code."),
    ("dados", "Dados", "Base de informação para consultar."),
]
TIPO_NOME = {k: n for k, n, _ in TIPOS}

# Ordem das seções do README = o que a pessoa quer fazer
CATEGORIAS = [
    ("doc", "Ler, pesquisar e escrever"),
    ("audio", "Transcrever e trabalhar com voz"),
    ("video", "Criar e editar vídeo"),
    ("visual", "Design, apresentações e imagens"),
    ("skill", "Deixar o design feito com IA mais bonito"),
    ("prod", "Organizar o dia a dia"),
    ("vida", "Finanças, viagem e currículo"),
    ("agent", "Agentes e automação"),
    ("cursos", "Cursos, área de membros e comunidade"),
    ("apps", "Construir apps e interfaces"),
]
CAT_NOME = dict(CATEGORIAS)

DESTAQUES = [
    ("alta", "Comece por estas.", "As mais úteis para a maioria das pessoas"),
    ("media", "Boas quando a necessidade aparecer.", "Resolvem bem um problema específico"),
    ("baixa", "Para casos específicos.", "Nichadas, novas demais, paradas ou com alguma limitação"),
]
ORDEM_DESTAQUE = {k: i for i, (k, _, _) in enumerate(DESTAQUES)}

PRECISA = [
    ("Instalar e usar", "Baixa e abre, sem terminal"),
    ("Navegador", "Funciona no navegador"),
    ("Claude Code", "Precisa do Claude Code instalado"),
    ("Codex", "Feita para o Codex, da OpenAI"),
    ("Terminal", "Precisa rodar comandos"),
    ("Docker ou servidor", "Você hospeda (Docker ou servidor)"),
    ("Programar", "É para quem programa"),
    ("GPU", "Precisa de placa de vídeo forte"),
    ("Chave de API paga", "Usa API paga por uso"),
    ("DaVinci Resolve", "Precisa do DaVinci Resolve"),
    ("Só consultar", "É só consultar"),
    ("Só Windows", "Só roda no Windows"),
]

NIVEIS = [
    ("facil", "Fácil", "Baixa e usa, abre no navegador ou só consulta", {"Instalar e usar", "Navegador", "Só consultar"}),
    ("medio", "Médio", "Precisa do Claude Code, do Codex ou do terminal", {"Claude Code", "Codex", "Terminal", "DaVinci Resolve"}),
    ("avancado", "Avançado", "Precisa de servidor, GPU ou saber programar", {"Docker ou servidor", "Programar", "GPU"}),
]
NIVEL_NOME = {k: n for k, n, _, _ in NIVEIS}
TIPO_DICA = {
    "app": "Tem tela própria", "skill": "Ensina o Claude Code", "terminal": "Roda por comando",
    "lib": "Para quem programa", "modelo": "IA no seu computador", "mcp": "O Claude controla outro programa",
    "comp": "Peças de interface", "plugin": "Muda o Claude Code", "dados": "Para consultar",
}

# Nome curto de cada tarefa nos atalhos do site
TAREFA_CURTA = {
    "doc": "Texto e pesquisa", "audio": "Voz e transcrição", "video": "Vídeo", "visual": "Design e imagens",
    "skill": "Design sem cara de IA", "prod": "Dia a dia", "vida": "Finanças e vida", "agent": "Agentes",
    "apps": "Construir apps", "cursos": "Cursos e comunidade",
}
SUGESTOES = ["vídeo", "reunião", "Figma", "currículo", "legenda", "finanças"]


ESTRELAS = [("1000", "+1 mil"), ("10000", "+10 mil"), ("50000", "+50 mil"), ("100000", "+100 mil")]


def estrelas_num(i):
    """'1,7k' -> 1700; '53' -> 53."""
    t = i["estrelas"].strip().lower().replace(",", ".")
    return int(float(t[:-1]) * 1000) if t.endswith("k") else int(float(t))


def nivel_de(i):
    nivel = "facil"
    for k, _, _, req in NIVEIS:
        if req & set(i["precisa"]):
            nivel = k
    return nivel


PEDIDO = ("Antes de instalar, verifique este repositório: {link}. Leia o README e os arquivos de instalação e me diga: "
          "1) o que ele instala no meu computador e onde; 2) se baixa ou roda algo da internet durante a instalação; "
          "3) se pede chave de API, senha ou acesso a alguma conta; 4) se muda configurações do meu agente de IA ou do sistema; "
          "5) a licença e se o projeto está ativo. Não instale nada até eu aprovar.")

REGRAS = [
    "Dado sensível, seu ou de cliente, não vai para versão de nuvem de terceiro. Várias destas ferramentas têm versão cloud; use a que roda na sua máquina.",
    "GPL e AGPL podem ser usadas por conta própria. Colocar dentro de um produto vendido exige cuidado com a licença.",
    "Projeto de terceiro que você ainda está avaliando roda melhor em Docker, isolado do resto da máquina.",
    "Nem tudo aqui foi testado por nós. Antes de instalar, peça para a sua IA verificar o repositório (o pedido pronto está acima da lista e em cada ficha).",
    "Skill é texto: leia o arquivo antes de instalar e veja o que ela manda o agente fazer.",
    "Confira de novo a licença e a atividade do repositório no dia da instalação.",
]


def ordenadas(itens):
    return sorted(itens, key=lambda i: (ORDEM_DESTAQUE[i["destaque"]], i["nome"].lower()))


# ---------------------------------------------------------------- README
def readme():
    n = len(DADOS)
    linhas = [
        "# Prateleira de Repositórios",
        "",
        f"Repositórios de IA de código aberto, separados pelo que você quer fazer. São {n} até agora. "
        "Cada um diz o que faz, o que precisa para rodar, quanto custa e qual produto conhecido ele substitui.",
        "",
        f"**Versão com filtros:** {SITE_URL}",
        "",
        "Um projeto do [Product Weekly](https://productweekly.com.br), o que importa em produto, toda semana. "
        "Curadoria de Eduardo Oliveira.",
        "",
        "## Como ler cada item",
        "",
        "- **Tipo:** App, Skill, Terminal e outros (explicados [no fim da página](#os-tipos)).",
        "- **Nível:** Fácil (baixa e usa, ou abre no navegador), Médio (precisa do Claude Code ou do terminal) ou Avançado (servidor, GPU ou programação).",
        "- **Precisa de:** o que você precisa ter para usar.",
        "- **Alternativa a:** o produto pago ou fechado que ela substitui, quando existe.",
        "- **Atenção:** licença, custo escondido, projeto parado ou qualquer coisa que você deve saber antes.",
        "- **Testado pelo PW:** a gente instalou e usou de verdade. Os outros a gente ainda não testou.",
        "",
        "## Antes de instalar, peça para a sua IA verificar",
        "",
        "Nem tudo aqui foi testado por nós. Antes de instalar qualquer item, cole na sua IA (Claude Code, Codex…) o pedido abaixo, trocando o link:",
        "",
        "```text",
        PEDIDO.format(link="<link do repositório>"),
        "```",
        "",
        "## Comece por aqui",
        "",
    ]
    for i in ordenadas([x for x in DADOS if x["destaque"] == "alta"]):
        linhas.append(f"- [{i['nome']}](#{ancora(i)}): {primeira_frase(i['o_que_faz'])}")
    linhas += ["", "## O que você quer fazer?", ""]
    for k, nome in CATEGORIAS:
        qtd = sum(1 for x in DADOS if x["categoria"] == k)
        if qtd:
            linhas.append(f"- [{nome}](#{slug(nome)}) ({qtd})")
    for k, nome in CATEGORIAS:
        itens = ordenadas([x for x in DADOS if x["categoria"] == k])
        if not itens:
            continue
        linhas += ["", f"## {nome}", ""]
        for i in itens:
            linhas += item_md(i)
    linhas += ["", "## Os tipos", ""]
    for _, nome, desc in TIPOS:
        linhas.append(f"- **{nome}:** {desc}")
    linhas += ["", "## Antes de instalar qualquer uma", ""]
    linhas += [f"- {r}" for r in REGRAS]
    linhas += [
        "",
        "## Sugira uma ferramenta",
        "",
        "Conhece uma ferramenta de IA de código aberto que resolve um problema real? "
        f"[Abra uma sugestão]({REPO_URL}/issues/new?template=sugerir-ferramenta.yml) ou mande um pull request "
        "seguindo o [guia de contribuição](CONTRIBUTING.md). Toda sugestão passa por revisão antes de entrar.",
        "",
        "## Licença",
        "",
        "O conteúdo desta lista está sob [CC BY 4.0](LICENSE): pode copiar e adaptar, dando o crédito. "
        "Cada ferramenta tem a sua própria licença, indicada no item.",
        "",
        f"Estrelas e data do último push conferidos no GitHub. Lista gerada em {HOJE}.",
        "",
    ]
    return "\n".join(linhas)


def item_md(i):
    tipo = TIPO_NOME[i["tipo"]]
    destaque = " · comece por esta" if i["destaque"] == "alta" else ""
    testado = " · **testado pelo PW**" if i.get("testado") else ""
    out = [f"### {i['nome']}", "", f"`{tipo}`{destaque}{testado} · [{i['repo']}]({i['url']})", "", i["o_que_faz"], ""]
    if i["alternativa_a"]:
        out += [f"**Alternativa a:** {i['alternativa_a']}", ""]
    out.append("**Para que serve:**")
    out += [f"- {u}" for u in i["para_que_serve"]]
    out.append("")
    out += [f"**Como começar:** {i['primeiro_passo']}", ""]
    out.append(f"**Nível:** {NIVEL_NOME[nivel_de(i)]} · **Precisa de:** {', '.join(i['precisa'])} · **Licença:** {i['licenca']} · "
               f"**Estrelas:** {i['estrelas']} · **Último push:** {i['ultimo_push']} · **Situação:** {i['situacao']}")
    out.append("")
    if i["atencao"]:
        out += [f"> **Atenção:** {i['atencao']}", ""]
    return out


def primeira_frase(t):
    p = t.split(": ")[0] if ": " in t[:80] else t.split(". ")[0]
    return p.rstrip(".") + "."


def slug(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = "".join(c if c.isalnum() or c in " -" else "" for c in t)
    return t.strip().replace(" ", "-")


def ancora(i):
    return slug(i["nome"])


# ---------------------------------------------------------------- site
def e(t):
    return html.escape(t, quote=True)


def normalizar(t):
    import unicodedata
    t = unicodedata.normalize("NFD", t.lower())
    return " ".join("".join(c for c in t if not unicodedata.combining(c)).split())


def com_codigo(t):
    """Escapa o texto e transforma `trecho` em <code>trecho</code>."""
    partes = e(t).split("`")
    return "".join(f"<code>{p}</code>" if n % 2 else p for n, p in enumerate(partes))


def ficha(i):
    t = i["tipo"]
    fid = slug(i["nome"])
    busca = normalizar(" ".join([i["nome"], i["repo"], i["o_que_faz"], " ".join(i["para_que_serve"]),
                                  i["alternativa_a"] or "", TIPO_NOME[t],
                                  " ".join(i["precisa"]), i["atencao"] or "",
                                  "testado testado pelo pw" if i.get("testado") else ""]))
    alt = f'<p class="alt"><span>Alternativa a</span>{e(i["alternativa_a"])}</p>' if i["alternativa_a"] else ""
    nota = ""
    if i["atencao"]:
        nota = f'<p class="nota{" forte" if i["atencao_forte"] else ""}">{e(i["atencao"])}</p>'
    precisa = "".join(f"<span>{e(p)}</span>" for p in i["precisa"])
    lic = f'<span class="aviso">{e(i["licenca"])}</span>' if i["licenca_alerta"] else f"<span>{e(i['licenca'])}</span>"
    sit = f'<span class="aviso">{e(i["situacao"])}</span>' if i["situacao_alerta"] else f"<span>{e(i['situacao'])}</span>"
    usos = "".join(f"<li>{e(u)}</li>" for u in i["para_que_serve"])
    capa_img = (f'<img src="{e(i["imagem"])}" alt="" loading="lazy" decoding="async" referrerpolicy="no-referrer" width="1200" height="600">'
                if i.get("imagem") else "")
    return f"""
        <article class="ficha" id="{fid}" data-tipo="{t}" data-c="{i['categoria']}" data-n="{nivel_de(i)}" data-api="{1 if 'Chave de API paga' in i['precisa'] else 0}" data-e="{estrelas_num(i)}" data-t="{1 if i.get('testado') else 0}" data-busca="{e(busca)}">
          <a class="capa" href="{e(i['url'])}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><span class="capa-nome">{e(i['nome'])}<i>.</i></span>{capa_img}</a>
          <div class="topo"><span class="marcas"><span class="tipo">{TIPO_NOME[t]}</span>{'<span class="selo-testado" title="A gente instalou e usou">Testado</span>' if i.get('testado') else ''}</span><span class="cat">{CAT_NOME[i['categoria']]}</span></div>
          <h3><a href="{e(i['url'])}" target="_blank" rel="noopener">{e(i['nome'])}</a></h3>
          <span class="repo">{e(i['repo'])}</span>{alt}
          <p class="oque">{e(i['o_que_faz'])}</p>
          <div class="usos"><span class="rot">Para que serve</span><ul>{usos}</ul>{nota}</div>
          <div class="comecar"><span class="rot">Como começar</span><p>{com_codigo(i['primeiro_passo'])}</p><button class="verif" type="button" data-pedido="{e(PEDIDO.format(link=i['url']))}">Copiar pedido de verificação para a sua IA</button></div>
          <div class="precisa"><span class="rot">Precisa de</span><span class="nv nv-{nivel_de(i)}">Nível {NIVEL_NOME[nivel_de(i)].lower()}</span>{precisa}</div>
          <div class="meta">{lic}<span>{e(i['estrelas'])} estrelas</span><span>push {e(i['ultimo_push'])}</span>{sit}<button class="link" type="button" data-id="{fid}">Copiar link</button></div>
        </article>"""


def exemplos(cat):
    nomes = [x["nome"] for x in ordenadas([x for x in DADOS if x["categoria"] == cat])][:3]
    return e(", ".join(nomes))


def site():
    n = len(DADOS)
    conta = lambda f: sum(1 for x in DADOS if f(x))
    tarefas = "".join(
        f'<button class="tarefa" type="button" data-g="c" data-v="{k}" aria-pressed="false"><b>{TAREFA_CURTA[k]}</b>'
        f'<span class="desc">{exemplos(k)}</span><span class="n">{conta(lambda x: x["categoria"] == k)}</span></button>'
        for k, nome in CATEGORIAS if conta(lambda x: x["categoria"] == k))
    seg = f'<button class="segb" type="button" data-g="n" data-v="all" aria-pressed="true">Tudo<span class="n">{n}</span></button>'
    seg += "".join(
        f'<button class="segb" type="button" data-g="n" data-v="{k}" aria-pressed="false" title="{e(desc)}">{nome}<span class="n">{conta(lambda x: nivel_de(x) == k)}</span></button>'
        for k, nome, desc, _ in NIVEIS)
    seg_e = f'<button class="segb" type="button" data-g="e" data-v="all" aria-pressed="true">Tudo<span class="n">{n}</span></button>'
    seg_e += "".join(
        f'<button class="segb" type="button" data-g="e" data-v="{v}" aria-pressed="false">{nome}<span class="n">{conta(lambda x: estrelas_num(x) >= int(v))}</span></button>'
        for v, nome in ESTRELAS)
    opcoes = f'<li role="option" id="op-all" data-v="all" aria-selected="true"><span class="ok" aria-hidden="true"></span><span><b>Todos os tipos</b></span><span class="n">{n}</span></li>' + "".join(
        f'<li role="option" id="op-{k}" data-v="{k}" aria-selected="false"><span class="ok" aria-hidden="true"></span>'
        f'<span><b>{nome}</b><small>{TIPO_DICA[k]}</small></span><span class="n">{conta(lambda x: x["tipo"] == k)}</span></li>'
        for k, nome, _ in TIPOS if conta(lambda x: x["tipo"] == k))
    sugestoes = "".join(f'<button class="sug" type="button">{e(t)}</button>' for t in SUGESTOES)
    rotulos = json.dumps({
        "c": {k: TAREFA_CURTA[k] for k, _ in CATEGORIAS},
        "n": {k: f"Nível {nome.lower()}" for k, nome, _, _ in NIVEIS},
        "tipo": TIPO_NOME,
        "tipo_n": {k: nome for k, nome, _ in TIPOS},
        "e": {v: f"{nome} estrelas" for v, nome in ESTRELAS},
    }, ensure_ascii=False)
    secoes = ""
    for k, titulo, sub in DESTAQUES:
        itens = ordenadas([x for x in DADOS if x["destaque"] == k])
        secoes += f"""
    <section class="secao" data-d="{k}">
      <div class="sh"><h2>{titulo}</h2><span class="mono">{sub} · <b class="cont">{len(itens)}</b></span></div>
      <div class="grade">{''.join(ficha(i) for i in itens)}
      </div>
    </section>"""
    legenda = "".join(f"<div><b>{nome}</b><p>{e(desc)}</p></div>" for _, nome, desc in TIPOS)
    regras = "".join(f"<li>{e(r)}</li>" for r in REGRAS)
    return PAGINA.format(n=n, hoje=HOJE, pedido=e(PEDIDO.format(link="[cole aqui o link do repositório]")), hoje_curto=HOJE[:5], tarefas=tarefas, seg=seg, seg_e=seg_e, opcoes=opcoes,
                         sugestoes=sugestoes, rotulos=rotulos, secoes=secoes, legenda=legenda, regras=regras,
                         repo=REPO_URL, n_semapi=conta(lambda x: "Chave de API paga" not in x["precisa"]),
                         n_testados=conta(lambda x: x.get("testado")))


PAGINA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Prateleira de Repositórios · Product Weekly</title>
<meta name="description" content="Repositórios de IA de código aberto, separados pelo que você quer fazer: o que cada um faz, o que precisa para rodar e o que substitui.">
<meta property="og:title" content="Prateleira de Repositórios · Product Weekly">
<meta property="og:description" content="{n} repositórios de IA de código aberto, separados pelo que você quer fazer.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gabarito:wght@400..900&family=Instrument+Serif:ital@1&family=JetBrains+Mono:wght@400;500;700&display=swap">
<style>
%%CSS%%
</style>
</head>
<body>
<header class="barra">
  <div class="wrap">
    <a class="logo" href="https://productweekly.com.br" aria-label="Product Weekly"><span class="ico" aria-hidden="true">PW<i>.</i></span><b>Product</b><span class="pil">Weekly</span></a>
    <nav class="nav" aria-label="Links">
      <a href="{repo}">GitHub</a>
      <a href="{repo}/issues/new?template=sugerir-ferramenta.yml">Sugira uma ferramenta</a>
      <a class="cta" href="https://www.instagram.com/product.weekly/">Siga no Instagram</a>
    </nav>
  </div>
</header>

<main id="conteudo">
<!--prat--><div class="prat">
<section class="hero">
  <div class="wrap">
    <div>
      <span class="mono">Lista aberta · Product Weekly</span>
      <h1>Prateleira <span>de repos.</span></h1>
      <p>Repositórios de IA de código aberto, separados pelo que você quer fazer. <em>Cada um diz o que precisa para rodar,</em> quanto custa e qual produto conhecido ele substitui.</p>
      <div class="acoes"><a class="bt-gh" href="{repo}">Ver no GitHub</a><a class="bt-zip" href="{repo}/archive/refs/heads/main.zip">Baixar a lista (.zip)</a></div>
    </div>
    <div class="numeros">
      <div><b class="l">{n}</b><span class="mono">Repositórios</span></div>
      <div><b>9</b><span class="mono">Tipos</span></div>
      <div><b>{hoje_curto}</b><span class="mono">Atualizada</span></div>
    </div>
  </div>
</section>

<div class="faixa">
  <div class="wrap">
    <span class="mono">Não programa?</span>
    <p>Escolha o nível Fácil: são as que você baixa ou abre no navegador e já usa.</p>
  </div>
</div>

<div class="corpo">
  <div class="wrap">
    <div class="filtros">
      <div class="busca"><label class="mono" for="busca">Buscar</label><input id="busca" type="search" placeholder="Digite o que você quer fazer: vídeo, reunião, Figma, currículo…" autocomplete="off" spellcheck="false"><kbd class="mono" aria-hidden="true">/</kbd></div>
      <div class="sugestoes"><span class="mono">Experimente</span>{sugestoes}</div>
      <div class="bloco"><span class="mono tit">O que você quer fazer?</span><div class="tarefas" role="group" aria-label="Filtrar pelo que você quer fazer">{tarefas}</div></div>
      <div class="linha2">
        <div class="nivel"><span class="mono tit">Nível</span><div class="seg" role="group" aria-label="Filtrar por nível">{seg}</div></div>
        <div class="nivel"><span class="mono tit">Estrelas no GitHub</span><div class="seg" role="group" aria-label="Filtrar por estrelas no GitHub">{seg_e}</div></div>
        <label class="toggle" for="semapi"><input type="checkbox" id="semapi"><span class="caixa" aria-hidden="true"></span><span>Sem API paga <i class="n" id="n-semapi">{n_semapi}</i></span></label>
        <label class="toggle" for="sotestados"><input type="checkbox" id="sotestados"><span class="caixa" aria-hidden="true"></span><span>Só os testados <i class="n" id="n-testados">{n_testados}</i></span></label>
        <div class="tiposel"><span class="mono tit" id="tipo-rot">Tipo</span><div class="drop"><button type="button" class="drop-btn" id="tipo-btn" aria-haspopup="listbox" aria-expanded="false" aria-controls="tipo-menu" aria-labelledby="tipo-rot tipo-atual"><span id="tipo-atual">Todos os tipos</span><span class="n" id="tipo-n">{n}</span></button><ul class="drop-menu" id="tipo-menu" role="listbox" tabindex="-1" aria-labelledby="tipo-rot" hidden>{opcoes}</ul></div></div>
        <span class="mono resumo-n">Mostrando <b id="mostrando">{n}</b> de {n}</span>
      </div>
      <div class="ativos" id="ativos" hidden><div class="tokens" id="tokens"></div></div>
    </div>
    <div class="tarja" role="note"><p><b>Nem tudo aqui foi testado por nós:</b> só os que têm o selo <span class="selo-testado em-linha">Testado</span>. Antes de instalar os outros, peça para a sua IA verificar o repositório.</p><button class="btn-copiar" type="button" data-pedido="{pedido}">Copiar pedido de verificação</button></div>
{secoes}
    <div class="vazio" id="vazio" hidden><p>Nada encontrado com essa busca e esses filtros juntos.</p><p class="mono">Tente: <button class="sug" type="button">vídeo</button><button class="sug" type="button">reunião</button><button class="sug" type="button">design</button> ou <button class="limpar" type="button" data-limpar>limpe os filtros</button></p></div>

    <section class="tipos" aria-labelledby="tipos-h">
      <div class="sh"><h2 id="tipos-h">Os tipos.</h2><span class="mono">O que cada etiqueta quer dizer</span></div>
      <div class="lista">{legenda}</div>
    </section>

    <section class="regras" aria-labelledby="regras-h">
      <h2 id="regras-h">Antes de instalar<span>.</span></h2>
      <ul>{regras}</ul>
    </section>

    <section class="sugira" aria-labelledby="sugira-h">
      <div>
        <h2 id="sugira-h">Conhece uma que falta aqui?</h2>
        <p>Mande a sugestão pelo GitHub. Toda ferramenta passa por revisão antes de entrar na prateleira.</p>
      </div>
      <a class="btn" href="{repo}/issues/new?template=sugerir-ferramenta.yml">Sugerir ferramenta</a>
    </section>
  </div>
</div>
</div><!--/prat-->
</main>

<footer class="rodape">
  <div class="wrap">
    <span><b>Product Weekly</b> · O que importa em produto, toda semana. <a href="https://productweekly.com.br">productweekly.com.br</a></span>
    <span>Lista sob CC BY 4.0 · Dados do GitHub de {hoje} · <a href="{repo}">Código no GitHub</a></span>
  </div>
</footer>

<script>
(function () {{
  var ROT = {rotulos};
  var VAZIO = {{ c: 'all', n: 'all', e: 'all', tipo: 'all', api: false, t: false }};
  var estado = Object.assign({{}}, VAZIO);
  var termos = [];
  var campo = document.getElementById('busca');
  var semapi = document.getElementById('semapi');
  var sotestados = document.getElementById('sotestados');
  var dbtn = document.getElementById('tipo-btn');
  var dmenu = document.getElementById('tipo-menu');
  var dops = Array.prototype.slice.call(dmenu.querySelectorAll('li'));
  var fichas = Array.prototype.slice.call(document.querySelectorAll('.ficha'));
  var secoes = document.querySelectorAll('.secao');
  var botoes = document.querySelectorAll('[data-g]');
  function normalizar(t) {{ return t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim(); }}
  function passa(f, st, ignora) {{
    return (ignora === 'c' || st.c === 'all' || f.dataset.c === st.c)
      && (ignora === 'n' || st.n === 'all' || f.dataset.n === st.n)
      && (ignora === 'tipo' || st.tipo === 'all' || f.dataset.tipo === st.tipo)
      && (ignora === 'e' || st.e === 'all' || Number(f.dataset.e) >= Number(st.e))
      && (ignora === 'api' || !st.api || f.dataset.api === '0')
      && (ignora === 't' || !st.t || f.dataset.t === '1')
      && termos.every(function (t) {{ return f.dataset.busca.indexOf(t) !== -1; }});
  }}
  function conta(g, v) {{
    var st = Object.assign({{}}, estado); st[g] = v;
    return fichas.filter(function (f) {{ return passa(f, st); }}).length;
  }}
  function marcar(el, n, ativo) {{
    if (n === 0 && !ativo) el.setAttribute('aria-disabled', 'true'); else el.removeAttribute('aria-disabled');
  }}
  function tokens() {{
    var box = document.getElementById('tokens'); box.innerHTML = '';
    function add(txt, limpa) {{
      var b = document.createElement('button'); b.type = 'button'; b.className = 'token';
      b.innerHTML = '<b></b><span aria-hidden="true">×</span>'; b.firstChild.textContent = txt;
      b.setAttribute('aria-label', 'Tirar filtro ' + txt);
      b.addEventListener('click', function () {{ limpa(); aplicar(); }}); box.appendChild(b);
    }}
    if (campo.value.trim()) add('“' + campo.value.trim() + '”', function () {{ campo.value = ''; termos = []; }});
    if (estado.c !== 'all') add(ROT.c[estado.c], function () {{ estado.c = 'all'; }});
    if (estado.n !== 'all') add(ROT.n[estado.n], function () {{ estado.n = 'all'; }});
    if (estado.e !== 'all') add(ROT.e[estado.e], function () {{ estado.e = 'all'; }});
    if (estado.api) add('Sem API paga', function () {{ estado.api = false; }});
    if (estado.t) add('Só os testados', function () {{ estado.t = false; }});
    if (estado.tipo !== 'all') add(ROT.tipo[estado.tipo], function () {{ estado.tipo = 'all'; }});
    document.getElementById('ativos').hidden = box.children.length === 0;
    if (box.children.length > 1) {{
      var l = document.createElement('button'); l.type = 'button'; l.className = 'limpar'; l.textContent = 'Limpar tudo';
      l.addEventListener('click', limparTudo); box.appendChild(l);
    }}
  }}
  function aplicar() {{
    botoes.forEach(function (b) {{
      var g = b.dataset.g, v = b.dataset.v, ativo = estado[g] === v;
      b.setAttribute('aria-pressed', String(ativo));
      var n = conta(g, v); var el = b.querySelector('.n'); if (el) el.textContent = n; marcar(b, n, ativo);
    }});
    dops.forEach(function (o) {{
      var v = o.dataset.v, n = conta('tipo', v), ativo = estado.tipo === v;
      o.querySelector('.n').textContent = n; o.setAttribute('aria-selected', String(ativo)); marcar(o, n, ativo);
      if (ativo) {{ document.getElementById('tipo-atual').textContent = v === 'all' ? 'Todos os tipos' : ROT.tipo_n[v]; document.getElementById('tipo-n').textContent = n; }}
    }});
    semapi.checked = estado.api;
    sotestados.checked = estado.t;
    document.getElementById('n-testados').textContent = conta('t', true);
    var nApi = conta('api', true); document.getElementById('n-semapi').textContent = nApi;
    var total = 0;
    fichas.forEach(function (f) {{ var ok = passa(f, estado); f.hidden = !ok; if (ok) total++; }});
    secoes.forEach(function (s) {{
      var n = s.querySelectorAll('.ficha:not([hidden])').length;
      s.querySelector('.cont').textContent = n; s.hidden = n === 0;
    }});
    document.getElementById('mostrando').textContent = total;
    document.getElementById('vazio').hidden = total !== 0;
    tokens();
    try {{ localStorage.setItem('prateleira-de-repos', JSON.stringify(estado)); }} catch (e) {{}}
  }}
  function limparTudo() {{ estado = Object.assign({{}}, VAZIO); campo.value = ''; termos = []; aplicar(); }}
  botoes.forEach(function (b) {{
    b.addEventListener('click', function () {{
      if (b.getAttribute('aria-disabled') === 'true') return;
      var g = b.dataset.g, v = b.dataset.v;
      estado[g] = (g === 'c' && estado.c === v) ? 'all' : v; aplicar();
    }});
  }});
  semapi.addEventListener('change', function () {{ estado.api = semapi.checked; aplicar(); }});
  sotestados.addEventListener('change', function () {{ estado.t = sotestados.checked; aplicar(); }});
  var foco = -1;
  function realcar(i) {{
    dops.forEach(function (o) {{ o.classList.remove('ativo'); }});
    foco = i; if (i >= 0) {{ dops[i].classList.add('ativo'); dmenu.setAttribute('aria-activedescendant', dops[i].id); dops[i].scrollIntoView({{ block: 'nearest' }}); }}
  }}
  function abrir() {{
    dmenu.hidden = false; dbtn.setAttribute('aria-expanded', 'true');
    realcar(dops.findIndex(function (o) {{ return o.dataset.v === estado.tipo; }})); dmenu.focus();
  }}
  function fechar(devolver) {{ dmenu.hidden = true; dbtn.setAttribute('aria-expanded', 'false'); if (devolver) dbtn.focus(); }}
  function escolher(o) {{ if (o.getAttribute('aria-disabled') === 'true') return; estado.tipo = o.dataset.v; fechar(true); aplicar(); }}
  dbtn.addEventListener('click', function () {{ dmenu.hidden ? abrir() : fechar(false); }});
  dbtn.addEventListener('keydown', function (ev) {{ if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') {{ ev.preventDefault(); abrir(); }} }});
  dops.forEach(function (o, i) {{
    o.addEventListener('click', function () {{ escolher(o); }});
    o.addEventListener('mousemove', function () {{ if (foco !== i) realcar(i); }});
  }});
  dmenu.addEventListener('keydown', function (ev) {{
    var passo = function (d) {{ var i = foco; do {{ i = (i + d + dops.length) % dops.length; }} while (dops[i].getAttribute('aria-disabled') === 'true' && i !== foco); realcar(i); }};
    if (ev.key === 'ArrowDown') {{ ev.preventDefault(); passo(1); }}
    else if (ev.key === 'ArrowUp') {{ ev.preventDefault(); passo(-1); }}
    else if (ev.key === 'Home') {{ ev.preventDefault(); realcar(0); }}
    else if (ev.key === 'End') {{ ev.preventDefault(); realcar(dops.length - 1); }}
    else if (ev.key === 'Enter' || ev.key === ' ') {{ ev.preventDefault(); if (foco >= 0) escolher(dops[foco]); }}
    else if (ev.key === 'Escape' || ev.key === 'Tab') {{ fechar(ev.key === 'Escape'); }}
  }});
  document.addEventListener('click', function (ev) {{ if (!dmenu.hidden && !ev.target.closest('.drop')) fechar(false); }});
  campo.addEventListener('input', function () {{ termos = normalizar(campo.value).split(/\s+/).filter(Boolean); aplicar(); }});
  document.querySelectorAll('.sug').forEach(function (b) {{
    b.addEventListener('click', function () {{ campo.value = b.textContent; termos = normalizar(campo.value).split(/\s+/); estado = Object.assign({{}}, VAZIO); aplicar(); campo.focus(); }});
  }});
  document.querySelectorAll('[data-limpar]').forEach(function (b) {{ b.addEventListener('click', limparTudo); }});
  document.addEventListener('keydown', function (ev) {{
    if (ev.key === '/' && document.activeElement !== campo && !/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) {{ ev.preventDefault(); campo.focus(); }}
    if (ev.key === 'Escape' && document.activeElement === campo) {{ campo.value = ''; termos = []; aplicar(); }}
  }});
  document.querySelectorAll('.capa img').forEach(function (img) {{
    function sem() {{ img.parentNode.classList.add('sem-img'); img.remove(); }}
    if (img.complete && img.naturalWidth === 0) sem(); else img.addEventListener('error', sem);
  }});
  function copiar(txt, b, rotulo) {{
    function ok(m) {{ b.textContent = m; b.classList.add('ok'); setTimeout(function () {{ b.textContent = rotulo; b.classList.remove('ok'); }}, 2200); }}
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () {{ ok('Pedido copiado'); }}, function () {{ ok('Não deu para copiar: selecione o texto'); }});
    else ok('Não deu para copiar: selecione o texto');
  }}
  document.querySelectorAll('.verif').forEach(function (b) {{ var r = b.textContent; b.addEventListener('click', function () {{ copiar(b.dataset.pedido, b, r); }}); }});
  document.querySelectorAll('.btn-copiar').forEach(function (b) {{ var r = b.textContent; b.addEventListener('click', function () {{ copiar(b.dataset.pedido, b, r); }}); }});
  document.querySelectorAll('.link').forEach(function (b) {{
    b.addEventListener('click', function () {{
      var url = location.origin + location.pathname + '#' + b.dataset.id;
      function ok(txt) {{ b.textContent = txt; b.classList.add('ok'); setTimeout(function () {{ b.textContent = 'Copiar link'; b.classList.remove('ok'); }}, 2200); }}
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(function () {{ ok('Link copiado'); }}, function () {{ history.replaceState(null, '', '#' + b.dataset.id); ok('Link na barra de endereço'); }});
      else {{ history.replaceState(null, '', '#' + b.dataset.id); ok('Link na barra de endereço'); }}
    }});
  }});
  function irPara() {{
    var id = decodeURIComponent(location.hash.slice(1)); if (!id) return;
    var f = document.getElementById(id); if (!f || !f.classList.contains('ficha')) return;
    estado = Object.assign({{}}, VAZIO); campo.value = ''; termos = []; aplicar();
    f.scrollIntoView({{ block: 'center' }});
    f.classList.add('destaque'); setTimeout(function () {{ f.classList.remove('destaque'); }}, 2600);
  }}
  window.addEventListener('hashchange', irPara);
  try {{ var s = JSON.parse(localStorage.getItem('prateleira-de-repos') || 'null'); if (s && 'c' in s && 'n' in s && 'tipo' in s) estado = Object.assign({{}}, VAZIO, s); }} catch (e) {{}}
  aplicar();
  irPara();
}})();
</script>
</body>
</html>
"""


VARS_PRAT = """.prat {
  --linha: #3A3835;
  --f-corpo: "Gabarito", ui-sans-serif, system-ui, sans-serif;
  --f-serif: "Instrument Serif", Georgia, serif;
  --f-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
}
"""


def prefixar(css, pre=".prat "):
    """Põe o prefixo na frente de cada seletor, inclusive dentro de @media."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, i = [], 0
    while True:
        j = css.find("{", i)
        if j < 0:
            break
        sel = css[i:j].strip()
        if sel.startswith("@"):
            d, k = 1, j + 1
            while d:
                d += {"{": 1, "}": -1}.get(css[k], 0)
                k += 1
            out.append(sel + " {\n" + prefixar(css[j + 1:k - 1], pre) + "}")
            i = k
        else:
            k = css.find("}", j)
            sels = ", ".join(pre + x.strip() for x in sel.split(","))
            out.append(sels + " {" + css[j + 1:k] + "}")
            i = k + 1
    return "\n".join(out) + "\n"


def css_prateleira():
    return VARS_PRAT + prefixar((RAIZ / "scripts" / "estilo-prateleira.css").read_text(encoding="utf-8"))


def fragmento(pagina):
    """Miolo da página para o site do Product Weekly (sem topo, rodapé nem fontes)."""
    miolo = pagina[pagina.index("<!--prat-->") + len("<!--prat-->"):pagina.index("<!--/prat-->")]
    script = pagina[pagina.index("<script>"):pagina.index("</script>") + len("</script>")]
    return "<style>\n" + css_prateleira() + "</style>\n" + miolo.strip() + "\n" + script + "\n"


def main():
    (RAIZ / "README.md").write_text(readme(), encoding="utf-8")
    pagina = site()
    base = (RAIZ / "scripts" / "estilo-base.css").read_text(encoding="utf-8")
    (RAIZ / "docs" / "index.html").write_text(pagina.replace("%%CSS%%", base + css_prateleira()), encoding="utf-8")
    # Se a pasta do site do Product Weekly estiver ao lado, atualiza a página de lá também
    destino = RAIZ.parent / "site" / "src" / "data"
    if destino.is_dir():
        (destino / "prateleira.html").write_text(fragmento(pagina), encoding="utf-8")
        print("Página do site do Product Weekly atualizada:", destino.name + "/prateleira.html")
    print(f"README.md e docs/index.html gerados com {len(DADOS)} ferramentas.")


if __name__ == "__main__":
    main()
