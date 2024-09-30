from workflow import graph
from langchain_core.messages import HumanMessage

from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
# for s in graph.stream(
#     {
#         "messages": [
#             HumanMessage(content="Code hello world and print it to the terminal")
#         ]
#     }
# ):
#     if "__end__" not in s:
#         print(s)
#         print("----")

query = "Code hello world and print it to the terminal" 
messages = [HumanMessage(content=query)]

result = graph.invoke({"messages": messages})
print(result)