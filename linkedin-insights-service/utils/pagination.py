from typing import List

def paginate(data: List[dict], page: int = 1, limit: int = 10):
    """Paginate a list of data."""
    start = (page - 1) * limit
    end = start + limit
    return {
        "page": page,
        "limit": limit,
        "total_items": len(data),
        "total_pages": (len(data) // limit) + (1 if len(data) % limit > 0 else 0),
        "data": data[start:end]
    }

# Example usage:
# print(paginate([{"id": i} for i in range(100)], page=2, limit=10))
