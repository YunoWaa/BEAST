# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RoutePlanner
def validate_and_repair_routes(routes):
    repaired = []
    for route in routes:
        r = {"points": [], "tasks": [], "notes": [], "errors": []}
        for p in route.get("points", []):
            if isinstance(p, dict):
                if "lat" in p and "lon" in p:
                    r["points"].append({"lat": float(p["lat"]), "lon": float(p["lon"])})
                    continue
                if isinstance(p, str) and p.startswith("POINT"):
                    coords = p.split()[1].split()
                    r["points"].append({"lat": float(coords[0]), "lon": float(coords[1])})
                    continue
                r["errors"].append(f"invalid point: {p}")
            else:
                r["errors"].append(f"invalid point type: {type(p)}")
        for t in route.get("tasks", []):
            if isinstance(t, dict) and "name" in t:
                r["tasks"].append(t)
            else:
                r["errors"].append(f"invalid task: {t}")
        for n in route.get("notes", []):
            if isinstance(n, str) and len(n) > 0:
                r["notes"].append(n)
            else:
                r["errors"].append(f"invalid note: {n}")
        if r["errors"]:
            r["points"] = r["points"][:0]
            r["tasks"] = r["tasks"][:0]
            r["notes"] = r["notes"][:0]
            r["errors"] = r["errors"]
        repaired.append(r)
    return repaired
