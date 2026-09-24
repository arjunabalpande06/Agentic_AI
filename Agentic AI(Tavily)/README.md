# Agentic AI Tavily

A small AI agent project containing:

- `agent.py`: Runs a fact-checking agent with the OpenAI Agents SDK through Groq's OpenAI-compatible API.
- `tavily.py`: Demonstrates a Tavily web-search tool wrapped as a LangChain tool.

## Requirements

- Python 3.10 or newer
- A Groq API key for `agent.py`
- A Tavily API key for `tavily.py`

## Setup

From this folder, create a local `.env` file:

```env
OPENAI_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Install the packages used by the scripts:

```bash
pip install openai-agents openai python-dotenv ipython tavily-python langchain-core
```

The `.env` file is ignored by Git and must not be committed.

## Run the fact-checker

```bash
python agent.py
```

The script checks a sample statement and prints the agent's verdict.

## Run the Tavily search example

```bash
python tavily.py
```

This performs a sample web search and prints the returned tool output.

## Notes

`agent.py` uses the Groq endpoint with the `llama-3.3-70b-versatile` model. Update the sample statement in the script to check a different claim.
