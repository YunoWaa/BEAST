# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RoutePlanner
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


def add_tag(tag_name, route_point=None, distance=None, task=None, note=None):
    """Добавить тег к объекту (route point / distance / task / note)."""
    if not tag_name:
        raise ValueError("Тег должен быть непустым")

    def _tag_object(obj):
        if obj is None:
            raise ValueError(f"Объект {type(obj).__name__} не задан")
        obj.tags = obj.tags or []
        tags_set = set(t.name for t in obj.tags)
        if tag_name not in tags_set:
            obj.tags.append(Tag(tag_name))

    if route_point is not None:
        _tag_object(route_point)
    elif distance is not None:
        _tag_object(distance)
    elif task is not None:
        _tag_object(task)
    elif note is not None:
        _tag_object(note)
    else:
        raise ValueError("Укажите route point, distance, task или note")

    return obj


def remove_tag(tag_name, route_point=None, distance=None, task=None, note=None):
    """Удалить тег из объекта."""
    if not tag_name:
        raise ValueError("Тег должен быть непустым")

    def _remove_from(obj):
        if obj is None or not getattr(obj, 'tags', []):
            return obj
        obj.tags = [t for t in obj.tags if t.name != tag_name]
        return obj

    if route_point is not None:
        return _remove_from(route_point)
    elif distance is not None:
        return _remove_from(distance)
    elif task is not None:
        return _remove_from(task)
    elif note is not None:
        return _remove_from(note)
    else:
        raise ValueError("Укажите route point, distance, task или note")
