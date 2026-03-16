from core.installer import is_installed, install
from core.server_manager import ServerManager
from core.launcher import start_game


def run():
    if not is_installed():
        install()

    manager = ServerManager()
    server_process = manager.start()
    
    flash = start_game()

    if flash:
        flash.wait()

    if server_process:
        server_process.terminate()

    print("Servidor encerrado.")


if __name__ == "__main__":
    run()