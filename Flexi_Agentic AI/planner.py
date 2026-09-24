class PlannerAgent:
    """
    Planner Agent
    Breaks the user's request into a plan.
    """

    def plan(self, query):
        print("\n[Planner Agent]")
        print("Creating a plan...")

        plan = {
            "topic": query,
            "steps": [
                "Search information",
                "Analyze information",
                "Generate report",
            ],
        }

        return plan
