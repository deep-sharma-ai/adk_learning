def calculator(expression: str) -> float:
    """
    Evaluate a mathematical expression and return the result.
    """
    try:
        # Safely evaluate the expression
        allowed_names = {"__builtins__": None}
        return eval(expression, allowed_names)
    except Exception as e:
        return f"Error evaluating expression: {e}"