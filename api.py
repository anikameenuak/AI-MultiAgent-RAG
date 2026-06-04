from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph.workflow import build_graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str

@app.post("/run")
def run_agents(body: Query):
    graph = build_graph()
    result = graph.invoke({"query": body.query})
    return {
        "plan": result.get("plan", ""),
        "research": result.get("research", ""),
        "final": result.get("final", "")
    }