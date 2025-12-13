# Generative AI Agent Example

Minimal **AI Agent** example using **Ollama** locally to fetch Hogwarts spells from a dedicated API.  
Educational project for Python developers wanting to build generative agents with minimal dependencies (only ollama, python-dotenv, requests).

## Key Features

- **ReAct Agent with Ollama**: uses qwen3:latest and nomic-embed-text:latest for reasoning and tool calling.
- **Two specific tools**: get_spell_info() for exact spells, search_spells() for searches.
- **Zero external dependencies**: only ollama==0.6.1, python-dotenv==1.2.1, requests.
- **Works offline**: local Ollama models, Hogwarts API requires internet only for queries.
- **Robust error handling**: fallback for failed APIs or spells not found.
- **Verbose tracing**: shows agent's reasoning and tool calls process.

## Prerequisites

- **Python 3.10+**
- **Ollama** installed and running (`ollama serve`)
- Ollama models: `ollama pull qwen3:latest` and `ollama pull nomic-embed-text:latest`
- `.env` file with `HOGWARTS_API_HOST=https://potterapi-fedeperin.vercel.app`

```bash
ollama pull qwen3:latest
ollama pull nomic-embed-text:latest
```

## Installation

```bash
git clone https://github.com/carmelolg/generative-ai-agent-example.git
cd generative-ai-agent-example
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create the `.env` file with the variables listed in prerequisites.

## Configuration

Edit `.env` to customize:

```
EMBEDDING_MODEL=nomic-embed-text:latest
LANGUAGE_MODEL=qwen3:latest
HOGWARTS_API_HOST=https://potterapi-fedeperin.vercel.app
```

Start Ollama in background: `ollama serve`.

## Running the Agent

Start the interactive agent:

```bash
python agent.py
```

Or run a direct prompt:

```bash
python agent.py "What does Expecto Patronum do?"
```

The agent will reason step-by-step, call necessary tools, and return the response.

## Usage Examples

**Specific spell query**:

```
Input: "Describe Wingardium Leviosa"
Output: Agent calls get_spell_info, fetches "Levitation charm" and description from API.
```

**Exploratory search**:

```
Input: "What spells are used for flying?"
Output: Uses search_spells, lists relevant results with reasoning on flight.
```

Hogwarts API: https://potterapi-fedeperin.vercel.app 

## Project Architecture

```
├── lib                         # Folder for reusable modules 
│   ├── HttpService.py          # HTTP calls to Hogwarts API
│   ├── KnowledgeService.py     # Spell search and retrieval tools
│   ├── MathUils.py             # Math helper functions (if needed)
│   ├── OllamaUtils.py          # Ollama model interaction helpers
│   └── SpellFunctions.py       # Spell-specific tool implementations
├── .env                        # Environment variables
├── hogwards-agent.py           # the main agent logic
└── requirements.txt            # Minimal dependencies
```

- **OllamaLLM + Embeddings**: local models for reasoning and context.
- **Custom tools**: pure HTTP calls with docstrings for tool calling.
- **AgentExecutor**: handles reasoning-action-observation loop.

## Recommended Extensions

- Add tools for potions/wands from Hogwarts API.
- Change model: update `LANGUAGE_MODEL` in `.env`.
- Change model: update `EMBEDDING_MODEL` in `.env`.
- Integrate RAG: use embeddings for local documents.
- Deploy: wrap in FastAPI for API endpoints.
- Multi-tool: expand with calculator or file I/O.

## Best Practices

- **Logging**: enable verbose for reasoning debug.
- **Rate limiting**: handle API delays with `time.sleep`.
- **Offline testing**: mock API for local development.
- **API Key**: none required, all local except Hogwarts API.
- **Updates**: `pip install -U -r requirements.txt` + pull models.

## License

![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)**.  
See `LICENSE` for details. Fork freely for non-commercial projects.
