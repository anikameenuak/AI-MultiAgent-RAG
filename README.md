⚡ AgentIQ — AI Multi-Agent Research System

A production-grade multi-agent AI pipeline built with LangGraph, Groq LLaMA 3.3, ChromaDB, and FastAPI — capable of autonomously planning, researching, writing, and critically refining answers to any query.


🚀 Live Demo

# 🤖 AI Multi-Agent RAG System

🚀 Live Demo:
https://ai-multiagent-rag-b4v8ge9fallau7mi4mt7az.streamlit.app/

📂 GitHub Repository:
https://github.com/anikameenuak/AI-MultiAgent-RAG

## Features
- Multi-Agent Architecture
- LangGraph Workflow
- RAG with ChromaDB
- Streamlit UI
- Planner Agent
- Research Agent
- Writer Agent


🧠 What It Does
AgentIQ uses 4 specialized AI agents that collaborate in a sequential pipeline to deliver polished, accurate research reports on any topic.
User Query
    ↓
🧠 Planner Agent      → Breaks query into actionable steps
    ↓
🔍 Researcher Agent   → Web search (DuckDuckGo) + ChromaDB RAG retrieval
    ↓
✍️  Writer Agent       → Converts research into a structured report
    ↓
🎯 Critic Agent       → Reviews grammar, structure, removes repetition
    ↓
📄 Final Output

🛠️ Tech Stack
TechnologyPurposeLangGraphMulti-agent workflow orchestrationGroq LLaMA 3.3 70BLLM backbone for all agentsChromaDBVector database for RAG retrievalSentence TransformersText embeddings (all-MiniLM-L6-v2)DuckDuckGo SearchReal-time web searchFastAPIREST API backendStreamlitWeb UI interfacePython 3.12Core language

📁 Project Structure
AI_MultiAgent_RAG/
├── agents/
│   ├── planner.py          # Planning agent
│   ├── researcher.py       # Research agent (web + RAG)
│   ├── writer.py           # Writing agent
│   ├── critic.py           # Critic/review agent
│   └── summarizer_agent.py # Summarization agent
├── graph/
│   ├── workflow.py         # LangGraph pipeline definition
│   └── state.py            # Shared agent state schema
├── tools/
│   ├── web_search.py       # DuckDuckGo search tool
│   ├── rag_tool.py         # ChromaDB vector store tool
│   ├── pdf_reader.py       # PDF ingestion tool
│   └── calculator.py       # Calculator tool
├── utils/
│   ├── llm.py              # Centralized LLM initialization
│   ├── logger.py           # Logging utility
│   └── helper.py           # Helper functions
├── api.py                  # FastAPI backend
├── app.py                  # Streamlit UI
├── main.py                 # CLI entry point
└── requirements.txt

⚙️ Setup & Installation
1. Clone the repository
bashgit clone https://github.com/anikameenuak/AI-MultiAgent-RAG.git
cd AI-MultiAgent-RAG
2. Create virtual environment
bashpython -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
3. Install dependencies
bashpip install -r requirements.txt
4. Set up environment variables
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here
Get your free Groq API key at console.groq.com

▶️ Running the Project
Option 1: Command Line
bashpython main.py
Option 2: Streamlit UI
bashstreamlit run app.py
Option 3: HTML UI (Recommended)
Terminal 1 — Start the backend:
bashuvicorn api:app --reload --port 8000
Then — Open index.html directly in your browser.

🔍 How RAG Works in This Project

The Researcher Agent performs a live web search using DuckDuckGo
Search results are chunked and stored in ChromaDB (persistent vector store)
Relevant context is retrieved using semantic similarity search
Both web data and retrieved context are passed to the LLM for richer answers


🤖 Agent Details
AgentModelRolePlannerLLaMA 3.3 70BBreaks query into numbered stepsResearcherLLaMA 3.3 70BWeb search + RAG retrieval + synthesisWriterLLaMA 3.3 70BConverts research into structured reportCriticLLaMA 3.3 70BReviews and improves final output

📦 Requirements
langchain-groq
langgraph
chromadb
sentence-transformers
duckduckgo-search
fastapi
uvicorn
streamlit
python-dotenv

👩‍💻 Author
Anika — AI/ML Engineering Student
GitHub: @anikameenuak

📄 License
MIT License — free to use and modify.