from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    TAVILY_API_KEY = "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"
    tools=[TavilySearch(max_results=2,tavily_api_key  = TAVILY_API_KEY)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)

