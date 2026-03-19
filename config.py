import os
import sys

BASE_DIR = os.path.dirname(sys.executable)

# URLs de Download
GAME_URL = "http://localhost/p/cbv/DungeonBlitz.swf?fv=cbq&gv=cbv"
FLASH_URL = "https://github.com/Grubsic/Adobe-Flash-Player-Debug-Downloads-Archive/raw/main/Windows/flashplayer_32_sa.exe"
SERVER_URL = "https://github.com/minesa-org/dungeon-blitz-reboot/archive/refs/heads/main.zip"
PYTHON_URL = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-amd64.zip"
GITHUB_API_URL = "https://api.github.com/repos/minesa-org/dungeon-blitz-reboot/branches/main"

# Estrutura de Pastas (Tudo relativo à pasta do EXE)
FLASH_DIR = os.path.join(BASE_DIR, "flashplayer.exe")
SERVER_DIR = os.path.join(BASE_DIR, "server")
PYTHON_DIR = os.path.join(BASE_DIR, "python")
VERSION_FILE_DIR = os.path.join(BASE_DIR, "version.json")