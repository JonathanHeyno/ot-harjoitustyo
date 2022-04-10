from ui.game_view import GameView
from ui.newgame_view import NewGameView


class UI:

    def __init__(self, root, service):
        self._root = root
        self._current_view = None
        self._service = service

    def start(self):
        self._show_new_game_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_game(self):
        self._show_game_view()

    def _handle_new_game(self):
        self._show_new_game_view()

    def _show_game_view(self):
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        self._hide_current_view()

        self._current_view = GameView(
            self._root,
            self._service,
            self._show_new_game_view,
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

        self._current_view = GameView(
            self._root,
            self._service,
            self._show_new_game_view,
            screen_width,
            screen_height
        )

        self._current_view.pack()

    def _show_new_game_view(self):
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        if screen_width == 1 and screen_height == 1:
            screen_width = 500
            screen_height = 450
        self._hide_current_view()

        self._current_view = NewGameView(
            self._root,
            self._service,
            self._show_game_view,
            screen_width,
            screen_height
        )

        self._current_view.pack()
