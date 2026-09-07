# === Stage 43: Добавь пагинацию длинных списков ===
# Project: RoutePlanner
def paginate(items, page_size=10, page=1):
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    page = max(1, min(page, total_pages))
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "page": page,
        "total_pages": total_pages,
        "total": len(items),
        "items": items[start:end],
        "has_next": end < len(items),
        "has_prev": page > 1,
    }
