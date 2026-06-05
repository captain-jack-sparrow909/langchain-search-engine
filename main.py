from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
import os
from pydantic import BaseModel, Field

load_dotenv()

tavily_search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))

class Source(BaseModel):
    """Information about the source"""
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Response from the agent"""
    answer: str = Field(description="The answer to the question")
    sources: list[Source] = Field(default_factory=list, description="The sources used to answer the question")


llm = ChatOpenAI(model="gpt-5-nano")
tools = [tavily_search]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from search-engine!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather at Paris, France?")]})
    print(result)


if __name__ == "__main__":
    main()
