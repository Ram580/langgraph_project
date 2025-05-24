from langgraph.graph import StateGraph, START, END 
from langgraph.prebuilt  import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate

from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder=StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph with a single tool node.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot", END)
       
    def setup_graph(self, usecase):
        """
        Sets up the graph based on the selected use case.
        
        Args:
            usecase (str): The selected use case for the graph.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()
        