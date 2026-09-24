# Flexi Agentic AI

A simple sequential multi-agent research workflow powered by Tavily:

1. The Planner Agent accepts the user's topic and creates a plan.
2. The Search Agent retrieves current web results from Tavily.
3. The Analyst Agent extracts titles and content from the results.
4. The Writer Agent formats the findings into a final report.

The generated report is printed to the terminal and saved as `final_report.txt`.

## Requirements

- Python 3.10 or newer
- A Tavily API key

## Setup

Create a local `.env` file in this folder:

```env
TAVILY_API_KEY=your_tavily_api_key
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

The `.env` file is ignored by Git and must not be committed.

## Run

```bash
python main.py
```

Enter a topic when prompted. The workflow searches Tavily, analyzes the results, and writes the report to `final_report.txt`.

## Project Structure

- `main.py`: Coordinates the agent workflow.
- `planner.py`: Creates the research plan.
- `search_agent.py`: Searches the web through Tavily.
- `analyst.py`: Summarizes search result content.
- `writer.py`: Builds the final report.
- `requirements.txt`: Python dependencies.
