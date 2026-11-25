# Prateleira de Repositórios

Repositórios de IA de código aberto, separados pelo que você quer fazer. São 72 até agora. Cada um diz o que faz, o que precisa para rodar, quanto custa e qual produto conhecido ele substitui.

**Versão com filtros:** https://www.productweekly.com.br/prateleira

Um projeto do [Product Weekly](https://productweekly.com.br), o que importa em produto, toda semana. Curadoria de Eduardo Oliveira.

## Como ler cada item

- **Tipo:** App, Skill, Terminal e outros (explicados [no fim da página](#os-tipos)).
- **Nível:** Fácil (baixa e usa, ou abre no navegador), Médio (precisa do Claude Code ou do terminal) ou Avançado (servidor, GPU ou programação).
- **Precisa de:** o que você precisa ter para usar.
- **Alternativa a:** o produto pago ou fechado que ela substitui, quando existe.
- **Atenção:** licença, custo escondido, projeto parado ou qualquer coisa que você deve saber antes.

## Comece por aqui

- [anarlog](#anarlog): Anotador de reuniões no estilo do Granola, que roda no computador.
- [claude-video (/watch)](#claude-video-watch): Dá ao Claude a capacidade de assistir um vídeo.
- [Emil Kowalski Skills](#emil-kowalski-skills): 19 skills de design engineering do Emil Kowalski (ex-Vercel e Linear) para animação e acabamento de interface: escolhem a curva e a duração certas, revisam animações, coordenam o que se mexe junto e testam a tela com dados extremos.
- [Firecrawl](#firecrawl): Lê sites inteiros e devolve o conteúdo limpo, em Markdown ou JSON, pronto para um agente usar.
- [Humanizer](#humanizer): Skill que reescreve texto gerado por IA para soar como uma pessoa escreveu, sem mudar o que ele diz.
- [Hyperframes](#hyperframes): Transforma HTML em vídeo.
- [Impeccable](#impeccable): Vocabulário de design para o agente.
- [MarkItDown](#markitdown): Converte PDF, Word, Excel, PowerPoint e HTML em Markdown, que é o formato que o agente lê melhor.
- [Postiz](#postiz): Agenda e publica posts em várias redes (Instagram, LinkedIn, TikTok, YouTube e outras), com um agente de IA que ajuda a criar e programar.
- [video-use](#video-use): Skill do Claude Code que edita vídeo conversando.
- [Whisper](#whisper): Transcreve áudio e vídeo localmente, em português e outras línguas, sem serviço externo.
- [whisper.cpp](#whispercpp): O Whisper reescrito para rodar rápido no Mac.
- [Yogurt](#yogurt): Anotações de reunião que ficam no computador.

## O que você quer fazer?

- [Ler, pesquisar e escrever](#ler-pesquisar-e-escrever) (5)
- [Transcrever e trabalhar com voz](#transcrever-e-trabalhar-com-voz) (5)
- [Criar e editar vídeo](#criar-e-editar-video) (19)
- [Design, apresentações e imagens](#design-apresentacoes-e-imagens) (9)
- [Deixar o design feito com IA mais bonito](#deixar-o-design-feito-com-ia-mais-bonito) (10)
- [Organizar o dia a dia](#organizar-o-dia-a-dia) (8)
- [Finanças, viagem e currículo](#financas-viagem-e-curriculo) (4)
- [Agentes e automação](#agentes-e-automacao) (6)
- [Cursos, área de membros e comunidade](#cursos-area-de-membros-e-comunidade) (1)
- [Construir apps e interfaces](#construir-apps-e-interfaces) (5)

## Ler, pesquisar e escrever

### Firecrawl

`Terminal` · comece por esta · [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)

Lê sites inteiros e devolve o conteúdo limpo, em Markdown ou JSON, pronto para um agente usar.

**Para que serve:**
- Pesquisa de mercado: preços e recursos de concorrentes
- Documentação pública de API puxada para análise
- Acompanhar mudanças em sites que você monitora

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/firecrawl/firecrawl` Prefira a versão que roda na sua máquina, com Docker.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** AGPL-3.0 · **Estrelas:** 198k · **Último push:** 03/11/2026 · **Situação:** Ativo

> **Atenção:** Licença AGPL: uso próprio tudo bem, mas não pode ir dentro de um produto que seja vendido.

### Humanizer

`Skill` · comece por esta · [blader/humanizer](https://github.com/blader/humanizer)

Skill que reescreve texto gerado por IA para soar como uma pessoa escreveu, sem mudar o que ele diz. Usa o guia da Wikipedia de sinais de escrita por IA (26 padrões).

**Para que serve:**
- Post do LinkedIn sem cara de texto de chatbot
- Revisar e-mail, apresentação e documento antes de mandar
- Corrigir vícios como "não é só X, é Y" e frases de efeito no fim

**Como começar:** No Claude Code: `/plugin marketplace add blader/humanizer` e `/plugin install humanizer@humanizer`. Depois, `/humanizer` com o texto.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 66k · **Último push:** 28/10/2026 · **Situação:** Ativo

> **Atenção:** O objetivo é ler melhor, não enganar detector de IA: os próprios autores dizem que os detectores ainda marcam a maior parte.

### MarkItDown

`Terminal` · comece por esta · [microsoft/markitdown](https://github.com/microsoft/markitdown)

Converte PDF, Word, Excel, PowerPoint e HTML em Markdown, que é o formato que o agente lê melhor.

**Para que serve:**
- Manual ou especificação de API em PDF vira texto para o agente analisar
- Planilha lida e resumida sem abrir o Excel
- Apresentações antigas viram texto pesquisável

**Como começar:** No terminal: `pip install "markitdown[all]"` e depois `markitdown arquivo.pdf > arquivo.md`.

**Nível:** Médio · **Precisa de:** Terminal · **Licença:** MIT · **Estrelas:** 194k · **Último push:** 28/10/2026 · **Situação:** Ativo

### Marketing Skills

`Skill` · [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)

Pacote de skills de marketing para o Claude Code: conversão, copy, SEO, analytics e growth.

**Para que serve:**
- Melhorar bio, chamadas e texto de lançamento de um perfil ou produto
- Revisar uma landing page com olhar de conversão

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/coreyhaines31/marketingskills`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 61k · **Último push:** 18/11/2026 · **Situação:** Ativo

### global-law

`Dados` · [lexifina/global-law](https://github.com/lexifina/global-law)

As leis do mundo num repositório git: qualquer artigo, de qualquer país, em qualquer data, com a lei que escreveu cada palavra.

**Para que serve:**
- Ver como um artigo de lei mudou ao longo do tempo
- Dar ao agente a lei exata como fonte de uma análise

**Como começar:** Abra o repositório e navegue até a pasta do país e do artigo que quer consultar.

**Nível:** Fácil · **Precisa de:** Só consultar · **Licença:** CC0 · **Estrelas:** 2,1k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** Conferir se o Brasil está coberto antes de contar com ele.


## Transcrever e trabalhar com voz

### Whisper

`Modelo` · comece por esta · [openai/whisper](https://github.com/openai/whisper)

Transcreve áudio e vídeo localmente, em português e outras línguas, sem serviço externo.

**Para que serve:**
- Gravação de reunião vira transcrição e depois ata
- Aulas e treinamentos viram material de consulta
- Entrevistas transcritas sem o áudio sair do Mac

**Como começar:** No terminal: `pip install -U openai-whisper` e depois `whisper gravacao.mp3 --language Portuguese`.

**Nível:** Médio · **Precisa de:** Terminal · **Licença:** MIT · **Estrelas:** 112k · **Último push:** 31/08/2026 · **Situação:** Ativo

### whisper.cpp

`Terminal` · comece por esta · [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

O Whisper reescrito para rodar rápido no Mac. Transcreve e gera legenda SRT com o tempo de cada palavra.

**Para que serve:**
- Transcrever uma gravação e sincronizar cada animação com a fala
- Legenda automática para vídeo de tutorial
- Transcrever reunião mais rápido que o Whisper original no Mac

**Como começar:** No Mac: `brew install whisper-cpp`. Depois, peça ao Claude Code para transcrever um arquivo com ele.

**Nível:** Médio · **Precisa de:** Terminal · **Licença:** MIT · **Estrelas:** 55k · **Último push:** 05/11/2026 · **Situação:** Ativo

### GPT-SoVITS

`App` · [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

Transforma texto em fala e clona uma voz a partir de cerca de 1 minuto de áudio.

**Alternativa a:** ElevenLabs (clonagem de voz)

**Para que serve:**
- Narração de vídeos sem precisar gravar
- Áudio de tutorial atualizado sem regravar a cada versão

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/RVC-Boss/GPT-SoVITS` Precisa de placa de vídeo Nvidia.

**Nível:** Avançado · **Precisa de:** Terminal, GPU · **Licença:** MIT · **Estrelas:** 65k · **Último push:** 31/10/2026 · **Situação:** Ativo

> **Atenção:** Só clonar a voz de alguém com o consentimento da pessoa.

### Kokoro

`Modelo` · [hexgrad/kokoro](https://github.com/hexgrad/kokoro)

Modelo leve de voz (82 milhões de parâmetros) que transforma texto em fala com boa qualidade e roda no computador.

**Para que serve:**
- Narração rápida para vídeo curto
- Locução de teste antes de gravar a sua voz

**Como começar:** No terminal: `pip install kokoro` e peça ao Claude Code um script que leia um texto em voz alta.

**Nível:** Médio · **Precisa de:** Terminal · **Licença:** Apache-2.0 · **Estrelas:** 10,2k · **Último push:** 06/08/2025 · **Situação:** Estável

> **Atenção:** Sem atualização no repositório desde ago/2025, mas o modelo é estável e outras ferramentas, como o huashu-motion, usam.

### VoiceStudio

`App` · [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

Estúdio de voz que roda no computador, alternativa local à ElevenLabs: clona e cria vozes, dubla vídeo, dita, transcreve e narra em 646 línguas.

**Alternativa a:** ElevenLabs

**Para que serve:**
- Dublar um vídeo para inglês ou espanhol mantendo o tempo da fala
- Narração com uma voz criada a partir de uma descrição
- Ditado e transcrição sem o áudio sair do Mac

**Como começar:** Baixe o app em voicestudio.sh e escolha no gerenciador só os modelos que vai usar.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** AGPL-3.0 · **Estrelas:** 104k · **Último push:** 08/11/2026 · **Situação:** Ativo

> **Atenção:** AGPL, e trabalho pago para cliente pede a licença Pro. Faz mais que o GPT-SoVITS e tem interface: preferir este. Clonar voz só com consentimento.


## Criar e editar vídeo

### claude-video (/watch)

`Skill` · comece por esta · [bradautomates/claude-video](https://github.com/bradautomates/claude-video)

Dá ao Claude a capacidade de assistir um vídeo: baixa, extrai quadros com horário e transcreve, e entrega tudo para ele analisar.

**Para que serve:**
- Mandar o link de um vídeo do YouTube e o Claude resumir, citar trechos e mostrar o que aparece na tela
- Analisar vídeos de referência antes de criar os seus
- Revisar o seu próprio vídeo antes de publicar

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/bradautomates/claude-video`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 21k · **Último push:** 25/09/2026 · **Situação:** Ativo

> **Atenção:** Funciona sem chave de API no modo local (ffmpeg e yt-dlp); a transcrição local usa WhisperX.

### Hyperframes

`Terminal` · comece por esta · [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

Transforma HTML em vídeo. O agente escreve as animações em código e ele renderiza o arquivo final.

**Para que serve:**
- Motor de várias skills de vídeo para o Claude Code
- Vídeo de tutorial com animação no ritmo da fala
- Abertura e vinheta para apresentação e posts

**Como começar:** Com o Node 22 instalado, rode `npx hyperframes` no terminal ou peça ao Claude Code para montar o vídeo com ele.

**Nível:** Médio · **Precisa de:** Terminal · **Licença:** Apache-2.0 · **Estrelas:** 79k · **Último push:** 05/11/2026 · **Situação:** Ativo

### video-use

`Skill` · comece por esta · [browser-use/video-use](https://github.com/browser-use/video-use)

Skill do Claude Code que edita vídeo conversando: você coloca as gravações numa pasta, pede o vídeo e recebe o arquivo final.

**Para que serve:**
- Gravação de tutorial sem "éé", pausas e falsos começos
- Legenda no seu estilo e correção de cor automáticas
- Animações por cima feitas com o Hyperframes

**Como começar:** No Claude Code, cole: "Set up https://github.com/browser-use/video-use for me." Ele instala e pede a chave da ElevenLabs.

**Nível:** Médio · **Precisa de:** Claude Code, Chave de API paga · **Licença:** MIT · **Estrelas:** 30k · **Último push:** 08/10/2026 · **Situação:** Ativo

> **Atenção:** Transcreve pela ElevenLabs, que é paga e manda o áudio para fora do computador. Evite em gravação com dado sensível.

### auto-editor

`Terminal` · [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor)

Corta sozinho os silêncios e as pausas de um vídeo gravado.

**Para que serve:**
- Limpar a gravação de um tutorial antes de montar o vídeo
- Enxugar gravação de reunião ou demo antes de compartilhar

**Como começar:** No terminal: `pip install auto-editor` e depois `auto-editor gravacao.mp4`.

**Nível:** Médio · **Precisa de:** Terminal · **Licença:** Domínio público · **Estrelas:** 5,8k · **Último push:** 05/11/2026 · **Situação:** Ativo

### Cap

`App` · [CapSoftware/Cap](https://github.com/CapSoftware/Cap)

Gravador de tela aberto, alternativa ao Loom: grava, edita e gera um link para compartilhar.

**Alternativa a:** Loom

**Para que serve:**
- Gravar demo de produto ou tutorial com a sua câmera no canto
- Mandar explicação gravada em vez de marcar reunião

**Como começar:** Baixe o app em cap.so e grave a primeira tela.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** Mista · **Estrelas:** 25k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** Licença mista: parte é MIT, o resto tem termos próprios. Conferir antes de uso comercial.

### DaVinci Resolve MCP

`MCP` · [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)

Deixa o Claude controlar o DaVinci Resolve, um editor profissional: linha do tempo, cortes, cor e exportação.

**Para que serve:**
- Edição de nível profissional comandada por conversa, para vídeo de lançamento
- Ajuste fino depois que o video-use fizer o primeiro corte

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/samuelgursky/davinci-resolve-mcp` Precisa do DaVinci Resolve instalado.

**Nível:** Médio · **Precisa de:** Claude Code, DaVinci Resolve · **Licença:** MIT · **Estrelas:** 4k · **Último push:** 05/11/2026 · **Situação:** Ativo

> **Atenção:** A descrição cita o Resolve Studio, que é a versão paga. Confirmar se funciona na versão grátis antes de instalar.

### Fluxo de edição

`Skill` · [LeiteZ/fluxo-de-edicao](https://github.com/LeiteZ/fluxo-de-edicao)

Skill do Claude Code, em português, que não edita o vídeo: ela entrevista você, analisa vídeos de referência que você gosta e escreve as suas próprias skills de edição, uma por etapa.

**Para que serve:**
- Montar um fluxo de edição no seu estilo: cortes, animação, movimento de câmera e efeito sonoro
- Ganhar uma skill "/editar" que guia cada vídeo novo etapa por etapa
- Aproveitar os cuidados com Hyperframes e com a entrega para o Premiere que vêm nos guias

**Como começar:** No Claude Code, peça: "Instala esta skill para mim: https://github.com/LeiteZ/fluxo-de-edicao". Depois, `/fluxo-de-edicao`.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 53 · **Último push:** 04/11/2026 · **Situação:** Novo

> **Atenção:** Projeto de 4 dias, feito por uma pessoa. É só texto, então dá para ler o SKILL.md antes de instalar e conferir o que ele vai pedir para instalar.

### huashu-motion

`Skill` · [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)

Faz filmes de lançamento de produto com o agente, inclusive a trilha: compõe a música no computador, com instrumentos reais, e coloca efeito sonoro em cada movimento.

**Para que serve:**
- Vídeo de lançamento de 30 segundos a partir do site do produto
- Trilha original sem pagar banco de música
- Apontar para o quadro do vídeo e pedir a mudança ali

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/alchaincyf/huashu-motion`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 2,9k · **Último push:** 16/11/2026 · **Situação:** Ativo

> **Atenção:** Documentação principalmente em chinês.

### Lemo-Opuscar

`Skill` · [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

Caixa de estilos de filme feitos em código: 99 estilos prontos, cada um com um prompt de estilo e um filme de exemplo feito só com código, sem modelo de vídeo.

**Para que serve:**
- Escolher um estilo pronto em vez de começar do zero
- Criar e guardar um estilo seu para usar em todos os vídeos

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/lemomo-ai/lemo-opuscar`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT + CC BY-NC · **Estrelas:** 18k · **Último push:** 17/11/2026 · **Situação:** Ativo

> **Atenção:** Código MIT; os textos dos estilos são CC BY-NC, mas liberados para fazer os próprios filmes, inclusive pagos. Não pode revender os estilos.

### MoviePy

`Biblioteca` · [Zulko/moviepy](https://github.com/Zulko/moviepy)

Biblioteca Python para editar vídeo por script: cortar, juntar, pôr trilha e texto. O Claude escreve o script.

**Para que serve:**
- Mesmo modelo de vídeo aplicado a vários temas, sem editar um por um
- Juntar abertura, gravação e encerramento padrão automaticamente

**Como começar:** No terminal: `pip install moviepy` e peça ao Claude Code um script para cortar e juntar os seus vídeos.

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** MIT · **Estrelas:** 15k · **Último push:** 26/08/2026 · **Situação:** Ativo

### rea-video

`Skill` · [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)

Desmonta qualquer vídeo plano a plano: diz se cada trecho foi filmado, gerado por IA ou feito em código, e como refazer.

**Para que serve:**
- Entender como foi feito um vídeo de referência
- Transformar a análise num roteiro para recriar no seu estilo

**Como começar:** No Claude Code, peça: "Install https://github.com/JuneYaooo/rea-video, then break down this video:" e o caminho do vídeo.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** Apache-2.0 · **Estrelas:** 10,5k · **Último push:** 18/11/2026 · **Situação:** Ativo

### reanimate

`Skill` · [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)

Skill que desmonta uma animação quadro a quadro, recria em código e prova que a cópia se mexe igual.

**Para que serve:**
- Reproduzir uma animação de interface que você viu num site ou app
- Aprender o tempo e a curva de um movimento bem feito

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/NiazMorshed2007/reanimate`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 1,8k · **Último push:** 31/10/2026 · **Situação:** Ativo

> **Atenção:** Usar como estudo, não para copiar o trabalho de alguém sem crédito.

### shorts-kit

`Skill` · [howznguyen/shorts-kit](https://github.com/howznguyen/shorts-kit)

Kit para fazer vídeos verticais narrados (TikTok, Shorts, Reels) com o agente: mais de 20 roteiros prontos, conferência de fatos e efeitos sonoros livres.

**Para que serve:**
- Explicar um conceito em 60 segundos com narração e animação
- Série de vídeos curtos com o mesmo formato

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/howznguyen/shorts-kit`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 190 · **Último push:** 09/11/2026 · **Situação:** Novo

> **Atenção:** Usa o Remotion, que é grátis para pessoa física. Projeto de nov/2026.

### freefield

`App` · [neuregex/freefield](https://github.com/neuregex/freefield)

Versão aberta do Higgsfield em cima do ComfyUI: 120 apps de imagem, vídeo, efeitos e áudio, todos com modelos abertos.

**Alternativa a:** Higgsfield e Runway

**Para que serve:**
- Gerar vídeo a partir de foto, como no Higgsfield, sem assinatura

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/neuregex/freefield` Precisa de GPU própria ou alugada.

**Nível:** Avançado · **Precisa de:** GPU, Docker ou servidor · **Licença:** MIT · **Estrelas:** 1,6k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** Precisa de GPU: alugada por hora (Modal, RunPod) ou própria. Não roda bem no Mac.

### LosslessCut

`App` · [mifi/lossless-cut](https://github.com/mifi/lossless-cut)

Corta trechos de vídeo e áudio sem recodificar, então não perde qualidade e é instantâneo. Edição manual.

**Alternativa a:** Cortes rápidos no Premiere ou no CapCut

**Para que serve:**
- Tirar o começo e o fim de uma gravação de reunião ou demo antes de compartilhar

**Como começar:** Baixe em losslesscut.app, abra o vídeo e marque o trecho que quer manter.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** GPL-2.0 · **Estrelas:** 46k · **Último push:** 03/11/2026 · **Situação:** Ativo

### OpenCut

`App` · [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

Editor de vídeo aberto e gratuito, no estilo do CapCut. A edição é manual, sem o Claude.

**Alternativa a:** CapCut

**Para que serve:**
- Ajuste manual rápido num vídeo que o Claude já montou

**Como começar:** Abra opencut.app no navegador e arraste um vídeo para começar.

**Nível:** Fácil · **Precisa de:** Navegador · **Licença:** MIT · **Estrelas:** 97k · **Último push:** 24/09/2026 · **Situação:** Ativo

### raea

`Terminal` · [shinyobjectz/raea](https://github.com/shinyobjectz/raea)

Motor que renderiza vídeo, motion, 3D e jogos escritos em React e TypeScript, na GPU do computador.

**Para que serve:**
- Cenas 3D e animações pesadas que o Hyperframes não dá conta

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/shinyobjectz/raea` Precisa de placa de vídeo.

**Nível:** Avançado · **Precisa de:** Terminal, GPU · **Licença:** FSL-1.1 · **Estrelas:** 2,8k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** Licença FSL 1.1: uso comum liberado, mas não pode virar produto concorrente; vira Apache depois de 2 anos.

### Remotion

`Biblioteca` · [remotion-dev/remotion](https://github.com/remotion-dev/remotion)

Faz vídeo com código React. Cumpre o mesmo papel do Hyperframes.

**Para que serve:**
- Alternativa ao Hyperframes, caso algum dia ele deixe de atender

**Como começar:** No terminal: `npx create-video@latest` cria um projeto de vídeo em React.

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** Licença própria · **Estrelas:** 71k · **Último push:** 05/11/2026 · **Situação:** Ativo

> **Atenção:** Licença própria: grátis para pessoa física e empresa pequena. Empresa maior precisa de licença paga.

### Remotion Skills

`Skill` · [remotion-dev/skills](https://github.com/remotion-dev/skills)

Skills oficiais do Remotion para o agente criar vídeo em React.

**Para que serve:**
- Criar vídeo em React com o agente, se você usa o Remotion

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/remotion-dev/skills`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** Sem licença · **Estrelas:** 7,5k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** Sem licença declarada no repositório. O Remotion é grátis para pessoa física; empresa maior paga.


## Design, apresentações e imagens

### ComfyUI

`App` · [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)

Gera imagens com IA no próprio computador, montando o processo em blocos ligados.

**Alternativa a:** Midjourney

**Para que serve:**
- Imagens para posts no LinkedIn e capas de apresentação
- Ilustrações para tutoriais e páginas

**Como começar:** Baixe o app para computador em comfy.org e comece por um dos modelos prontos de fluxo.

**Nível:** Avançado · **Precisa de:** Instalar e usar, GPU · **Licença:** GPL-3.0 · **Estrelas:** 145k · **Último push:** 03/11/2026 · **Situação:** Ativo

> **Atenção:** Pede GPU. No Mac roda, mas devagar. Licença GPL.

### Doop

`App` · [kgoedecke/doop](https://github.com/kgoedecke/doop)

Canvas de design em que pessoas e agentes de IA desenham juntos, ao vivo. O Claude Code entra pelo MCP e as telas são HTML de verdade.

**Alternativa a:** Paper.design e Claude Design

**Para que serve:**
- Protótipo de tela feito com o agente, com outras pessoas comentando no mesmo canvas
- Fluxo clicável para validar uma ideia antes de desenvolver
- Guardar as regras de estilo de um design system para todo agente seguir

**Como começar:** `git clone https://github.com/kgoedecke/doop`, depois `docker compose up -d` na pasta e abra http://localhost:4400.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** AGPL-3.0 · **Estrelas:** 1,7k · **Último push:** 04/11/2026 · **Situação:** Ativo

> **Atenção:** Projeto novo (ago/2026) e AGPL. Faz quase o mesmo que o Design do Claude: vale se você precisa de um canvas hospedado por você ou de um agente que não seja o Claude.

### FigCraft

`App` · [storytold/figcraft](https://github.com/storytold/figcraft)

Editor de design no estilo do Figma, aberto e nativo: componentes, auto layout, variáveis, protótipo e modo dev. Abre arquivos .fig, e o agente controla tudo por MCP, com mais de 400 comandos.

**Alternativa a:** Figma

**Para que serve:**
- Abrir um arquivo do Figma no computador, sem nuvem, e pedir para o agente mexer
- Montar um design system com componentes e variáveis pelo Claude
- Exportar tela em PNG, SVG, PDF ou código React

**Como começar:** Baixe o instalador para o seu sistema na página de Releases do repositório.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** Apache-2.0 · **Estrelas:** 4,7k · **Último push:** 07/11/2026 · **Situação:** Alpha

> **Atenção:** Em alpha: o próprio projeto diz que está a cerca de 49% de substituir o Figma. Abre .fig "no melhor esforço" e a colaboração ao vivo ainda é prévia.

### frontend-slides

`Skill` · [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)

Skill que faz apresentações bonitas na web, usando o que o agente sabe de front-end.

**Para que serve:**
- Apresentação em HTML com animação, sem PowerPoint
- Deck rápido a partir de um texto ou de um roteiro

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/zarazhangrui/frontend-slides`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 32k · **Último push:** 23/06/2026 · **Situação:** Ativo

> **Atenção:** Comparar com os Slides do Claude antes de adotar.

### Penpot

`App` · [penpot/penpot](https://github.com/penpot/penpot)

Plataforma de design aberta e madura, alternativa ao Figma: roda no navegador ou no seu servidor, trabalha com SVG, CSS e HTML e tem servidor MCP para o agente.

**Alternativa a:** Figma

**Para que serve:**
- Design de telas com colaboração, hospedado por você
- Ligar design e código pelo MCP, com tokens de design
- Alternativa mais madura ao FigCraft quando você precisa de um Figma aberto

**Como começar:** Crie uma conta grátis em penpot.app. Para hospedar, siga o guia de self-host com Docker.

**Nível:** Avançado · **Precisa de:** Navegador, Docker ou servidor · **Licença:** MPL-2.0 · **Estrelas:** 63k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** Projeto de 10 anos, bem mais estável que o FigCraft. Ainda assim é design vetorial, não HTML como o Doop.

### Presenton

`App` · [presenton/presenton](https://github.com/presenton/presenton)

Gera apresentações com IA a partir de um tema ou documento, com API. Alternativa aberta ao Gamma.

**Alternativa a:** Gamma, Canva e Beautiful.ai

**Para que serve:**
- Primeiro rascunho de apresentação em minutos
- Deck gerado por API a partir de dados, como um relatório semanal
- Comparar antes com os Slides que o Claude já faz

**Como começar:** Teste em presenton.ai ou hospede com Docker seguindo o README.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** Apache-2.0 · **Estrelas:** 12k · **Último push:** 02/11/2026 · **Situação:** Ativo

### Fooocus

`App` · [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)

Gera imagens com IA de um jeito simples: escreve o pedido e pronto.

**Alternativa a:** Midjourney

**Para que serve:**
- Mesmo uso do ComfyUI, para quem quer só digitar e gerar

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/lllyasviel/Fooocus` Precisa de placa de vídeo forte.

**Nível:** Avançado · **Precisa de:** Terminal, GPU · **Licença:** GPL-3.0 · **Estrelas:** 54k · **Último push:** 01/12/2025 · **Situação:** Parado

> **Atenção:** Sem atualização desde dez/2025. Preferir o ComfyUI.

### sand3d

`Biblioteca` · [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d)

Modelagem 3D em Python feita para o agente usar.

**Para que serve:**
- Peça 3D simples (ícone, objeto) gerada por descrição

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/Sandflow-ai/sand3d`

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** Apache-2.0 · **Estrelas:** 2,1k · **Último push:** 18/11/2026 · **Situação:** Novo

> **Atenção:** Projeto de nov/2026.

### Screenshot to Code

`App` · [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)

Transforma um print, ou uma gravação de tela, em código pronto: HTML com Tailwind, React, Vue ou Bootstrap.

**Alternativa a:** v0 e Lovable (a partir de um print)

**Para que serve:**
- Print de uma tela vira protótipo editável para propor melhoria
- Gravação do fluxo de outro app vira protótipo clicável para comparar

**Como começar:** Teste em screenshottocode.com com um print sem dado sensível. Para rodar local, precisa de chave de API.

**Nível:** Médio · **Precisa de:** Terminal, Chave de API paga · **Licença:** MIT · **Estrelas:** 81k · **Último push:** 05/11/2026 · **Situação:** Ativo

> **Atenção:** Precisa de chave de API paga (Anthropic, OpenAI ou Gemini), não usa a assinatura do Claude. O Claude Code já transforma print em HTML, inclusive direto no Doop. A versão de nuvem não deve receber tela com dado sensível.


## Deixar o design feito com IA mais bonito

### Emil Kowalski Skills

`Skill` · comece por esta · [emilkowalski/skills](https://github.com/emilkowalski/skills)

19 skills de design engineering do Emil Kowalski (ex-Vercel e Linear) para animação e acabamento de interface: escolhem a curva e a duração certas, revisam animações, coordenam o que se mexe junto e testam a tela com dados extremos.

**Para que serve:**
- Dar animações com acabamento profissional a um site genérico
- Revisar e cortar animação demais, que deixa a página com cara de IA
- Testar a tela com nomes longos, listas vazias e números enormes antes de publicar

**Como começar:** No terminal: `npx skills@latest add emilkowalski/skills`. Não sabe qual usar? Peça a skill `ask-emil`, que indica a certa para o seu caso.

**Nível:** Médio · **Precisa de:** Claude Code, Terminal · **Licença:** MIT · **Estrelas:** 60k · **Último push:** 15/11/2026 · **Situação:** Ativo

> **Atenção:** O foco é animação e detalhe de interface. Para revisar o visual geral, combina com o Impeccable ou a Taste Skill.

### Impeccable

`Skill` · comece por esta · [pbakaus/impeccable](https://impeccable.style)

Vocabulário de design para o agente: comandos para revisar (critique, audit), dar acabamento (polish, bolder, quieter) e um detector com 62 regras que pega a cara de IA antes de publicar.

**Para que serve:**
- Achar a cara de IA numa página pronta: Inter em tudo, degradê roxo, card dentro de card, contraste ruim
- Pedir ao agente uma crítica de UX ou uma passada final de acabamento com um comando só
- Rodar "npx impeccable detect" numa pasta ou num endereço, sem instalar nada

**Como começar:** Teste sem instalar: `npx impeccable detect .` na pasta do seu site. Para instalar: `npx impeccable install`.

**Nível:** Médio · **Precisa de:** Claude Code, Terminal · **Licença:** Apache-2.0 · **Estrelas:** 117k · **Último push:** 25/11/2026 · **Situação:** Ativo

> **Atenção:** Ao instalar, cria um hook que verifica toda edição de interface e baixa um programa próprio. Tem telemetria anônima, que desliga com "npx impeccable telemetry off". Mesmo espaço da Taste Skill, da Hallmark e do Unslop.

### Hallmark

`Skill` · [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

Skill contra o "design com cara de IA" para o Claude Code, com regras de layout, tipografia e cor.

**Para que serve:**
- Dar acabamento de designer a páginas e telas feitas pelo agente

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/Nutlope/hallmark`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 57k · **Último push:** 11/11/2026 · **Situação:** Ativo

> **Atenção:** Mesmo espaço da Taste Skill, do Unslop e do Impeccable. Escolher um só depois de testar na mesma página.

### Logo Design Skill

`Skill` · [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)

Skill completa de design de logo: princípios, processo, desenho em SVG, ferramentas de teste e uma biblioteca de mais de 1.400 logos de referência.

**Para que serve:**
- Criar logo em vetor (SVG) para um projeto novo
- Testar o logo em tamanho pequeno, em preto e branco e em fundo escuro

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/kaankiziltug/logo-design-skill`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 7,2k · **Último push:** 13/11/2026 · **Situação:** Ativo

### Photo Flipbook

`Skill` · [HaichaoLihc/create-photo-flipbook-ui](https://github.com/HaichaoLihc/create-photo-flipbook-ui)

Skill que transforma uma pasta de fotos num livro de fotos 3D interativo, com páginas que viram, entregue como site.

**Para que serve:**
- Álbum de viagem, casamento ou aniversário como site para presentear
- Base para um serviço de fotolivro digital
- Templates extras de galeria: anel de fotos, estante e atlas por ano

**Como começar:** No Codex, instale pelo instalador de skills com o comando do README e peça para transformar uma pasta de fotos em livro.

**Nível:** Médio · **Precisa de:** Codex, Chave de API paga · **Licença:** MIT · **Estrelas:** 657 · **Último push:** 20/10/2026 · **Situação:** Ativo

> **Atenção:** Feita para o Codex: gera a arte das páginas com o gerador de imagens da OpenAI. No Claude Code essa parte precisa de outro caminho; o livro 3D funciona igual.

### scroll-craft

`Skill` · [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)

Skill para sites imersivos que contam a história pela rolagem, com padrão de design e checagem de contraste e de celular.

**Para que serve:**
- Landing page de lançamento ou portfólio que prende quem rola
- Estudar os dez sites aprovados que vêm como exemplo

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/nateherkai/scroll-craft`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 4,7k · **Último push:** 30/09/2026 · **Situação:** Ativo

### Taste Skill

`Skill` · [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

Faz o papel de diretor de arte do agente: define uma direção visual, busca fotos reais em acervos abertos e confere o resultado em screenshot no navegador.

**Para que serve:**
- Landing page, post do LinkedIn e página com cara menos "feita por IA"
- Revisão visual por screenshot antes de entregar um artefato

**Como começar:** No Claude Code: `/plugin marketplace add Leonxlnx/taste-skill` e `/plugin install taste-skill@taste-skill`.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 110k · **Último push:** 04/11/2026 · **Situação:** Ativo

> **Atenção:** Ocupa o mesmo espaço do Hallmark, do Unslop e do Impeccable. Teste na mesma página antes de escolher um.

### UI Skills

`Skill` · [ibelick/ui-skills](https://github.com/ibelick/ui-skills)

Catálogo de skills para quem faz interface (motion, tipografia, layout), com buscador pelo terminal e por MCP.

**Para que serve:**
- Achar uma skill pronta para um problema de interface específico
- Ler o playbook, que resume as lições das melhores skills de design

**Como começar:** No terminal: `npx ui-skills start` para navegar pelas skills e pegar a que precisa.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 10,8k · **Último push:** 07/11/2026 · **Situação:** Ativo

> **Atenção:** O MCP aponta para o site deles (ui-skills.com), que é um serviço de terceiro.

### UI UX Pro Max

`Skill` · [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

Catálogo de design com buscador, que o agente consulta enquanto desenha: estilos, paletas, fontes, regras de UX e um checklist de entrega.

**Para que serve:**
- Checklist de UX e acessibilidade antes de entregar uma tela ou protótipo
- Regras de texto que quebra e rótulo curto, problema comum em formulário
- Cobre 22 stacks, de React e Angular a SwiftUI e Flutter

**Como começar:** No Claude Code: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` e `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 145k · **Último push:** 04/11/2026 · **Situação:** Ativo

> **Atenção:** Quando o projeto já tem um padrão visual, usar só as regras de UX dele, não a paleta e as fontes.

### Unslop

`Skill` · [heydamir/unslop](https://github.com/heydamir/unslop)

Skill que transforma uma interface com cara de feita por IA numa interface desenhada.

**Para que serve:**
- Revisar uma tela pronta e tirar os vícios visuais de IA

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/heydamir/unslop`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** CC-BY-4.0 · **Estrelas:** 18k · **Último push:** 15/11/2026 · **Situação:** Ativo

> **Atenção:** Licença CC BY 4.0: pode usar, mas precisa dar crédito. Mesmo espaço do Hallmark e da Taste Skill.


## Organizar o dia a dia

### anarlog

`App` · comece por esta · [fastrepl/anarlog](https://github.com/fastrepl/anarlog)

Anotador de reuniões no estilo do Granola, que roda no computador: escuta o áudio do Mac, transcreve localmente e monta as notas, sem bot entrando na chamada.

**Alternativa a:** Granola e Otter

**Para que serve:**
- Notas e resumo de reunião sem mandar a conversa para a nuvem
- Ata pronta logo depois da chamada

**Como começar:** Baixe o app em anarlog.so e dê permissão de microfone e áudio do sistema.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** MIT · **Estrelas:** 9,9k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** A equipe agora toca um produto pago (char.com); o anarlog segue aberto e mantido, mas vale acompanhar.

### Postiz

`App` · comece por esta · [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app)

Agenda e publica posts em várias redes (Instagram, LinkedIn, TikTok, YouTube e outras), com um agente de IA que ajuda a criar e programar.

**Alternativa a:** Buffer, Hootsuite e mLabs

**Para que serve:**
- Programar a semana inteira de posts de uma vez
- Pedir ao Claude para agendar as peças prontas nos dias certos
- Ver num calendário só o que sai em cada rede

**Como começar:** Teste na nuvem em postiz.com ou hospede com Docker seguindo o README.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** AGPL-3.0 · **Estrelas:** 42k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** AGPL. Tem versão de nuvem paga; a versão que você mesmo hospeda é grátis.

### Yogurt

`App` · comece por esta · [FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)

Anotações de reunião que ficam no computador: grava o microfone e o áudio da chamada, transcreve, resume e responde perguntas sobre as reuniões, sem bot entrando na chamada.

**Alternativa a:** Granola, Otter e Fireflies

**Para que serve:**
- Ata e resumo de reunião do Zoom, Teams ou Meet sem nuvem
- Perguntar "o que ficou combinado sobre X?" e receber a resposta com o trecho da reunião
- Exportar notas e transcrição em Markdown

**Como começar:** Baixe em yogurt.so ou, no Mac: `brew install --cask frigadehq/yogurt/yogurt`.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** MIT · **Estrelas:** 3,4k · **Último push:** 25/11/2026 · **Situação:** Novo

> **Atenção:** Tem instalador para Mac e é mais simples de começar que o anarlog, que faz o mesmo. Projeto de nov/2026. Avisar quem está na chamada que ela está sendo gravada.

### AI File Sorter

`App` · [hyperfield/ai-file-sorter](https://github.com/hyperfield/ai-file-sorter)

Organiza pastas bagunçadas com IA: sugere uma categoria e um nome melhor para cada arquivo (fotos, documentos, áudio e vídeo) e só mexe depois que você aprova.

**Alternativa a:** Hazel (Mac)

**Para que serve:**
- Arrumar a pasta de Downloads e o HD externo de uma vez
- Renomear fotos como IMG_2048.jpg para nomes que dizem o que tem nelas

**Como começar:** Baixe o app em filesorter.app, aponte para a pasta de Downloads e revise as sugestões antes de aplicar.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** AGPL-3.0 · **Estrelas:** 1,9k · **Último push:** 21/11/2026 · **Situação:** Ativo

> **Atenção:** Roda com modelo local, sem mandar nada para fora. Se você ligar o nome do lugar nas fotos, as coordenadas vão para o OpenStreetMap.

### claude-hud

`Plugin` · [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)

Plugin do Claude Code que mostra o que está acontecendo: uso de contexto, ferramentas ativas, agentes rodando e progresso das tarefas.

**Para que serve:**
- Ver quanto do contexto já foi usado antes de a conversa ficar longa
- Acompanhar subagentes e tarefas em andamento

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/jarrodwatts/claude-hud`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 29k · **Último push:** 10/11/2026 · **Situação:** Ativo

### airhand

`App` · [sqlpxc/airhand](https://github.com/sqlpxc/airhand)

Acesso remoto ao computador com baixa latência, até 120 quadros por segundo, em Windows, Mac, Linux, Android e navegador.

**Alternativa a:** TeamViewer, AnyDesk e Parsec

**Para que serve:**
- Usar o Mac de outro lugar com fluidez

**Como começar:** Baixe o app para os dois computadores na página de Releases do repositório.

**Nível:** Fácil · **Precisa de:** Instalar e usar · **Licença:** MIT · **Estrelas:** 1,4k · **Último push:** 18/11/2026 · **Situação:** Novo

> **Atenção:** Projeto de out/2026. Acesso remoto exige cuidado com segurança.

### Plane

`App` · [makeplane/plane](https://github.com/makeplane/plane)

Gestão de projetos aberta, alternativa ao Jira, Linear e ClickUp: tarefas, sprints, documentos e triagem.

**Alternativa a:** Jira, Linear, Monday e ClickUp

**Para que serve:**
- Organizar um projeto pessoal com quadro, ciclos e documentos
- Hospedar para um time pequeno sem pagar por usuário

**Como começar:** Teste na nuvem em plane.so ou hospede com Docker seguindo o README.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** AGPL-3.0 · **Estrelas:** 63k · **Último push:** 17/11/2026 · **Situação:** Ativo

> **Atenção:** AGPL. Para projeto pessoal, um quadro simples pode bastar.

### Windrecorder

`App` · [yuka-friends/Windrecorder](https://github.com/yuka-friends/Windrecorder)

Grava tudo o que passa na tela, em arquivo pequeno, e deixa buscar depois pelo texto que apareceu ou pela descrição da imagem.

**Alternativa a:** Windows Recall e Rewind

**Para que serve:**
- Achar aquela tela que você viu na semana passada e não salvou

**Como começar:** Só no Windows: siga a instalação do README (precisa do ffmpeg).

**Nível:** Fácil · **Precisa de:** Instalar e usar, Só Windows · **Licença:** GPL-2.0 · **Estrelas:** 4k · **Último push:** 25/09/2026 · **Situação:** Só Windows

> **Atenção:** Só funciona no Windows. E guarda tudo o que aparece na tela, inclusive senha e dado sensível.


## Finanças, viagem e currículo

### Reactive Resume

`App` · [reactive-resume/reactive-resume](https://github.com/reactive-resume/reactive-resume)

Criador de currículo aberto e gratuito: você escreve e vê a página pronta ao lado, baixa em PDF, Word ou Markdown, ou compartilha por link.

**Alternativa a:** Canva e Zety (currículo)

**Para que serve:**
- Manter o currículo atualizado num modelo bonito, sem pagar assinatura
- Gerar versões do currículo para vagas diferentes

**Como começar:** Crie uma conta grátis em rxresu.me e importe o currículo que você já tem.

**Nível:** Fácil · **Precisa de:** Navegador · **Licença:** MIT · **Estrelas:** 46k · **Último push:** 20/11/2026 · **Situação:** Ativo

> **Atenção:** Grátis no site deles ou hospedado por você. A IA é opcional e usa um provedor que você conecta.

### Sure

`App` · [we-promise/sure](https://github.com/we-promise/sure)

App de finanças pessoais que você mesmo hospeda: contas, gastos, orçamento e patrimônio num lugar só. É a continuação, feita pela comunidade, do Maybe Finance.

**Alternativa a:** Mobills, Organizze e YNAB

**Para que serve:**
- Controlar gastos e patrimônio sem entregar os dados a um app de terceiro
- Consultar as suas finanças por um agente de IA, que tem acesso próprio ao app

**Como começar:** Hospede com Docker seguindo o guia de hosting do repositório (docs/hosting/docker.md).

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** AGPL-3.0 · **Estrelas:** 17,9k · **Último push:** 25/11/2026 · **Situação:** Ativo

> **Atenção:** AGPL. A conexão automática com banco foi pensada para fora do Brasil: confira como importar extrato de banco brasileiro antes de adotar.

### TaxHacker

`App` · [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker)

Contabilidade com IA que você mesmo hospeda: tira foto do recibo ou sobe a nota em PDF, e ele extrai valor, data, loja, itens e impostos e lança como despesa ou receita.

**Alternativa a:** Expensify

**Para que serve:**
- Controlar as despesas de um projeto pessoal ou de PJ sem digitar nota por nota
- Separar os gastos por projeto e categoria e exportar para o contador

**Como começar:** Teste em taxhacker.app ou hospede com Docker seguindo o README.

**Nível:** Avançado · **Precisa de:** Docker ou servidor, Chave de API paga · **Licença:** MIT · **Estrelas:** 6,9k · **Último push:** 20/11/2026 · **Situação:** Ativo

> **Atenção:** Ainda em desenvolvimento inicial, nas palavras do autor. Usa OpenAI, Gemini ou Mistral, que são pagos, ou um modelo local.

### TREK

`App` · [liketrek/TREK](https://github.com/liketrek/TREK)

Planejador de viagem completo, hospedado por você: roteiro no mapa editado em tempo real por quem vai junto, reservas, custos divididos, lista de mala e diário da viagem.

**Alternativa a:** Wanderlog e TripIt

**Para que serve:**
- Montar uma viagem em família ou com amigos, todo mundo editando junto
- Dividir os gastos e guardar as reservas num lugar só

**Como começar:** Teste a demonstração em demo.liketrek.com e, se gostar, hospede com Docker seguindo o README.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** AGPL-3.0 · **Estrelas:** 15,9k · **Último push:** 25/11/2026 · **Situação:** Ativo

> **Atenção:** AGPL. Tem servidor MCP, então o Claude pode montar o roteiro dentro do app.


## Agentes e automação

### gstack

`Skill` · [garrytan/gstack](https://github.com/garrytan/gstack)

O setup do Claude Code do Garry Tan: 23 ferramentas que fazem papel de CEO, designer, gerente de engenharia, release, documentação e QA.

**Para que serve:**
- Estudar como ele organiza papéis e revisões com o agente
- Pegar uma ou outra skill (revisão, QA) para o seu fluxo

**Como começar:** Leia o README antes. A instalação (`git clone` em ~/.claude/skills e `./setup`) mexe no seu CLAUDE.md.

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 142k · **Último push:** 18/11/2026 · **Situação:** Ativo

> **Atenção:** A instalação manda mexer no CLAUDE.md e proibir as ferramentas do Chrome. Leia antes e não instale inteiro se você já tem um setup próprio.

### LobeHub

`App` · [lobehub/lobehub](https://github.com/lobehub/lobehub)

Plataforma de chat e agentes com vários modelos de IA, que você mesmo hospeda.

**Alternativa a:** ChatGPT e Claude no navegador

**Para que serve:**
- Um chat de agentes prontos e compartilhados para um time
- Base de conhecimento consultável por quem não usa Claude Code

**Como começar:** Teste em lobehub.com ou hospede com Docker seguindo o README. Você conecta a chave do modelo.

**Nível:** Avançado · **Precisa de:** Docker ou servidor, Chave de API paga · **Licença:** Licença própria · **Estrelas:** 84k · **Último push:** 03/11/2026 · **Situação:** Ativo

> **Atenção:** Licença própria: confirmar as condições antes de qualquer uso comercial.

### Flowise

`App` · [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)

Monta agentes e fluxos de IA arrastando blocos, sem programar.

**Alternativa a:** n8n e Make (fluxos com IA)

**Para que serve:**
- Protótipo de ideia para mostrar: triagem automática de chamados, chatbot de suporte

**Como começar:** Com o Node instalado: `npx flowise start` e abra http://localhost:3000.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** Licença própria · **Estrelas:** 56k · **Último push:** 13/08/2026 · **Situação:** Arquivado

> **Atenção:** Repositório arquivado: sem manutenção. Só para protótipo, nunca em produção.

### Laya

`Biblioteca` · [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)

Motor de decisão rápido para desenvolvedor: classifica um texto, dá nota ou responde sim ou não em mais de 100 línguas, em milissegundos, sem chamar um modelo grande.

**Para que serve:**
- Triagem automática de mensagens ou chamados (urgente, reclamação, cancelamento) a custo quase zero
- Filtro barato antes de mandar algo para um agente mais caro

**Como começar:** No terminal: `pip install laya` e siga o Quickstart do README.

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** Apache-2.0 · **Estrelas:** 35k · **Último push:** 08/11/2026 · **Situação:** Ativo

> **Atenção:** Ferramenta de programador, em Python. Projeto de set/2026.

### MetaGPT

`Biblioteca` · [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)

Monta uma "empresa de software" feita de agentes: a partir de um requisito de uma linha, papéis de PM, arquiteto e engenheiro geram histórias, análise competitiva, PRD, APIs e código.

**Para que serve:**
- Referência de como dividir papéis e passos entre agentes
- Rascunho de PRD a partir de uma ideia

**Como começar:** Para estudar: leia o README e os exemplos. Para rodar: `pip install --upgrade metagpt` (Python abaixo do 3.12).

**Nível:** Avançado · **Precisa de:** Programar, Chave de API paga · **Licença:** MIT · **Estrelas:** 71k · **Último push:** 21/01/2026 · **Situação:** Parado

> **Atenção:** Sem atualização desde jan/2026, pede Python abaixo do 3.12 e chave de API paga. Ler as ideias, não instalar.

### OpenHands

`App` · [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)

Agente que escreve e roda código sozinho, num ambiente isolado.

**Alternativa a:** Devin

**Para que serve:**
- Protótipo de tela ou script feito do zero, num ambiente separado
- Vale se você quer um agente hospedado por você ou com outro modelo; quem já usa o Claude Code tem quase tudo isso

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/OpenHands/OpenHands` Roda em Docker e pede a chave do modelo que você usa.

**Nível:** Avançado · **Precisa de:** Docker ou servidor, Chave de API paga · **Licença:** MIT · **Estrelas:** 93k · **Último push:** 03/11/2026 · **Situação:** Ativo


## Cursos, área de membros e comunidade

### Icarus

`App` · [tiberiolemes/icarus-area-de-membros](https://github.com/tiberiolemes/icarus-area-de-membros)

Plataforma de código aberto para montar a sua área de membros e vender cursos online: aulas em texto, vídeo e áudio, certificados, suporte por chamados e comunidade com moderação manual.

**Alternativa a:** Hotmart Club, Kiwify e Memberkit

**Para que serve:**
- Vender e entregar um curso sem pagar mensalidade de plataforma
- Comunidade de alunos com aprovação manual de cada publicação
- Certificado com verificação pública por código

**Como começar:** Teste a demonstração pública, com acesso de aluno e de administrador: `https://tiberiolemes.github.io/icarus-area-de-membros/`. Para instalar: `npm ci`, `npm run local:start` e `npm run dev`.

**Nível:** Avançado · **Precisa de:** Docker ou servidor · **Licença:** MIT · **Estrelas:** 1 · **Último push:** 25/11/2026 · **Situação:** Novo

> **Atenção:** Projeto novo (nov/2026). Para vender de verdade, precisa configurar Supabase, e-mail, Asaas e Bunny; a cobrança fica bloqueada até essa homologação.


## Construir apps e interfaces

### BAMA

`Skill` · [daveebbelaar/bama](https://github.com/daveebbelaar/bama)

Skills para o agente pesquisar, desenhar, construir e testar apps nativos de Mac em Swift e SwiftUI.

**Para que serve:**
- Criar um app de Mac pequeno para uma tarefa sua

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/daveebbelaar/bama`

**Nível:** Médio · **Precisa de:** Claude Code · **Licença:** MIT · **Estrelas:** 1,9k · **Último push:** 05/11/2026 · **Situação:** Ativo

### BoardUI

`Componentes` · [BoardUI/boardui](https://github.com/BoardUI/boardui)

Biblioteca de componentes React para produtos com IA: chat, indicador de "pensando", log de agente, tabelas e formulários, com tema claro e escuro.

**Para que serve:**
- Base visual para um app próprio com chat de IA

**Como começar:** Num projeto React: `npx boardui add` e o nome do componente que quer copiar.

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** MIT · **Estrelas:** 1,1k · **Último push:** 02/10/2026 · **Situação:** Ativo

> **Atenção:** Só vale se você for construir um produto em React. Esta é a parte grátis; o resto é pago.

### Exact

`Biblioteca` · [expo/exact](https://github.com/expo/exact)

Da Expo: escreve o app uma vez e ele roda nativo na web, no Mac, no iPhone e no Linux, e o agente consegue construir, rodar, ver e testar em todos.

**Para que serve:**
- Protótipo de app que funciona no celular e no computador

**Como começar:** Sem instrução específica. Passe o link para a sua IA (Claude Code, Codex…) e peça para ela instalar: `https://github.com/expo/exact`

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** MIT · **Estrelas:** 4,6k · **Último push:** 18/11/2026 · **Situação:** Novo

> **Atenção:** Projeto de nov/2026, da mesma equipe do Expo.

### ThreeUI

`Componentes` · [MengTo/threeui](https://github.com/MengTo/threeui)

Catálogo de componentes 3D e interativos para sites, com o código pronto para copiar.

**Para que serve:**
- Efeito 3D pontual numa landing page

**Como começar:** Abra threeui.com, escolha o componente e copie o código para o seu site.

**Nível:** Avançado · **Precisa de:** Programar · **Licença:** MIT · **Estrelas:** 7,2k · **Último push:** 03/09/2026 · **Situação:** Ativo

> **Atenção:** Edição aberta de um produto pago: os componentes Pro ficam de fora.

### Web Artifacts Builder

`Skill` · [anthropics/skills · web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)

Skill oficial da Anthropic para artifacts grandes do claude.ai: monta um projeto em React, TypeScript, Tailwind e shadcn/ui, e no fim empacota tudo num único arquivo HTML.

**Para que serve:**
- Ferramenta interativa com várias telas, estado e navegação, publicada como artifact
- Painel ou app pequeno que precisa de componentes prontos (tabelas, formulários, diálogos)

**Como começar:** Sem instrução específica. Passe o link para a sua IA e peça para ela instalar a skill: `https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder`. Rode numa pasta separada.

**Nível:** Médio · **Precisa de:** Claude Code, Terminal · **Licença:** Apache-2.0 · **Estrelas:** 200k · **Último push:** 20/04/2026 · **Situação:** Oficial

> **Atenção:** Para página de leitura, como esta prateleira, HTML simples resolve e carrega mais rápido. A instalação baixa muita coisa (pnpm global, Vite, 40+ componentes): rodar numa pasta separada.


## Os tipos

- **App:** Programa com tela própria. Roda no computador, no navegador ou num servidor seu.
- **Skill:** Instruções que ensinam o Claude Code (ou outro agente) a fazer um trabalho. Instala com um comando e vira um /comando.
- **Terminal:** Ferramenta sem tela, usada por comando. Dá para pedir ao Claude Code rodar por você.
- **Biblioteca:** Código para usar dentro de um projeto de programação.
- **Modelo:** Modelo de IA que roda no seu computador, sem serviço externo.
- **MCP:** Ponte que deixa o Claude controlar outro programa.
- **Componentes:** Peças de interface prontas para copiar num site ou app.
- **Plugin:** Extensão que muda o próprio Claude Code.
- **Dados:** Base de informação para consultar.

## Antes de instalar qualquer uma

- Dado sensível, seu ou de cliente, não vai para versão de nuvem de terceiro. Várias destas ferramentas têm versão cloud; use a que roda na sua máquina.
- GPL e AGPL podem ser usadas por conta própria. Colocar dentro de um produto vendido exige cuidado com a licença.
- Projeto de terceiro que você ainda está avaliando roda melhor em Docker, isolado do resto da máquina.
- Skill é texto: leia o arquivo antes de instalar e veja o que ela manda o agente fazer.
- Confira de novo a licença e a atividade do repositório no dia da instalação.

## Sugira uma ferramenta

Conhece uma ferramenta de IA de código aberto que resolve um problema real? [Abra uma sugestão](https://github.com/dlotuz/prateleira-de-repos/issues/new?template=sugerir-ferramenta.yml) ou mande um pull request seguindo o [guia de contribuição](CONTRIBUTING.md). Toda sugestão passa por revisão antes de entrar.

## Licença

O conteúdo desta lista está sob [CC BY 4.0](LICENSE): pode copiar e adaptar, dando o crédito. Cada ferramenta tem a sua própria licença, indicada no item.

Estrelas e data do último push conferidos no GitHub. Lista gerada em 25/11/2026.
