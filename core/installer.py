import os
from config import BASE_DIR, FLASH_URL, REPO_ZIP_URL, FLASH_PATH, SERVER_DIR, PYTHON_URL
from core.utils import ensure_base_dir, download_file, download_and_extract_zip, check_python_installed, install_python

def is_installed():
    return os.path.exists(FLASH_PATH) and os.path.exists(SERVER_DIR)

def install():
    print("Iniciando instalação...")

    # Verificar e instalar Python se necessário
    if not check_python_installed():
        if not install_python(PYTHON_URL):
            print("Erro: Python é necessário para continuar.")
            return

    ensure_base_dir(BASE_DIR)

    if not os.path.exists(FLASH_PATH):
        download_file(FLASH_URL, FLASH_PATH)

    if not os.path.exists(SERVER_DIR):
        ensure_base_dir(SERVER_DIR)
        download_and_extract_zip(REPO_ZIP_URL, SERVER_DIR)

    print("Instalação concluída.")