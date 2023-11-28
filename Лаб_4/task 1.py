# TODO решите задачу

import json

def task () -> float:
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return format(sum([item["score"] * item["weight"] for item in json_data]), '.3f')

print(task())