from google.adk.agents.llm_agent import Agent
from .tool import (
    calculate_uplift,
    calculate_ctr,
    calculate_conversion_rate,
    calculate_roi
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='first_agent',
    description='Data science personal agent',
    instruction="""
You are an experienced Senior Data Scientist.

Use available tools whenever calculations are required.
Always explain business implications.
""",
    tools=[calculate_uplift,
    calculate_ctr,
    calculate_conversion_rate,
    calculate_roi]
)
