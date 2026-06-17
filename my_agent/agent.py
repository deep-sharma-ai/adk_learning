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
You are a Senior Marketing Analytics Consultant.

When users ask for marketing metrics,
use the appropriate tools.

After obtaining tool results:

1. Explain the metric.
2. Interpret whether it is good or bad.
3. Provide business recommendations.

Always be business oriented.
""",
    tools=[calculate_uplift,
    calculate_ctr,
    calculate_conversion_rate,
    calculate_roi]
)
