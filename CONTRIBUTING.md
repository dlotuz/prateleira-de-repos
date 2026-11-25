# Como sugerir um repositório

A Prateleira de Repositórios junta ferramentas de IA de código aberto que resolvem um problema real. Toda sugestão passa por revisão antes de entrar.

## Jeito mais fácil: abrir uma sugestão

Use o formulário [Sugerir ferramenta](https://github.com/dlotuz/prateleira-de-repos/issues/new?template=sugerir-ferramenta.yml). Basta o link do repositório e uma frase sobre o que ele resolve para você.

## Para quem prefere mandar pull request

1. Edite `data/ferramentas.json` e acrescente um item no mesmo formato dos outros.
2. Rode `python3 scripts/gerar.py` para atualizar o `README.md` e o site (`docs/index.html`).
3. Abra o pull request com os três arquivos.

### Campos de cada item

| Campo | O que vai |
|---|---|
| `nome`, `repo`, `url` | Nome da ferramenta, `dono/repositorio` e link |
| `tipo` | `app`, `skill`, `terminal`, `lib`, `modelo`, `mcp`, `comp`, `plugin` ou `dados` |
| `categoria` | `doc`, `audio`, `video`, `visual`, `skill`, `prod`, `vida`, `agent`, `cursos` ou `apps` |
| `destaque` | `alta`, `media` ou `baixa` (quem revisa pode mudar) |
| `o_que_faz` | Uma ou duas frases, sem jargão |
| `para_que_serve` | Lista com 1 a 3 usos concretos |
| `alternativa_a` | O produto conhecido que ela substitui, ou `null` |
| `precisa` | Lista com o que é preciso para usar (veja os valores no README) |
| `atencao` | Licença, custo escondido, projeto parado ou outro alerta, ou `null` |
| `primeiro_passo` | Uma linha de como começar. Comando entre crases. Sem instrução oficial: "Sem instrução específica. Passe o link para a sua IA…" |
| `testado` | `true` só quando o PW instalou e usou (quem revisa marca; em sugestão, deixe `false`) |
| `imagem` | Endereço da imagem do repositório (campo `openGraphImageUrl` da API do GitHub) ou `null` |
| `licenca`, `estrelas`, `ultimo_push`, `situacao` | Como aparecem no GitHub |

## O que entra

- Código aberto e com licença declarada.
- Projeto ativo ou, se parado, ainda útil (com o alerta no item).
- Explicação em português claro, pensando em quem não programa.

## O que não entra

- Produto fechado ou só com versão paga.
- Repositório sem README ou que pede credencial sem explicar o porquê.
- Texto de divulgação. A descrição diz o que a ferramenta faz e onde ela falha.
