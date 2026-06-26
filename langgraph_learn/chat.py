from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    return {"message": ["hi, this is a message from chatbot node "]}    

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)