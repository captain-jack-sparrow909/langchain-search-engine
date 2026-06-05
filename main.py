from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
import os

load_dotenv()

tavily_search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))


llm = ChatOpenAI(model="gpt-5-nano")
tools = [tavily_search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from search-engine!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather at Paris, France?")]})
    print(result)


if __name__ == "__main__":
    main()
