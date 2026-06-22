from google.adk.tools import ToolContext

def calculate_uplift(test_rate: float, control_rate: float) -> float:
    """
    Calculate campaign uplift percentage.
    """
    return round(((test_rate - control_rate) / control_rate) * 100, 2)

def calculate_ctr(clicks: int, impressions: int) -> float:
    """Calculate Click Through Rate.
Use when user asks for CTR,
engagement rate,
or click performance.
    """
    return round((clicks / impressions) * 100, 2)

def calculate_conversion_rate(conversions: int, visitors: int) -> float:
    """
    Calculate conversion rate percentage.
    """
    return round((conversions / visitors) * 100, 2)

def calculate_roi(revenue: float, cost: float) -> float:
    """
    Calculate ROI percentage.
    """
    return round(((revenue - cost) / cost) * 100, 2)

campaign_state = {}
def store_metric(metric_name: str, value: float) :
    """
    Store campaign metric in memory
    Use when user wants to save revenue, cost, clicks, impressions.
    """
    campaign_state[metric_name] = value
    return f"Stored {metric_name} = {value}."

def show_state():
    """
    Show all stored campaign metrics.
    Use when user wants to see current campaign state.
    """
    return campaign_state

def store_revenue(revenue: float,tool_context: ToolContext) :
    """
    Store campaign revenue in session state.
    """
    tool_context.state['revenue'] = revenue
    return f"Stored revenue = {revenue}."

def store_cost(cost: float,tool_context: ToolContext) :
    """
    Store campaign cost in session state.
    """
    tool_context.state['cost'] = cost
    return f"Stored cost = {cost}."

def show_metrics(tool_context: ToolContext):
    """
    Show all stored campaign metrics from session state.
    """
    return dict(tool_context.state)

def calculate_roi_from_state(
    tool_context: ToolContext
):
    """
    Calculate ROI using stored revenue and cost.
    """

    revenue = tool_context.state.get("revenue")
    cost = tool_context.state.get("cost")

    if revenue is None:
        return "Revenue not found."

    if cost is None:
        return "Cost not found."

    roi = ((revenue - cost) / cost) * 100

    return {
        "revenue": revenue,
        "cost": cost,
        "roi": round(roi, 2)
    }

from google.adk.tools import ToolContext

def debug_state(tool_context: ToolContext):
    """
    Debug ADK state
    """

    return {
        "state_type": str(type(tool_context.state)),
        "state_value": str(tool_context.state)
    }