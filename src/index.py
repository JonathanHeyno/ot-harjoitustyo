from tkinter import Tk
from ui.ui import UI
from services.game_service import GameService


def main():
    window = Tk()
    window.title('Tic Tac Toe')

    service = GameService()

    user_interface = UI(window, service)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()

# BUGIT: DIFFICULTY EI TOIMI. SE EI TEE MITAAN
