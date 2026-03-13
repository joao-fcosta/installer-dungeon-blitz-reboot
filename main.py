from core.installer import is_installed, install
from core.server_manager import start_server
from core.launcher import start_game


def run():
    if not is_installed():
        install()

    server = start_server()
    flash = start_game()

    if flash:
        flash.wait()

    if server:
        server.terminate()

    print("Servidor encerrado.")


if __name__ == "__main__":
    run()