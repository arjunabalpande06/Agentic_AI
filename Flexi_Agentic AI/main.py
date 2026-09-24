from planner import PlannerAgent
from search_agent import SearchAgent
from analyst import AnalystAgent
from writer import WriterAgent


def main():
    print("=" * 50)
    print("     Multi-Agent AI System using Tavily")
    print("=" * 50)

    # User Input
    query = input("\nEnter your topic: ")

    # Create Agent Objects
    planner = PlannerAgent()
    search = SearchAgent()
    analyst = AnalystAgent()
    writer = WriterAgent()

    # Step 1: Planner Agent
    plan = planner.plan(query)

    # Step 2: Search Agent
    search_results = search.search(plan["topic"])

    # Step 3: Analyst Agent
    summary = analyst.analyze(search_results)

    # Step 4: Writer Agent
    final_report = writer.write(plan["topic"], summary)

    # Display Final Report
    print(final_report)

    # Save the report to disk as well
    with open("final_report.txt", "w", encoding="utf-8") as f:
        f.write(final_report)
    print("\nSaved to final_report.txt")


if __name__ == "__main__":
    main()
