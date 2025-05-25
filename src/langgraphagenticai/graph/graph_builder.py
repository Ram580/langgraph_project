from langgraph.graph import StateGraph, START, END 
from langgraph.prebuilt  import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate

from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tool, create_tool_node
from src.langgraphagenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode

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
       
       
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        
        # Assuming get_tool() returns a list of tools
        
        tools = get_tool()
        tool_node = create_tool_node(tools)
        
        # define the llm
        llm = self.llm
        
        ## Define the tool and tool node
        obj_chatbot_with_node = ChatbotWithToolNode(self.llm)
        chatbot = obj_chatbot_with_node.create_chatbot(tools)
        
        self.graph_builder.add_node("chatbot", chatbot)
        self.graph_builder.add_node("tools", tool_node)
        
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", END)
          
       
    def setup_graph(self, usecase):
        """
        Sets up the graph based on the selected use case.
        
        Args:
            usecase (str): The selected use case for the graph.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            
            
        if usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()
        
        return self.graph_builder.compile()
        