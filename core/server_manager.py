import subprocess
import os
import time
import sys
from config import SERVER_DIR, PYTHON_DIR

class ServerManager:
    def __init__(self):
        self.python_exe = os.path.normpath(os.path.join(PYTHON_DIR, "python.exe"))
        self.server_root = os.path.normpath(os.path.join(SERVER_DIR, "server"))
        self.server_script = os.path.normpath(os.path.join(self.server_root, "server.py"))
        self.stdout_path = os.path.join(SERVER_DIR, "server.out.log")
        self.stderr_path = os.path.join(SERVER_DIR, "server.err.log")

    def is_environment_ready(self) -> bool:
        """Valida se os arquivos necessários existem antes de iniciar."""
        if not os.path.exists(self.python_exe):
            print(f"Erro: Executável Python não encontrado em: {self.python_exe}")
            return False
        if not os.path.exists(self.server_script):
            print(f"Erro: Script do servidor não encontrado em: {self.server_script}")
            return False
        return True

    def _build_injection_command(self) -> str:
        """Cria o comando Python que injeta os paths necessários no runtime."""
        parent_folder = os.path.dirname(self.server_root)
        
        # Usamos f-strings com aspas triplas para facilitar a leitura do comando injetado
        return (
            f"import sys, os; "
            f"sys.path.insert(0, r'{self.server_root}'); "
            f"sys.path.insert(0, r'{parent_folder}'); "
            f"os.chdir(r'{self.server_root}'); "
            f"exec(open(r'{self.server_script}', encoding='utf-8').read())"
        )

    def _get_creation_flags(self) -> int:
        """Retorna flags de criação de processo baseadas no SO."""
        return subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0

    def start(self):
        """Inicia o servidor e retorna o objeto do processo ou None em caso de falha."""
        if not self.is_environment_ready():
            return None

        print("Iniciando servidor de jogo...")
        
        try:
            # Gerenciamento automático de fechamento de arquivos com o 'with' não é possível 
            # aqui pois o Popen precisa dos arquivos abertos enquanto o processo roda.
            out_file = open(self.stdout_path, "w", encoding="utf-8")
            err_file = open(self.stderr_path, "w", encoding="utf-8")

            process = subprocess.Popen(
                [self.python_exe, "-u", "-c", self._build_injection_command()],
                cwd=self.server_root,
                stdout=out_file,
                stderr=err_file,
                creationflags=self._get_creation_flags(),
                shell=False
            )

            return self._verify_process(process)

        except Exception as e:
            print(f"Erro crítico ao disparar o servidor: {e}")
            return None

    def _verify_process(self, process: subprocess.Popen):
        """Aguardar inicialização e verifica se o processo não morreu imediatamente."""
        time.sleep(2.0)
        
        status = process.poll()
        if status is not None:
            print(f"Falha na inicialização. Código de saída: {status}")
            print(f"Verifique os detalhes em: {self.stderr_path}")
            return None

        print(f"Servidor online! (PID: {process.pid})")
        return process
