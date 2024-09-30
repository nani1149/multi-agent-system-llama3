
from langchain.chains import ConversationalRetrievalChain
import chainlit as cl
from langchain.schema.runnable.config import RunnableConfig
from workflow import graph
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

welcome_message = """Welcome Agentic Supervision Workflow:
1.Ask a question related research or code
"""


@cl.on_chat_start
async def start():
    msg = cl.Message(content=welcome_message)
    await msg.send()

    # cl.user_session.set("graph", workflow.compile())

@cl.on_message

async def run_convo(message: cl.Message):
#"what is the weather in sf"
    inputs = {"messages": [HumanMessage(content=message.content)]}

    res = graph.invoke(inputs, config=RunnableConfig(callbacks=[
        cl.LangchainCallbackHandler(
            to_ignore=["ChannelRead", "RunnableLambda", "ChannelWrite", "__start__", "_execute"]
            # can add more into the to_ignore: "agent:edges", "call_model"
            # to_keep=

        )]))

    await cl.Message(content=res["messages"][-1].content).send()
