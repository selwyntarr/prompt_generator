import random

def random_num():
    return str(random.randint(1, 9))

def random_unit():
    units = ["units", "meters", "inches"]
    return random.choice(units)

def random_object():
    try:
        with open("dataset/objects.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if lines:
                return random.choice(lines).strip()
            else:
                return None
    except FileNotFoundError:
        return "missing"

def random_direction():
    try:
        with open("dataset/directions.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if lines:
                return random.choice(lines).strip()
            else:
                return None
    except FileNotFoundError:
        return "missing"

def random_spawn():
    try:
        with open("dataset/spawn.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if lines:
                return random.choice(lines).strip()
            else:
                return None
    except FileNotFoundError:
        return "missing"

def random_remove():
    try:
        with open("dataset/remove.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if lines:
                return random.choice(lines).strip()
            else:
                return None
    except FileNotFoundError:
        return "missing"


