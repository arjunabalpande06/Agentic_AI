class AnalystAgent:
    """
    Fundamentals Analyst Agent
    Processes the search results and prepares a summary.
    """

    def analyze(self, search_results):
        print("\n[Fundamentals Analyst Agent]")
        print("Analyzing search results...")

        summary = []

        if "results" in search_results:
            for result in search_results["results"]:
                title = result.get("title", "No Title")
                content = result.get("content", "No Content")

                summary.append(
                    f"Title: {title}\nSummary: {content}\n"
                )

        return summary
