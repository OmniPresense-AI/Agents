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

# Configure OpenAI API key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

car_rental_agent = Agent()

root_agent = Agent(
    name="car_rental_sasb_agent",
    model="openai/gpt-3.5-turbo",  # Using OpenAI model
    description="An agent that provides information about SASB standards for the Car Rental & Leasing industry",
    instruction=f"""You're a SASB standards expert for the Car Rental & Leasing industry. Today is {datetime.now()}.
You can help users by:
- Answering questions about SASB standards for Car Rental & Leasing
- Explaining reporting requirements
- Providing guidance on specific metrics
- Identifying relevant sustainability indicators

Always:
- Reference specific SASB codes when applicable
- Provide clear explanations of reporting requirements
- Include both mandatory and recommended metrics
- Explain the business relevance of each metric
- Use the file_search tool to find relevant information in the document store""",
    tools=[]
)