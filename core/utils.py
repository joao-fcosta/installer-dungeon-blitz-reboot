import os
import urllib.request
import zipfile
import shutil
import subprocess
import shutil

def ensure_base_dir(path):
    os.makedirs(path, exist_ok=True)

def download_file(url, destination):
    print(f"Baixando: {url}")
    urllib.request.urlretrieve(url, destination)
    print("Download concluído.")

def download_and_extract_zip(url, destination):
    print(f"Baixando repositório: {url}")
    zip_path = destination + ".zip"
    urllib.request.urlretrieve(url, zip_path)
    print("Download concluído.")
    
    print("Extraindo repositório...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination)
    
    # Move the extracted folder contents to the destination
    extracted_folder = os.path.join(destination, os.listdir(destination)[0])
    if os.path.isdir(extracted_folder):
        for item in os.listdir(extracted_folder):
            shutil.move(os.path.join(extracted_folder, item), os.path.join(destination, item))
        os.rmdir(extracted_folder)
    
    os.remove(zip_path)
    print("Repositório extraído.")

import shutil

def check_python_installed():
    return bool(shutil.which("py") or shutil.which("python"))

def install_python(python_url):
    print("Python não encontrado. Iniciando instalação...")
    
    installer_path = os.path.join(os.path.expanduser("~"), "python_installer.exe")
    
    try:
        download_file(python_url, installer_path)
        
        print("Instalando Python...")
        subprocess.run([
            installer_path,
            "/quiet",
            "InstallAllUsers=1",
            "PrependPath=1",
            "Include_pip=1"
        ], check=True)
        
        print("Python instalado com sucesso!")
        os.remove(installer_path)
        return True
    except Exception as e:
        print(f"Erro ao instalar Python: {e}")
        if os.path.exists(installer_path):
            os.remove(installer_path)
        return False