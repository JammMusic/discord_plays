import pyautogui
from time import sleep
from typing import Optional

BUTTON_MAP = {
    "u": "up",
    "up": "up",
    "d": "down",
    "down": "down",
    "l": "left",
    "left": "left",
    "r": "right",
    "right": "right",
    "a": "x",
    "b": "z",
    "x": "s",
    "y": "a",
    "lb": "q",
    "rb": "w",
    "start": "return",
    "select": "tab",
}

def filter(input: str) -> Optional[str]:
    normalized = input.lower().strip()

    if normalized in BUTTON_MAP:
        return BUTTON_MAP[normalized]
    else:
        return None

def press_button(button: str) -> None:
    pyautogui.keyDown(button)
    sleep(0.1)
    pyautogui.keyUp(button)