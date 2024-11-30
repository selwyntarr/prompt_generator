import random

def random_num():
    return str(random.randint(1, 9))

def random_degrees():
    return str(random.randint(0, 360))

def random_unit():
    units = ["units"]
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

def random_axis():
    try:
        with open("dataset/axis.txt", "r") as file:
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
    
def random_move():
    try:
        with open("dataset/move.txt", "r") as file:
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

def random_rotate():
    try:
        with open("dataset/rotate.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if lines:
                return random.choice(lines).strip()
            else:
                return None
    except FileNotFoundError:
        return "missing"

def random_replace():
    try:
        with open("dataset/replace.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if lines:
                return random.choice(lines).strip()
            else:
                return None
    except FileNotFoundError:
        return "missing"


