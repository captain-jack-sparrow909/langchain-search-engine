from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

@tool
def search_web(query: str) -> str:
    """Tool to search the web for information.
    Args:
        query: The query to search the web for.
    Returns:
        The search results.
    """
    print(f"Searching the web for {query}")
    return "Search results for " + query

llm = ChatOpenAI(model="gpt-5-nano")
tools = [search_web]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from search-engine!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the capital of France?")]})
    print(result)


if __name__ == "__main__":
    main()
