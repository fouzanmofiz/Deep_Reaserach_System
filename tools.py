import os
import requests
from langchain_core.tools import tool
from bs4 import BeautifulSoup
from tavily import TavilyClient

from dotenv import load_dotenv
from rich import print
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_Search(query : str)-> str:
    """Search the web for recent and reliable information on a topic. Return tittles, URL and snippet."""
    result = tavily.search(query = query, max_result = 5)

    out = []

    for r in result['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n----\n".join(out)

if __name__ == "__main__":
    print(web_Search.invoke("What is the latest news of war?"))

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
    
    



