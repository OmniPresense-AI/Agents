from google.adk.agents import Agent
from datetime import datetime
import os
from dotenv import load_dotenv
from typing import List, Dict
import json
import litellm
from google.adk.tools import FunctionTool
import requests

load_dotenv()


root_agent = Agent(
    name="industry_finder_agent",
    model="openai/gpt-3.5-turbo",
    description="An agent that helps identify and classify industries based on business descriptions",
    instruction=f"""You're an industry classification expert. Today is {datetime.now()}.
You can help users by:
- Identifying the correct industry classification for a business
- Explaining industry codes and standards
- Providing industry-specific information
- Suggesting relevant industry categories

Always:
- Reference standard industry classification systems (NAICS, SIC, GICS)
- Provide clear explanations of industry categories
- Include both primary and secondary industry classifications
- Explain the business relevance of each classification
- Use the industry_search tool to find relevant industry information""",
    tools=[]
)