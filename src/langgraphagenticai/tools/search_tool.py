from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode
import os
import streamlit as st
from dotenv import load_dotenv
def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    load_dotenv()
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY", "")
    tools=[TavilySearch(max_results=2,tavily_api_key  = TAVILY_API_KEY)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)

