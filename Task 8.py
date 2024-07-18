import datetime

def process_data(filename):
    """Обработка данных из файла."""
    pool_data = {}
    center_data = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) != 4:
                log_error(f"Некорректная строка: {line.strip()}")
                continue
            athlete_id, location, time_in, time_out = parts
            if location == "Pool-1" or location == "Pool-2":
                update_location_data(pool_data, athlete_id, location, time_in, time_out)
            elif location == "Center":
                update_location_data(center_data, athlete_id, location, time_in, time_out)
            else:
                log_error(f"Неизвестное местоположение: {location}")

    print_results(pool_data, "Pool")
    print_results(center_data, "Center")

def update_location_data(data, athlete_id, location, time_in, time_out):
    """Обновляет данные о времени входа и выхода для указанного места."""
    if athlete_id not in data:
        data[athlete_id] = {}
    if location not in data[athlete_id]:
        data[athlete_id][location] = {}
    if time_in:
        data[athlete_id][location]["time_in"] = time_in
    if time_out:
        data[athlete_id][location]["time_out"] = time_out

def print_results(data, location_type):
    """Печатает результаты вычислений."""
    for athlete_id, locations in data.items():
        for location, times in locations.items():
            if "time_in" in times and "time_out" in times:
                time_in = times["time_in"]
                time_out = times["time_out"]
                time_spent = calculate_time_difference(time_in, time_out)
                print(f"Атлет {athlete_id} провёл в {location}: {time_spent} мин.")
            else:
                if "time_in" not in times:
                    log_error(f"Не зафиксировано время входа атлета {athlete_id} в {location}")
                if "time_out" not in times:
                    log_error(f"Не зафиксировано время выхода атлета {athlete_id} из {location}")

def calculate_time_difference(time_in, time_out):
    """Рассчитывает разницу между двумя временами."""
    try:
        in_time = datetime.datetime.strptime(time_in, "%H:%M")
        out_time = datetime.datetime.strptime(time_out, "%H:%M")
        time_difference = out_time - in_time
        return int(time_difference.total_seconds() / 60)
    except ValueError:
        log_error(f"Некорректное время: {time_in} или {time_out}")
        return None

def log_error(error_message):
    """Записывает ошибку в лог."""
    with open("logs.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} | ERROR    | {error_message}\n")

if __name__ == "__main__":
    process_data("data.txt")