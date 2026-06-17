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