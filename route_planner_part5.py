# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RoutePlanner
def delete_record(record_id, records):
    if record_id in records:
        del records[record_id]
        return True
    else:
        print(f"Запись с ID {record_id} не найдена.")
        return False

if __name__ == "__main__":
    sample_records = {"101": "Москва", "102": "Санкт-Петербург"}
    delete_record("101", sample_records)
    print(sample_records)
