# TODO решите задачу
import json
file_path = "input.json"


def task() -> float:
    total_sum = 0.0

    with open(file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        score = item['score']
        weight = item['weight']
        result = score * weight
        total_sum += result

    return round(total_sum, 3)


print(task())
