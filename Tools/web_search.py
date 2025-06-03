from crewai_tools import ScrapeWebsiteTool
from google.adk.tools.crewai_tool import CrewaiTool

scrape_tool = ScrapeWebsiteTool()

web_search = CrewaiTool(
    name="web_search",
    description="Use this tool to search the web for relevant information about the company ",
    tool=scrape_tool
)