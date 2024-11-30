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

    prefab = random_object()
    reference_prefab = random_object()
    direction = random_direction()
    number = random_num()

    prompt = prompt.replace("object", prefab)
    prompt = prompt.replace("direction", direction)
    prompt = prompt.replace("ref_obj", reference_prefab)
    prompt = prompt.replace("num", number)

    unit = random_unit().rstrip('es').rstrip('s') if "1" in prompt else random_unit()
    prompt = prompt.replace("units", unit)

    with open('dataset/spawn.json', 'r') as file:
        data = json.load(file)

        data['parameters']['prefab'] = prefab
        data['parameters']['reference_object'] = reference_prefab
        data['parameters']['direction'] = direction
        data['parameters']['value'] = number

        formatted_json = json.dumps(data, indent=4)

    return prompt, formatted_json

def get_move():
    prompt = random_move()

    prefab = random_object()
    direction = random_direction()
    number = random_num()

    prompt = prompt.replace("object", prefab)
    prompt = prompt.replace("direction", direction)
    prompt = prompt.replace("num", number)

    unit = random_unit().rstrip('es').rstrip('s') if "1" in prompt else random_unit()
    prompt = prompt.replace("units", unit)

    with open('dataset/move.json', 'r') as file:
        data = json.load(file)

        data['parameters']['prefab'] = prefab
        data['parameters']['direction'] = direction
        data['parameters']['value'] = number

        formatted_json = json.dumps(data, indent=4)

    return prompt, formatted_json

def get_remove():
    prompt = random_remove()

    prefab = random_object()

    prompt = prompt.replace("object", prefab)

    with open('dataset/remove.json', 'r') as file:
        data = json.load(file)

        data['parameters']['prefab'] = prefab

        formatted_json = json.dumps(data, indent=4)

    return prompt, formatted_json

def get_rotate():
    prompt = random_rotate()

    prefab = random_object()
    axis = random_axis()
    degrees = random_degrees()

    prompt = prompt.replace("object", prefab)
    prompt = prompt.replace("axs", axis)
    prompt = prompt.replace("num", degrees)

    with open('dataset/rotate.json', 'r') as file:
        data = json.load(file)

        data['parameters']['prefab'] = prefab
        data['parameters']['axis'] = axis
        data['parameters']['value'] = degrees

        formatted_json = json.dumps(data, indent=4)

    return prompt, formatted_json

def get_replace():
    prompt = random_replace()

    prefab = random_object()
    object_to_replace = random_object()

    prompt = prompt.replace("object", prefab)
    prompt = prompt.replace("rep_obj", object_to_replace)

    with open('dataset/replace.json', 'r') as file:
        data = json.load(file)

        data['parameters']['prefab'] = prefab
        data['parameters']['object_to_replace'] = object_to_replace

        formatted_json = json.dumps(data, indent=4)

    return prompt, formatted_json
