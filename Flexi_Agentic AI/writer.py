class WriterAgent:
    """
    Writer Agent
    Generates the final report using the analyzed data.
    """

    def write(self, topic, summary):
        print("\n[Writer Agent]")
        print("Generating final report...\n")

        report = f"""
========================================
              FINAL REPORT
========================================

Topic:
{topic}

Summary:
"""

        for item in summary:
            report += item + "\n"

        report += "\nReport Generated Successfully."

        return report
