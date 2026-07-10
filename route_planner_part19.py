# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RoutePlanner
def archive_records(archive_file, records_to_archive):
    """Archive completed or old route planner records to a separate file."""
    archived = []
    for record in records_to_archive:
        if 'completed' in record and record['completed']:
            archived.append(record.copy())
        elif 'distance_miles' in record and record['distance_miles'] < 10:
            archived.append(record.copy())

    with open(archive_file, 'a') as f:
        for item in archived:
            f.write(f"--- Archived Record ---\n")
            f.write(json.dumps(item, indent=2))
            f.write('\n\n')

    print(f"{len(archived)} record(s) archived to {archive_file}")
