# AI Agent System

A multi-agent AI research and report-generation system built with FastAPI, Streamlit, LangGraph, Groq, and Tavily.

The app takes a user query, gathers recent web research, analyzes the findings, drafts an executive-style report, and reviews the output before returning the final result.

## Features

- Research agent that retrieves real-time web context with Tavily
- Analysis agent that ranks key insights, risks, opportunities, and contradictions
- Writer agent that turns the analysis into a concise business report
- Reviewer agent that checks the draft before final output
- FastAPI backend endpoint for running the workflow
- Streamlit frontend for entering queries and viewing each agent stage

## Project Structure

```text
.
├── agents/
│   ├── analysis_agent.py
│   ├── research_agent.py
│   ├── reviewer_agent.py
│   └── writer_agent.py
├── api/
│   └── server.py
├── graph/
│   └── workflow.py
├── tools/
│   ├── llm.py
│   └── search_tool.py
├── ui/
│   └── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11 or newer
- Groq API key
- Tavily API key

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_groq_model
TAVILY_API_KEY=your_tavily_api_key
```

Example Groq models include `llama3-70b-8192` or another chat model available in your Groq account.

## Run the App

Start the FastAPI backend:

```bash
uvicorn api.server:app --reload
```

In a second terminal, start the Streamlit UI:

```bash
streamlit run ui/app.py
```

Open the Streamlit URL shown in the terminal, enter a query, and click **Run**.

## API Usage

You can also call the backend directly:

```bash
curl -X POST http://127.0.0.1:8000/run \
  -H "Content-Type: application/json" \
  -d '{"query":"latest AI agent trends"}'
```

The response contains:

- `research`
- `analysis`
- `draft`
- `final`

## Notes

- Do not commit `.env` or API keys to GitHub.
- The local `venv/` folder is ignored and should be recreated with `pip install -r requirements.txt`.
- The backend must be running before using the Streamlit UI.
