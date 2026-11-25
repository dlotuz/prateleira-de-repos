#!/usr/bin/env python3
"""Gera o README.md e o site (docs/index.html) a partir de data/ferramentas.json.

Uso: python3 scripts/gerar.py
"""
import html
import json
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = json.loads((RAIZ / "data" / "ferramentas.json").read_text(encoding="utf-8"))
HOJE = date.today().strftime("%d/%m/%Y")
REPO_URL = "https://github.com/dlotuz/prateleira-de-repos"
SITE_URL = "https://dlotuz.github.io/prateleira-de-repos/"

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
    ("apps", "Construir apps"),
    ("ui", "Componentes de interface"),
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

# Nome curto de cada tarefa nos atalhos do site
TAREFA_CURTA = {
    "doc": "Texto e pesquisa", "audio": "Voz e transcrição", "video": "Vídeo", "visual": "Design e imagens",
    "skill": "Design sem cara de IA", "prod": "Dia a dia", "vida": "Finanças e vida", "agent": "Agentes",
    "apps": "Construir apps", "ui": "Componentes",
}
SUGESTOES = ["vídeo", "reunião", "Figma", "currículo", "legenda", "finanças"]


def nivel_de(i):
    nivel = "facil"
    for k, _, _, req in NIVEIS:
        if req & set(i["precisa"]):
            nivel = k
    return nivel


REGRAS = [
    "Dado sensível, seu ou de cliente, não vai para versão de nuvem de terceiro. Várias destas ferramentas têm versão cloud; use a que roda na sua máquina.",
    "GPL e AGPL podem ser usadas por conta própria. Colocar dentro de um produto vendido exige cuidado com a licença.",
    "Projeto de terceiro que você ainda está avaliando roda melhor em Docker, isolado do resto da máquina.",
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
    out = [f"### {i['nome']}", "", f"`{tipo}`{destaque} · [{i['repo']}]({i['url']})", "", i["o_que_faz"], ""]
    if i["alternativa_a"]:
        out += [f"**Alternativa a:** {i['alternativa_a']}", ""]
    out.append("**Para que serve:**")
    out += [f"- {u}" for u in i["para_que_serve"]]
    out.append("")
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


def ficha(i):
    t = i["tipo"]
    busca = normalizar(" ".join([i["nome"], i["repo"], i["o_que_faz"], " ".join(i["para_que_serve"]),
                                  i["alternativa_a"] or "", TIPO_NOME[t],
                                  " ".join(i["precisa"]), i["atencao"] or ""]))
    alt = f'<p class="alt"><span>Alternativa a</span>{e(i["alternativa_a"])}</p>' if i["alternativa_a"] else ""
    nota = ""
    if i["atencao"]:
        nota = f'<p class="nota{" forte" if i["atencao_forte"] else ""}">{e(i["atencao"])}</p>'
    precisa = "".join(f"<span>{e(p)}</span>" for p in i["precisa"])
    lic = f'<span class="aviso">{e(i["licenca"])}</span>' if i["licenca_alerta"] else f"<span>{e(i['licenca'])}</span>"
    sit = f'<span class="aviso">{e(i["situacao"])}</span>' if i["situacao_alerta"] else f"<span>{e(i['situacao'])}</span>"
    usos = "".join(f"<li>{e(u)}</li>" for u in i["para_que_serve"])
    return f"""
        <article class="ficha" data-tipo="{t}" data-c="{i['categoria']}" data-n="{nivel_de(i)}" data-api="{1 if 'Chave de API paga' in i['precisa'] else 0}" data-busca="{e(busca)}">
          <div class="topo"><span class="tipo">{TIPO_NOME[t]}</span><span class="cat">{CAT_NOME[i['categoria']]}</span></div>
          <h3><a href="{e(i['url'])}" target="_blank" rel="noopener">{e(i['nome'])}</a></h3>
          <span class="repo">{e(i['repo'])}</span>{alt}
          <p class="oque">{e(i['o_que_faz'])}</p>
          <div class="usos"><span class="rot">Para que serve</span><ul>{usos}</ul>{nota}</div>
          <div class="precisa"><span class="rot">Precisa de</span><span class="nv nv-{nivel_de(i)}">Nível {NIVEL_NOME[nivel_de(i)].lower()}</span>{precisa}</div>
          <div class="meta">{lic}<span>{e(i['estrelas'])} estrelas</span><span>push {e(i['ultimo_push'])}</span>{sit}</div>
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
    opcoes = '<option value="all">Todos os tipos</option>' + "".join(
        f'<option value="{k}">{nome}</option>' for k, nome, _ in TIPOS if conta(lambda x: x["tipo"] == k))
    sugestoes = "".join(f'<button class="sug" type="button">{e(t)}</button>' for t in SUGESTOES)
    rotulos = json.dumps({
        "c": {k: TAREFA_CURTA[k] for k, _ in CATEGORIAS},
        "n": {k: f"Nível {nome.lower()}" for k, nome, _, _ in NIVEIS},
        "tipo": TIPO_NOME,
        "tipo_n": {k: nome for k, nome, _ in TIPOS},
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
    return PAGINA.format(n=n, hoje=HOJE, hoje_curto=HOJE[:5], tarefas=tarefas, seg=seg, opcoes=opcoes,
                         sugestoes=sugestoes, rotulos=rotulos, secoes=secoes, legenda=legenda, regras=regras,
                         repo=REPO_URL, n_semapi=conta(lambda x: "Chave de API paga" not in x["precisa"]))


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
/* Visual do Product Weekly: papel + tinta + laranja; topo escuro, filtros em pílula, fichas por destaque, rodapé laranja */
:root {{
  --papel:#EEEBE4; --tinta:#121212; --lar:#FF5B1F; --graf:#6F6B64; --bq:#F8F6F1; --creme:#F2ECE3; --grade:#DDD8CE; --linha:#3A3835;
  --f-corpo:"Gabarito", ui-sans-serif, system-ui, sans-serif;
  --f-serif:"Instrument Serif", Georgia, serif;
  --f-mono:"JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{ margin: 0; background: var(--papel); color: var(--tinta); font-family: var(--f-corpo); font-size: 16px; line-height: 1.45; -webkit-font-smoothing: antialiased; }}
[hidden] {{ display: none !important; }}
a {{ color: inherit; text-decoration: none; }}
h1, h2, h3 {{ font-weight: 900; letter-spacing: -.025em; line-height: 1; margin: 0; text-wrap: balance; }}
.wrap {{ max-width: 1240px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.mono {{ font-family: var(--f-mono); font-size: 12px; letter-spacing: .06em; text-transform: uppercase; }}
:focus-visible {{ outline: 3px solid var(--lar); outline-offset: 3px; }}

.barra {{ background: var(--tinta); color: var(--bq); }}
.barra .wrap {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-block: 18px; flex-wrap: wrap; }}
.logo {{ display: flex; align-items: center; gap: 12px; }}
.logo .ico {{ width: 40px; height: 40px; border-radius: 10px; background: var(--creme); color: var(--tinta); display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 19px; letter-spacing: -.04em; }}
.logo .ico i {{ color: var(--lar); font-style: normal; }}
.logo b {{ font-size: 22px; font-weight: 900; letter-spacing: -.025em; }}
.logo .pil {{ background: var(--lar); color: var(--bq); border-radius: 999px; padding: 4px 12px; font-weight: 900; font-size: 17px; line-height: 1; letter-spacing: -.02em; }}
.nav {{ display: flex; gap: 10px 20px; align-items: center; flex-wrap: wrap; font-weight: 600; }}
.nav a:hover {{ color: var(--lar); }}
.cta {{ background: var(--lar); color: var(--bq); border-radius: 999px; padding: 9px 16px; font-weight: 800; }}
.nav .cta:hover {{ color: var(--bq); filter: brightness(1.05); }}

.hero {{ background: var(--tinta); color: var(--bq); }}
.hero .wrap {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 32px; align-items: end; padding-block: 40px 64px; }}
.hero .mono {{ color: #B9B3A8; }}
.hero h1 {{ font-size: clamp(52px, 10vw, 120px); letter-spacing: -.05em; line-height: .88; margin-top: 14px; }}
.hero h1 span {{ color: var(--lar); }}
.hero p {{ margin: 22px 0 0; max-width: 58ch; font-size: 18px; color: #D9D4CA; }}
.hero p em {{ font-family: var(--f-serif); font-size: 21px; color: var(--bq); }}
.numeros {{ display: grid; grid-template-columns: repeat(3, auto); border: 1px solid var(--linha); border-radius: 12px; }}
.numeros div {{ padding: 14px 20px; display: grid; gap: 6px; min-width: 0; }}
.numeros div + div {{ border-left: 1px solid var(--linha); }}
.numeros b {{ font-size: 32px; font-weight: 900; letter-spacing: -.03em; font-variant-numeric: tabular-nums; }}
.numeros b.l {{ color: var(--lar); }}
.numeros .mono {{ font-size: 10.5px; }}

.faixa {{ background: var(--lar); color: var(--tinta); }}
.faixa .wrap {{ display: flex; gap: 10px 18px; align-items: baseline; flex-wrap: wrap; padding-block: 16px; }}
.faixa .mono {{ font-weight: 700; }}
.faixa p {{ margin: 0; font-size: 17px; font-weight: 500; min-width: 0; flex: 1 1 320px; }}

main .wrap {{ padding-block: 36px 72px; display: grid; gap: 56px; }}
.filtros {{ display: grid; gap: 14px; }}
.linha-f {{ display: grid; grid-template-columns: 110px minmax(0, 1fr); gap: 12px; align-items: start; }}
.linha-f > .mono {{ color: var(--graf); padding-top: 8px; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.chip {{ font-family: var(--f-mono); font-size: 12px; letter-spacing: .05em; text-transform: uppercase; font-weight: 500; padding: 7px 12px; border-radius: 999px; border: 1.5px solid var(--tinta); background: transparent; color: var(--tinta); cursor: pointer; display: inline-flex; gap: 7px; align-items: center; }}
.chip span {{ color: var(--graf); font-variant-numeric: tabular-nums; }}
.chip:hover {{ background: var(--bq); }}
.chip[aria-pressed="true"] {{ background: var(--tinta); color: var(--bq); }}
.chip[aria-pressed="true"] span {{ color: var(--lar); }}
.busca {{ display: grid; grid-template-columns: 110px minmax(0, 1fr) auto; gap: 12px; align-items: center; }}
.busca label {{ color: var(--graf); }}
.busca input {{ width: 100%; min-width: 0; font-family: var(--f-corpo); font-size: 19px; font-weight: 600; color: var(--tinta); background: var(--bq); border: 2px solid var(--tinta); border-radius: 999px; padding: 12px 20px; outline: none; }}
.busca input::placeholder {{ color: var(--graf); font-weight: 500; }}
.busca input:focus {{ border-color: var(--lar); box-shadow: 0 0 0 3px rgba(255, 91, 31, .25); }}
.busca kbd {{ border: 1.5px solid var(--grade); border-radius: 6px; padding: 3px 8px; color: var(--graf); background: var(--bq); }}
.resumo {{ display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; color: var(--graf); }}
.resumo b {{ color: var(--tinta); }}
.limpar {{ font-family: var(--f-mono); font-size: 12px; text-transform: uppercase; letter-spacing: .05em; background: none; border: 0; padding: 0; color: var(--tinta); text-decoration: underline; text-underline-offset: 3px; cursor: pointer; }}

.filtros .tit {{ color: var(--graf); }}
.sugestoes {{ display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: baseline; padding-left: 122px; margin-top: -4px; }}
.sugestoes .mono {{ color: var(--graf); font-size: 11px; }}
.sug {{ font: 600 15px/1.2 var(--f-corpo); color: var(--tinta); background: none; border: 0; padding: 0; text-decoration: underline; text-decoration-color: var(--lar); text-decoration-thickness: 2px; text-underline-offset: 4px; cursor: pointer; }}
.sug:hover {{ color: var(--lar); }}
.bloco {{ display: grid; gap: 12px; }}
.tarefas {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 10px; }}
@media (min-width: 1100px) {{ .tarefas {{ grid-template-columns: repeat(5, minmax(0, 1fr)); }} }}
.tarefa {{ position: relative; text-align: left; font-family: var(--f-corpo); color: var(--tinta); background: var(--bq); border: 1.5px solid var(--grade); border-radius: 14px; padding: 14px 44px 14px 16px; cursor: pointer; display: grid; gap: 3px; min-width: 0; }}
.tarefa b {{ font-weight: 900; font-size: 19px; letter-spacing: -.02em; line-height: 1.1; }}
.tarefa .desc {{ font-size: 13px; color: var(--graf); line-height: 1.3; }}
.tarefa .n {{ position: absolute; top: 14px; right: 14px; font-family: var(--f-mono); font-size: 12px; color: var(--graf); font-variant-numeric: tabular-nums; }}
.tarefa:hover {{ border-color: var(--tinta); }}
.tarefa[aria-pressed="true"] {{ background: var(--tinta); border-color: var(--tinta); color: var(--bq); }}
.tarefa[aria-pressed="true"] .desc {{ color: #B9B3A8; }}
.tarefa[aria-pressed="true"] .n {{ color: var(--lar); }}
.linha2 {{ display: flex; flex-wrap: wrap; gap: 14px 28px; align-items: center; }}
.nivel, .tiposel {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
.seg {{ display: inline-flex; border: 1.5px solid var(--tinta); border-radius: 999px; padding: 3px; gap: 2px; flex-wrap: wrap; }}
.segb {{ font: 700 15px/1 var(--f-corpo); color: var(--tinta); background: transparent; border: 0; border-radius: 999px; padding: 9px 14px; cursor: pointer; display: inline-flex; gap: 7px; align-items: baseline; }}
.segb .n {{ font-family: var(--f-mono); font-size: 11px; font-weight: 500; color: var(--graf); font-variant-numeric: tabular-nums; }}
.segb:hover {{ background: var(--bq); }}
.segb[aria-pressed="true"] {{ background: var(--tinta); color: var(--bq); }}
.segb[aria-pressed="true"] .n {{ color: var(--lar); }}
.toggle {{ display: inline-flex; align-items: center; gap: 10px; font-weight: 700; font-size: 15px; cursor: pointer; position: relative; }}
.toggle input {{ position: absolute; opacity: 0; width: 1px; height: 1px; }}
.toggle .caixa {{ width: 40px; height: 24px; border-radius: 999px; background: var(--grade); position: relative; flex: none; transition: background .15s; }}
.toggle .caixa::after {{ content: ""; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px; border-radius: 50%; background: var(--bq); transition: transform .15s; }}
.toggle input:checked + .caixa {{ background: var(--lar); }}
.toggle input:checked + .caixa::after {{ transform: translateX(16px); }}
.toggle input:focus-visible + .caixa {{ outline: 3px solid var(--lar); outline-offset: 3px; }}
.toggle .n {{ font-style: normal; font-family: var(--f-mono); font-size: 11px; font-weight: 500; color: var(--graf); }}
.tiposel select {{ font: 700 15px/1 var(--f-corpo); color: var(--tinta); background: var(--bq); border: 1.5px solid var(--tinta); border-radius: 999px; padding: 10px 36px 10px 16px; appearance: none; -webkit-appearance: none; cursor: pointer;
  background-image: linear-gradient(45deg, transparent 50%, var(--tinta) 50%), linear-gradient(135deg, var(--tinta) 50%, transparent 50%); background-position: right 18px center, right 13px center; background-size: 5px 5px; background-repeat: no-repeat; }}
[aria-disabled="true"] {{ opacity: .38; }}
.ativos {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; min-height: 34px; }}
.ativos > .mono {{ color: var(--graf); }}
.ativos b {{ color: var(--tinta); }}
.tokens {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
.token {{ font: 700 14px/1 var(--f-corpo); background: var(--lar); color: var(--tinta); border: 0; border-radius: 999px; padding: 8px 12px; cursor: pointer; display: inline-flex; gap: 8px; align-items: center; }}
.token span {{ font-size: 16px; line-height: 0; }}
.precisa .nv {{ font-weight: 800; }}
.precisa .nv-facil {{ background: var(--tinta) !important; color: var(--bq); border-color: var(--tinta) !important; }}
.vazio {{ display: grid; gap: 10px; }}
.vazio p {{ margin: 0; }}
.vazio .sug {{ margin: 0 8px; text-transform: none; letter-spacing: 0; }}
.secao {{ display: grid; gap: 28px; }}
.sh {{ display: flex; align-items: baseline; justify-content: space-between; gap: 16px; flex-wrap: wrap; border-top: 2px solid var(--tinta); padding-top: 22px; }}
.sh h2 {{ font-size: clamp(34px, 5.5vw, 60px); letter-spacing: -.04em; }}
.sh .mono {{ color: var(--graf); }}
.sh .mono b {{ color: var(--tinta); }}
.grade {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }}
@media (max-width: 400px) {{ .grade {{ grid-template-columns: 1fr; }} }}

.ficha {{ background: var(--bq); border: 1px solid var(--grade); border-radius: 14px; padding: 22px; display: grid; grid-template-rows: auto auto auto auto auto 1fr auto auto; gap: 10px; min-width: 0; }}
.topo {{ display: flex; justify-content: space-between; align-items: center; gap: 8px; flex-wrap: wrap; }}
.tipo {{ font-family: var(--f-mono); font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; background: var(--tinta); color: var(--bq); border-radius: 999px; padding: 4px 10px; }}
.ficha[data-tipo="skill"] .tipo {{ background: var(--lar); color: var(--tinta); }}
.cat {{ font-family: var(--f-mono); font-size: 11px; letter-spacing: .05em; text-transform: uppercase; color: var(--graf); }}
.ficha h3 {{ font-size: 25px; letter-spacing: -.03em; margin-top: 6px; }}
.ficha h3 a:hover {{ color: var(--lar); }}
.repo {{ font-family: var(--f-mono); font-size: 12px; color: var(--graf); overflow-wrap: anywhere; }}
.alt {{ margin: 2px 0 0; font-weight: 800; font-size: 15px; display: flex; flex-wrap: wrap; align-items: baseline; gap: 2px 8px; }}
.alt span {{ font-family: var(--f-mono); font-size: 11px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; color: var(--graf); }}
.oque {{ margin: 4px 0 0; }}
.usos {{ display: grid; gap: 6px; align-content: start; margin-top: 4px; }}
.rot {{ font-family: var(--f-mono); font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--lar); }}
.usos ul {{ margin: 0; padding-left: 18px; display: grid; gap: 4px; }}
.usos li::marker {{ color: var(--lar); }}
.nota {{ margin: 8px 0 0; font-size: 14px; background: var(--creme); border: 1px solid var(--grade); border-radius: 10px; padding: 9px 12px; }}
.nota.forte {{ background: transparent; border: 1.5px solid var(--lar); }}
.precisa {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-top: 4px; }}
.precisa .rot {{ margin-right: 2px; }}
.precisa span:not(.rot) {{ font-size: 13px; font-weight: 600; border: 1px solid var(--grade); background: var(--papel); border-radius: 999px; padding: 3px 10px; }}
.meta {{ display: flex; flex-wrap: wrap; gap: 4px 14px; border-top: 1px solid var(--grade); padding-top: 12px; margin-top: 6px; font-family: var(--f-mono); font-size: 11px; letter-spacing: .04em; text-transform: uppercase; color: var(--graf); font-variant-numeric: tabular-nums; }}
.meta .aviso {{ color: var(--tinta); }}
.meta .aviso::before {{ content: "●"; color: var(--lar); margin-right: 5px; }}
.vazio {{ font-size: 18px; color: var(--graf); }}

.tipos {{ display: grid; gap: 22px; }}
.tipos .lista {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 18px 28px; }}
.tipos b {{ font-weight: 900; font-size: 19px; }}
.tipos p {{ margin: 4px 0 0; color: var(--graf); }}

.regras {{ background: var(--tinta); color: var(--bq); border-radius: 18px; padding: 32px; display: grid; gap: 16px; }}
.regras h2 {{ font-size: clamp(32px, 5vw, 48px); letter-spacing: -.04em; }}
.regras h2 span {{ color: var(--lar); }}
.regras ul {{ margin: 0; padding-left: 20px; display: grid; gap: 8px; max-width: 80ch; color: #D9D4CA; }}
.regras li::marker {{ color: var(--lar); }}

.sugira {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 20px; align-items: center; border: 2px solid var(--tinta); border-radius: 18px; padding: 28px 32px; }}
.sugira h2 {{ font-size: clamp(28px, 4vw, 40px); letter-spacing: -.035em; }}
.sugira p {{ margin: 8px 0 0; max-width: 60ch; color: var(--graf); }}
.btn {{ display: inline-flex; align-items: center; gap: 10px; padding: 14px 22px; border-radius: 999px; font-weight: 800; font-size: 17px; background: var(--tinta); color: var(--bq); white-space: nowrap; }}
.btn:hover {{ background: var(--lar); color: var(--tinta); }}

.rodape {{ background: var(--lar); color: var(--tinta); }}
.rodape .wrap {{ display: flex; justify-content: space-between; gap: 8px 24px; flex-wrap: wrap; padding-block: 22px; font-size: 14px; }}
.rodape b {{ font-weight: 800; }}
.rodape a {{ text-decoration: underline; text-underline-offset: 3px; }}

@media (max-width: 760px) {{
  .hero .wrap {{ grid-template-columns: 1fr; padding-block: 32px 44px; }}
  .hero p {{ font-size: 17px; }}
  .numeros {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
  .numeros div {{ padding: 12px; }}
  .numeros b {{ font-size: 24px; }}
  .numeros .mono {{ font-size: 9.5px; overflow-wrap: anywhere; }}
  .linha-f {{ grid-template-columns: 1fr; gap: 8px; }}
  .busca {{ grid-template-columns: 1fr; gap: 8px; }}
  .sugestoes {{ padding-left: 0; margin-top: 0; }}
  .tarefas {{ grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }}
  .tarefa {{ padding: 12px 34px 12px 12px; }}
  .tarefa b {{ font-size: 16px; }}
  .tarefa .desc {{ display: none; }}
  .tarefa .n {{ top: 12px; right: 10px; }}
  .linha2 {{ gap: 14px; }}
  .busca kbd {{ display: none; }}
  .busca input {{ font-size: 17px; }}
  .linha-f > .mono {{ padding-top: 0; }}
  .regras, .sugira {{ padding: 24px 20px; }}
  .sugira {{ grid-template-columns: 1fr; }}
  .logo b {{ display: none; }}
  .nav a:not(.cta) {{ display: none; }}
}}
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

<section class="hero">
  <div class="wrap">
    <div>
      <span class="mono">Lista aberta · Product Weekly</span>
      <h1>Prateleira <span>de repos.</span></h1>
      <p>Repositórios de IA de código aberto, separados pelo que você quer fazer. <em>Cada um diz o que precisa para rodar,</em> quanto custa e qual produto conhecido ele substitui.</p>
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

<main>
  <div class="wrap">
    <div class="filtros">
      <div class="busca"><label class="mono" for="busca">Buscar</label><input id="busca" type="search" placeholder="Digite o que você quer fazer: vídeo, reunião, Figma, currículo…" autocomplete="off" spellcheck="false"><kbd class="mono" aria-hidden="true">/</kbd></div>
      <div class="sugestoes"><span class="mono">Experimente</span>{sugestoes}</div>
      <div class="bloco"><span class="mono tit">O que você quer fazer?</span><div class="tarefas" role="group" aria-label="Filtrar pelo que você quer fazer">{tarefas}</div></div>
      <div class="linha2">
        <div class="nivel"><span class="mono tit">Nível</span><div class="seg" role="group" aria-label="Filtrar por nível">{seg}</div></div>
        <label class="toggle" for="semapi"><input type="checkbox" id="semapi"><span class="caixa" aria-hidden="true"></span><span>Sem API paga <i class="n" id="n-semapi">{n_semapi}</i></span></label>
        <label class="tiposel" for="tipo"><span class="mono tit">Tipo</span><select id="tipo">{opcoes}</select></label>
      </div>
      <div class="ativos"><div class="tokens" id="tokens"></div><span class="mono">Mostrando <b id="mostrando">{n}</b> de {n}</span></div>
    </div>
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
  var VAZIO = {{ c: 'all', n: 'all', tipo: 'all', api: false }};
  var estado = Object.assign({{}}, VAZIO);
  var termos = [];
  var campo = document.getElementById('busca');
  var semapi = document.getElementById('semapi');
  var seltipo = document.getElementById('tipo');
  var fichas = Array.prototype.slice.call(document.querySelectorAll('.ficha'));
  var secoes = document.querySelectorAll('.secao');
  var botoes = document.querySelectorAll('[data-g]');
  function normalizar(t) {{ return t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim(); }}
  function passa(f, st, ignora) {{
    return (ignora === 'c' || st.c === 'all' || f.dataset.c === st.c)
      && (ignora === 'n' || st.n === 'all' || f.dataset.n === st.n)
      && (ignora === 'tipo' || st.tipo === 'all' || f.dataset.tipo === st.tipo)
      && (ignora === 'api' || !st.api || f.dataset.api === '0')
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
    if (estado.api) add('Sem API paga', function () {{ estado.api = false; }});
    if (estado.tipo !== 'all') add(ROT.tipo[estado.tipo], function () {{ estado.tipo = 'all'; }});
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
    Array.prototype.forEach.call(seltipo.options, function (o) {{
      var n = conta('tipo', o.value);
      o.textContent = (o.value === 'all' ? 'Todos os tipos' : ROT.tipo_n[o.value]) + ' (' + n + ')';
      o.disabled = n === 0 && o.value !== estado.tipo;
    }});
    seltipo.value = estado.tipo;
    semapi.checked = estado.api;
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
  seltipo.addEventListener('change', function () {{ estado.tipo = seltipo.value; aplicar(); }});
  campo.addEventListener('input', function () {{ termos = normalizar(campo.value).split(/\s+/).filter(Boolean); aplicar(); }});
  document.querySelectorAll('.sug').forEach(function (b) {{
    b.addEventListener('click', function () {{ campo.value = b.textContent; termos = normalizar(campo.value).split(/\s+/); estado = Object.assign({{}}, VAZIO); aplicar(); campo.focus(); }});
  }});
  document.querySelectorAll('[data-limpar]').forEach(function (b) {{ b.addEventListener('click', limparTudo); }});
  document.addEventListener('keydown', function (ev) {{
    if (ev.key === '/' && document.activeElement !== campo && !/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) {{ ev.preventDefault(); campo.focus(); }}
    if (ev.key === 'Escape' && document.activeElement === campo) {{ campo.value = ''; termos = []; aplicar(); }}
  }});
  try {{ var s = JSON.parse(localStorage.getItem('prateleira-de-repos') || 'null'); if (s && 'c' in s && 'n' in s && 'tipo' in s) estado = Object.assign({{}}, VAZIO, s); }} catch (e) {{}}
  aplicar();
}})();
</script>
</body>
</html>
"""


def main():
    (RAIZ / "README.md").write_text(readme(), encoding="utf-8")
    pagina = site()
    (RAIZ / "docs" / "index.html").write_text(pagina, encoding="utf-8")
    print(f"README.md e docs/index.html gerados com {len(DADOS)} ferramentas.")


if __name__ == "__main__":
    main()
