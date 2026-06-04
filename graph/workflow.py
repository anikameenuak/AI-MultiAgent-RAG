# # # # from langgraph.graph import StateGraph, END
# # # # from typing import TypedDict

# # # # from agents.planner import run_planner
# # # # from agents.researcher_agent import run_researcher
# # # # from agents.writer import run_writer


# # # # # ---------------- STATE ----------------
# # # # class AgentState(TypedDict):
# # # #     query: str
# # # #     plan: str
# # # #     research: str
# # # #     final: str


# # # # # ---------------- NODES ----------------
# # # # def planner_node(state: AgentState):
# # # #     plan = run_planner(state["query"])
# # # #     return {"plan": plan}


# # # # def researcher_node(state: AgentState):
# # # #     research = run_researcher(state["plan"])
# # # #     return {"research": research}


# # # # def writer_node(state: AgentState):
# # # #     final = run_writer(state["research"])
# # # #     return {"final": final}


# # # # # ---------------- GRAPH ----------------
# # # # def build_graph():
# # # #     graph = StateGraph(AgentState)

# # # #     graph.add_node("planner", planner_node)
# # # #     graph.add_node("researcher", researcher_node)
# # # #     graph.add_node("writer", writer_node)

# # # #     graph.set_entry_point("planner")

# # # #     graph.add_edge("planner", "researcher")
# # # #     graph.add_edge("researcher", "writer")
# # # #     graph.add_edge("writer", END)

# # # #     return graph.compile()
# # # # graph.add_node("critic", critic_node)

# # # # graph.add_edge("writer", "critic")
# # # # graph.add_edge("critic", END)
# # # from langgraph.graph import StateGraph, END
# # # from typing import TypedDict

# # # from agents.planner import run_planner
# # # from agents.researcher_agent import run_researcher
# # # from agents.writer import run_writer


# # # # ---------------- STATE ----------------
# # # class AgentState(TypedDict):
# # #     query: str
# # #     plan: str
# # #     research: str
# # #     final: str


# # # # ---------------- NODES ----------------

# # # def planner_node(state: AgentState):
# # #     query = state["query"]
# # #     plan = run_planner(query)

# # #     return {
# # #         "query": query,
# # #         "plan": plan
# # #     }


# # # def researcher_node(state: AgentState):
# # #     plan = state["plan"]
# # #     research = run_researcher(plan)

# # #     return {
# # #         "query": state["query"],
# # #         "plan": plan,
# # #         "research": research
# # #     }


# # # def writer_node(state: AgentState):
# # #     research = state["research"]
# # #     final = run_writer(research)

# # #     return {
# # #         "query": state["query"],
# # #         "plan": state["plan"],
# # #         "research": research,
# # #         "final": final
# # #     }


# # # # ---------------- GRAPH ----------------
# # # def build_graph():
# # #     graph = StateGraph(AgentState)

# # #     graph.add_node("planner", planner_node)
# # #     graph.add_node("researcher", researcher_node)
# # #     graph.add_node("writer", writer_node)

# # #     graph.set_entry_point("planner")

# # #     graph.add_edge("planner", "researcher")
# # #     graph.add_edge("researcher", "writer")
# # #     graph.add_edge("writer", END)

# # #     return graph.compile()
# # from langgraph.graph import StateGraph
# # from graph.state import AgentState

# # from agents.planner import run_planner
# # from agents.researcher_agent import run_researcher
# # from agents.writer import run_writer


# # def planner_node(state: AgentState):
# #     plan = run_planner(state["query"])
# #     return {"plan": plan}


# # def researcher_node(state: AgentState):
# #     research = run_researcher(state["plan"])
# #     return {"research": research}


# # def writer_node(state: AgentState):
# #     final = run_writer(state["research"])
# #     return {"final": final}


# # def build_graph():
# #     workflow = StateGraph(AgentState)

# #     workflow.add_node("planner", planner_node)
# #     workflow.add_node("researcher", researcher_node)
# #     workflow.add_node("writer", writer_node)

# #     workflow.set_entry_point("planner")

# #     workflow.add_edge("planner", "researcher")
# #     workflow.add_edge("researcher", "writer")

# #     workflow.set_finish_point("writer")
# #     return workflow.compile()
# from langgraph.graph import StateGraph
# from graph.state import AgentState

# from agents.planner import run_planner
# from agents.researcher import run_researcher
# from agents.writer import run_writer


# def planner_node(state: AgentState):
#     return {"plan": run_planner(state["query"])}


# def researcher_node(state: AgentState):
#     return {"research": run_researcher(state["plan"])}


# def writer_node(state: AgentState):
#     return {"final": run_writer(state["research"])}


# def build_graph():
#     workflow = StateGraph(AgentState)

#     workflow.add_node("planner", planner_node)
#     workflow.add_node("researcher", researcher_node)
#     workflow.add_node("writer", writer_node)

#     workflow.set_entry_point("planner")

#     workflow.add_edge("planner", "researcher")
#     workflow.add_edge("researcher", "writer")

#     workflow.set_finish_point("writer")

#     return workflow.compile()
# from langgraph.graph import StateGraph, END

# from graph.state import AgentState

# from agents.planner import run_planner
# from agents.researcher import run_researcher   # ✅ adjust based on your file name
# from agents.writer import run_writer


# # ---------------- NODE FUNCTIONS ----------------

# def planner_node(state: AgentState):
#     return {"plan": run_planner(state["query"])}


# def researcher_node(state: AgentState):
#     return {"research": run_researcher(state["plan"])}


# def writer_node(state: AgentState):
#     return {"final": run_writer(state["research"])}


# # ---------------- BUILD GRAPH ----------------

# def build_graph():
#     workflow = StateGraph(AgentState)

#     workflow.add_node("planner", planner_node)
#     workflow.add_node("researcher", researcher_node)
#     workflow.add_node("writer", writer_node)

#     workflow.set_entry_point("planner")

#     workflow.add_edge("planner", "researcher")
#     workflow.add_edge("researcher", "writer")
#     workflow.add_edge("writer", END)   # ✅ correct termination

#     return workflow.compile()
from langgraph.graph import StateGraph, END
from graph.state import AgentState
from agents.planner import run_planner
from agents.researcher import run_researcher
from agents.writer import run_writer
from agents.critic import run_critic

def planner_node(state: AgentState):
    return {"plan": run_planner(state["query"])}

def researcher_node(state: AgentState):
    return {"research": run_researcher(state["plan"])}

def writer_node(state: AgentState):
    return {"final": run_writer(state["research"])}

def critic_node(state: AgentState):
    return {"final": run_critic(state["final"])}

def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("critic", critic_node)

    workflow.set_entry_point("planner")

    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "critic")
    workflow.add_edge("critic", END)

    return workflow.compile()