from supervisor import supervisor_agent,members
from agents import code_node,research_node,AgentState
from langgraph.graph import END, StateGraph, START
from langchain_core.messages import HumanMessage



workflow = StateGraph(AgentState)
workflow.add_node("Researcher", research_node)
workflow.add_node("Coder", code_node)
workflow.add_node("supervisor", supervisor_agent)
for member in members:
    # We want our workers to ALWAYS "report back" to the supervisor when done
    workflow.add_edge(member, "supervisor")
# The supervisor populates the "next" field in the graph state
# which routes to a node or finishes
conditional_map = {k: k for k in members}
print(conditional_map)
conditional_map["FINISH"] = END
workflow.add_conditional_edges(
    "supervisor", 
    lambda x: (print(x), x.get("next", "FINISH"))[-1],  # Print x and fetch 'next' safely
    conditional_map
)
# Finally, add entrypoint
workflow.add_edge(START, "supervisor")

graph = workflow.compile()

events = graph.stream(
    {
        "messages": [
            HumanMessage(
                content="Write a brief research report on pikas."
            )
        ],
    },
    # Maximum number of steps to take in the graph
    {"recursion_limit": 150},
)
for s in events:
    print(s)
    print("----")
