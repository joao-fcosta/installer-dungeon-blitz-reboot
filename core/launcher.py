import subprocess
import time
import ctypes
from config import FLASH_PATH, GAME_URL


def _send_ctrl_f():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # ctrl down
    ctypes.windll.user32.keybd_event(0x46, 0, 0, 0)  # f down
    ctypes.windll.user32.keybd_event(0x46, 0, 2, 0)  # f up
    ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # ctrl up


def start_game():
    print("Abrindo jogo...")
    proc = subprocess.Popen([
        FLASH_PATH,
        GAME_URL
    ])
    # aguarda um pouco para a janela ser criada e ganhe foco
    time.sleep(1)
    try:
        _send_ctrl_f()
    except Exception:
        pass
    return proc