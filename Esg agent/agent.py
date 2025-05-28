from google.adk.agents import Agent
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


esg_agent = Agent()

root_agent = Agent(
    name="esg_agent",
    model="gemini-2.5-flash-preview-04-17",
    description="An ESG analysis agent that can evaluate environmental, social, and governance metrics",
    instruction=f"""You're an ESG analysis assistant. Today is {datetime.now()}.
You can help users by:
- Analyzing environmental impact metrics
- Evaluating social responsibility
- Assessing governance practices
- Generating comprehensive ESG reports
Always provide detailed explanations for your assessments and recommendations.""",
    tools=[
        esg_agent.analyze_environmental_impact,
        esg_agent.evaluate_social_responsibility,
        esg_agent.assess_governance,
        esg_agent.generate_esg_report
    ],
)
