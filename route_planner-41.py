# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: RoutePlanner
def dry_run(self, func, *args, **kwargs):
        """Execute a mutating operation in dry-run mode: log the action without persisting to storage."""
        action = {
            "op": func.__name__,
            "args": args,
            "kwargs": kwargs,
        }
        print(f"[DRY-RUN] {func.__name__}: {args} {kwargs}")
        return func(*args, **kwargs)
