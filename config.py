import os

BASE_DIR = r"C:\DungeonBlitz"

FLASH_URL = "https://github.com/Grubsic/Adobe-Flash-Player-Debug-Downloads-Archive/raw/main/Windows/flashplayer_32_sa.exe"
REPO_ZIP_URL = "https://github.com/minesa-org/dungeon-blitz-reboot/archive/refs/heads/main.zip"
PYTHON_URL = "https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe"

FLASH_PATH = os.path.join(BASE_DIR, "flashplayer.exe")
SERVER_DIR = os.path.join(BASE_DIR, "server")

GAME_URL = "http://localhost/p/cbv/DungeonBlitz.swf?fv=cbq&gv=cbv"

SERVER_PORT = 80