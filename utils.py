from langchain_core.messages import HumanMessage
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    ToolMessage,
)
from langchain_core.messages import AIMessage

# def agent_node(state, agent, name):
#     result = agent.invoke(state)
#     return {"messages": [HumanMessage(content=result["messages"][-1].content, "next":name)]}

def agent_node(state, agent, name):
    result = agent.invoke(state)
    # We convert the agent output into a format that is suitable to append to the global state
    if isinstance(result, ToolMessage):
        pass
    else:
        result = AIMessage(**result.dict(exclude={"type", "name"}), name=name)
    return {
        "messages": [result],
        # Since we have a strict workflow, we can
        # track the sender so we know who to pass to next.
        "next": name,
    }