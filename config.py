import os

BASE_DIR = r"C:\DungeonBlitz"

FLASH_URL = "https://github.com/Grubsic/Adobe-Flash-Player-Debug-Downloads-Archive/raw/main/Windows/flashplayer_32_sa.exe"
SERVER_URL = "https://github.com/minesa-org/dungeon-blitz-reboot/archive/refs/heads/main.zip"
PYTHON_URL = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-amd64.zip"

FLASH_DIR = os.path.join(BASE_DIR, "flashplayer.exe")
SERVER_DIR = os.path.join(BASE_DIR, "server")
PYTHON_DIR = os.path.join(BASE_DIR, "python")

GAME_URL = "http://localhost/p/cbv/DungeonBlitz.swf?fv=cbq&gv=cbv"
