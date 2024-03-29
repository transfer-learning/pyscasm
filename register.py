from typing import Dict

class Register:
    register_dict: Dict[str, int] = {
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "BP": 14,
        "SP": 15,
    }

    def __init__(self, name: str = "", num: int = -1):
        if num == -1:
            if not name.upper() in Register.register_dict:
                raise Exception(f"{name} is not a valid register name!")
            self.register = name.upper()
        else:
            self.register = [k for k, v in Register.register_dict.items() if v == num][0]

    def num(self) -> int:
        return Register.register_dict[self.register]

    def __repr__(self):
        return self.register

    def __str__(self):
        return self.register
