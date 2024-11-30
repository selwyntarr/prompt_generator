from random_picker import *
import json

def get_json(action):
    try:
        with open(f"dataset/{action}.json", "r") as file:
            file_content = file.read()
            data = json.loads(file_content)
            formatted_json = json.dumps(data, indent=4)
            return formatted_json
    except FileNotFoundError:
        print(f"File not found: dataset/{action}.json")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.") 

def get_spawn():
    prompt = random_spawn()

    prompt = prompt.replace("object", random_object())
    prompt = prompt.replace("direction", random_direction())
    prompt = prompt.replace("ref_obj", random_object())
    prompt = prompt.replace("num", random_num())

    unit = random_unit().rstrip('es').rstrip('s') if "1" in prompt else random_unit()
    prompt = prompt.replace("units", unit)

    return prompt

def get_remove():
    prompt = random_remove()
    prompt = prompt.replace("object", random_object())

    return prompt