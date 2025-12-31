from typing import List

def normalize(values: List[float], maximize: bool = True) -> List[float]:
    """Normalize a list of numbers to 0-1 scale"""
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [1.0 for _ in values]
    if maximize:
        return [(v - min_val) / (max_val - min_val) for v in values]
    else:
        return [(max_val - v) / (max_val - min_val) for v in values]
