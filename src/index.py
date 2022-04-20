from tkinter import Tk
from ui.ui import UI
#from services.game_service import GameService
#from repositories.player_scores_repository import PlayerScoresRepository


def main():
    window = Tk()
    window.title('Tic Tac Toe')

    #service = GameService(PlayerScoresRepository())

    #user_interface = UI(window, service)
    user_interface = UI(window)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
