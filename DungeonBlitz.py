from core.installer import is_installed, install
from core.server_manager import ServerManager
from core.launcher import start_game
from core.updater import check_for_updates


def run():
    if not is_installed():
        install()

    check_for_updates()
    
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