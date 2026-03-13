import subprocess
import os
import time
import traceback
from config import SERVER_DIR

def locate_python_executable():
    local_path = os.path.join(os.getcwd(), "python_runtime", "python.exe")
    if os.path.exists(local_path):
        return local_path
    return None

def find_server_script():
    for root, dirs, files in os.walk(SERVER_DIR):
        if "server.py" in files:
            return os.path.normpath(os.path.join(root, "server.py")), os.path.normpath(root)
    return None, None

def start_server():
    print("Verificando ambiente do servidor...")
    
    python_exe = locate_python_executable()
    if not python_exe:
        print("Erro: Python não encontrado.")
        return None

    server_path, server_cwd = find_server_script()
    if not server_path:
        return None

    current_folder = os.path.abspath(server_cwd)
    parent_folder = os.path.dirname(current_folder)

    script_comando = (
        f"import sys; "
        f"sys.path.insert(0, r'{current_folder}'); "
        f"sys.path.insert(0, r'{parent_folder}'); "
        f"import os; os.chdir(r'{current_folder}'); "
        f"exec(open(r'{server_path}', encoding='utf-8').read())"
    )

    try:
        stdout_log = open(os.path.join(SERVER_DIR, "server.out.log"), "w", encoding="utf-8")
        stderr_log = open(os.path.join(SERVER_DIR, "server.err.log"), "w", encoding="utf-8")

        proc = subprocess.Popen(
            [python_exe, "-u", "-c", script_comando], # Usamos o -c para injetar o caminho
            cwd=server_cwd,
            stdout=stdout_log,
            stderr=stderr_log,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0,
            shell=False
        )

        time.sleep(2.0)
        if proc.poll() is not None:
            print(f"O servidor fechou (Código: {proc.returncode}). Verifique o log!")
            return None

        print(f"Servidor iniciado com sucesso (PID: {proc.pid})")
        return proc

    except Exception:
        print(f"Erro: {traceback.format_exc()}")
        return None