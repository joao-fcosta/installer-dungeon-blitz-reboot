import os
import urllib.request
import zipfile
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
    
    extracted_folder = os.path.join(destination, os.listdir(destination)[0])
    if os.path.isdir(extracted_folder):
        for item in os.listdir(extracted_folder):
            shutil.move(os.path.join(extracted_folder, item), os.path.join(destination, item))
        os.rmdir(extracted_folder)
    
    os.remove(zip_path)
    print("Repositório extraído.")
