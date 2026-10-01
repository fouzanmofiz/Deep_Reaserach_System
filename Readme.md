# Multi-Agent Research System

## 1. Project Overview
- What problem the project solves
- What the system does
- Why multiple agents are used

## 2. Key Features
- Web search
- Web page scraping
- Research synthesis
- Report generation
- Report criticism/review
- Streamlit UI
- LLM integration through OpenRouter

## 3. System Architecture
- Add architecture diagram
- Show how user request flows through different agents

## 4. Agents
- Search Agent
- Reader Agent
- Writer Agent
- Critic Agent

## 5. Technology Stack
- Python
- LangChain
- LangGraph
- OpenRouter
- Tavily
- BeautifulSoup
- Streamlit
- Requests
- python-dotenv


## 7. Workflow
1. User enters research topic
2. Search Agent searches the web
3. Reader Agent selects and scrapes relevant sources
4. Writer Agent creates the research report
5. Critic Agent reviews the report
6. Streamlit displays the results

## 8. Architecture Diagram

                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Streamlit UI   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Research        │
                    │ Pipeline        │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌────────────┐ ┌────────────┐ ┌────────────┐
       │   Search   │ │   Reader   │ │   Writer   │
       │   Agent    │ │   Agent    │ │   Agent    │
       └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
             │              │              │
             ▼              ▼              ▼
          Tavily       BeautifulSoup   OpenRouter
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                     ┌─────────────┐
                     │    Report   │
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │   Critic    │
                     │    Agent    │
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │   Final     │
                     │   Output    │
                     └─────────────┘



## 9. Installation
- Clone repository
- Create virtual environment
- Install requirements

## 10. Environment Variables
- OPENROUTER_API_KEY
- TAVILY_API_KEY

## 11. How to Run
- streamlit run app.py

## 12. Example
- Example research topic
- Example output

## 13. Future Improvements
- More agents
- Source citation
- PDF export
- Persistent research history
- Parallel research
- Better fact verification

