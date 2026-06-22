from google.adk.agents.llm_agent import Agent
from .tool import (
    calculate_uplift,
    calculate_ctr,
    calculate_conversion_rate,
    calculate_roi,
    store_revenue,
    store_cost,
    show_metrics,
    calculate_roi_from_state,
    debug_state
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
If user wants to save revenue,
use store_revenue.

If user wants to save cost,
use store_cost.

If user asks for stored metrics,
use show_metrics.

If user asks to calculate ROI using stored values,
use calculate_roi_from_state.
""",
    tools=[calculate_uplift,
    calculate_ctr,
    calculate_conversion_rate,
    calculate_roi,
    store_revenue,
    store_cost,
    show_metrics,
    calculate_roi_from_state,
    debug_state]
)
