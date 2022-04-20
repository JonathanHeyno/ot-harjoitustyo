from ui.game_view import GameView
from ui.newgame_view import NewGameView
from ui.scores_view import ScoresView
from services.game_service import game_service


class UI:

    #def __init__(self, root, service):
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._service = game_service

    def start(self):
        self._show_scores_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_game(self):
        self._show_game_view()

    def _handle_new_game(self):
        self._show_new_game_view()

    def _handle_scores(self):
        self._show_scores_view()

    def _show_game_view(self):
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        self._hide_current_view()

        self._current_view = GameView(
            self._root,
            self._service,
            self._show_new_game_view,
            self._show_scores_view,
            self._quit,
            screen_width,
            screen_height
        )

        self._current_view.pack()

    def _show_scores_view(self):
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        if screen_width == 1 and screen_height == 1:
            screen_width = 450
            screen_height = 200

        self._hide_current_view()

        self._current_view = ScoresView(
            self._root,
            self._service,
            self._show_new_game_view,
            self._quit,
            screen_width,
            screen_height
        )

        self._current_view.pack()

    def _show_new_game_view(self):
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        if screen_width < 550 and screen_height < 350:
            screen_width = 550
            screen_height = 350
        self._hide_current_view()

        self._current_view = NewGameView(
            self._root,
            self._service,
            self._show_game_view,
            self._show_scores_view,
            self._quit,
            screen_width,
            screen_height
        )

        self._current_view.pack()

    def _quit(self):
        self._root.destroy()