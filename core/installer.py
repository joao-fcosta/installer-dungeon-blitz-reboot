import os
from config import BASE_DIR, FLASH_URL, SERVER_URL, FLASH_DIR, SERVER_DIR, PYTHON_URL, PYTHON_DIR
from core.utils import ensure_base_dir, download_file, download_and_extract_zip

def is_installed():
    return os.path.exists(FLASH_DIR) and os.path.exists(SERVER_DIR) and os.path.exists(PYTHON_DIR)

def enable_site_packages(python_dir):
    for file in os.listdir(python_dir):
        if file.endswith("._pth"):
            pth = os.path.join(python_dir, file)
            with open(pth, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "import site" not in content:
                with open(pth, "a", encoding="utf-8") as f:
                    f.write("\nimport site\n")

def install():
    print("Iniciando instalação...")
    ensure_base_dir(BASE_DIR)

    if not os.path.exists(PYTHON_DIR):
        ensure_base_dir(PYTHON_DIR)
        download_and_extract_zip(PYTHON_URL, PYTHON_DIR)
        enable_site_packages(PYTHON_DIR)

    if not os.path.exists(FLASH_DIR):
        download_file(FLASH_URL, FLASH_DIR)

    if not os.path.exists(SERVER_DIR):
        ensure_base_dir(SERVER_DIR)
        download_and_extract_zip(SERVER_URL, SERVER_DIR)

    print("Instalação concluída.")