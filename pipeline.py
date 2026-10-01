from agent import build_read_Agent, build_search_Agent, writer_chain, critic_chain

def run_research_pipeline(topic: str, callback=None) -> dict:
    """
    Runs the full multi-agent research pipeline.
    Optionally accepts a callback(step_num: int, step_title: str, detail: str) to report progress.
    """
    state = {}

    def notify(step_num: int, step_title: str, detail: str = ""):
        if callback and callable(callback):
            try:
                callback(step_num, step_title, detail)
            except Exception:
                pass

    # Step 1 - Search Agent
    print("\n" + " =" * 50)
    print("step 1 - search agent is working ...")
    print("=" * 50)
    notify(1, "Search Agent Working", "Searching Tavily for recent, reliable, and detailed sources...")

    search_agent = build_search_Agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = search_result['messages'][-1].content

    print("\n search result ", state['search_results'])

    # Step 2 - Reader Agent
    print("\n" + " =" * 50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("=" * 50)
    notify(2, "Reader Agent Scraping", "Selecting top URL and scraping deep content via BeautifulSoup...")

    reader_agent = build_read_Agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\nscraped content: \n", state['scraped_content'])

    # Step 3 - Writer Chain
    print("\n" + " =" * 50)
    print("step 3 - Writer is drafting the report ...")
    print("=" * 50)
    notify(3, "Writer Agent Drafting", "Synthesizing research data into a structured research report...")

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report\n", state['report'])

    # Step 4 - Critic Report
    print("\n" + " =" * 50)
    print("step 4 - critic is reviewing the report ")
    print("=" * 50)
    notify(4, "Critic Agent Reviewing", "Evaluating report quality, strengths, weaknesses, and final score...")

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })

    print("\n critic report \n", state['feedback'])
    notify(5, "Pipeline Completed", "All agent steps finished successfully.")

    return state

if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)
