from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

def get_tool():
    """
    Returns a Tool that allows searching using Tavilly.
    This function creates a Tavilly search tool with a maximum of 5 results.
    """
    tools = [TavilySearchResults(max_results=5)]
    return tools
    
def create_tool_node(tools):
    """
    Creates a ToolNode for the Tavilly search tool.
    
    This function wraps the Tavilly search tool in a ToolNode, allowing it to be used in a LangGraph workflow.
    
    Returns:
        ToolNode: A node that can be used in a LangGraph workflow for search functionality.
    """
    return ToolNode(tools=tools)