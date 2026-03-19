import requests
import json
import os
from config import SERVER_URL, SERVER_DIR, GITHUB_API_URL ,VERSION_FILE_DIR
from core.utils import download_and_extract_zip

def check_for_updates():
    print("Verificando se há atualizações para o servidor...")
    
    if not os.path.exists(VERSION_FILE_DIR):
        return
    
    remote_sha = get_remote_version()
    local_sha = get_local_version()

    if not remote_sha:
        print("Pulando atualização (sem conexão com GitHub).")
        return

    if remote_sha != local_sha:
        print("Nova atualização encontrada! Baixando servidor...")
        
        download_and_extract_zip(SERVER_URL, SERVER_DIR)
        
        save_local_version(remote_sha)
        print("Servidor atualizado com sucesso.")
    else:
        print("O servidor já está na versão mais recente.")

def get_remote_version():
    """Busca o SHA do último commit no GitHub."""
    try:
        response = requests.get(GITHUB_API_URL, timeout=5)
        if response.status_code == 200:
            return response.json()['commit']['sha']
    except Exception as e:
        print(f"Não foi possível checar atualizações: {e}")
    return None

def get_local_version():
    """Lê a versão salva localmente."""
    if os.path.exists(VERSION_FILE_DIR):
        with open(VERSION_FILE_DIR, "r") as f:
            data = json.load(f)
            return data.get("version")
    return None

def save_local_version(sha):
    with open(VERSION_FILE_DIR, "w") as f:
        json.dump({"version": sha}, f)