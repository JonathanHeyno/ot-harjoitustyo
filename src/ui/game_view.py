from tkinter import ttk, constants, StringVar
import tkinter as tk


class GameView:
    """Pelin näkymä
    """
    def __init__(self, root, service, handle_show_new_game_view, show_save_view, show_load_view, show_scores, quit, screen_width, screen_height):
        """luokan konstruktori

        Args:
            root: tkinter root
            service: game service, rajapinta peliiin
            handle_show_new_game_view: asettaa new_game näkymän
            show_save_view: asettaa save_game näkymän
            show_load_view: asettaa load_game näkymän
            show_scores: asettaa show_scores näkymän
            quit: metodi lopettaa ohjelman
            screen_width: ikkunan leveys
            screen_height: ikkunban korkeus
        """
        self._root = root
        self._handle_show_new_game_view = handle_show_new_game_view
        self._show_save_view = show_save_view
        self._show_load_view = show_load_view
        self._show_scores = show_scores
        self._quit = quit
        self._frame_a = None
        self._frame_b = None
        self._game_over_label = None
        self._winner_label = None
        self._winner_symbol_label = None
        self._winner_symbol_variable = None
        self._turn_label = None
        self._turn_symbol_variable = None
        self._turn_symbol_label = None
        self._service = service
        self._buttons = []
        self._winner_style = ttk.Style()
        self._winner_style.configure('winners.TButton', background='green')
        self._previous_move_style = ttk.Style()
        self._previous_move_style.configure(
            'previous.TButton', background='red')
        self._previous_moves = []
        self._initialize(screen_width, screen_height)

    def pack(self):
        self._frame_a.pack(side=tk.LEFT, fill=tk.Y)
        self._frame_b.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def _handle_game_is_over(self):
        if self._service.game_is_over:
            self._game_over_label.pack()
            self._turn_label.pack_forget()
            self._turn_symbol_label.pack_forget()
        if self._service.game_is_won:
            self._winner_label.pack()
            self._winner_symbol_label.pack()
            self._winner_symbol_variable.set(self._service.winner_symbol)
            numbers = self._service.get_winning_row()
            for number in numbers:
                self._buttons[number]["style"] = 'winners.TButton'

    def _handle_button_click(self, i):
        moves = self._service.add_move_and_get_updates(i)
        self._turn_symbol_variable.set(self._service.turn_symbol)
        for previous_move in self._previous_moves:
            self._buttons[previous_move[0]]["style"] = ''

        self._previous_moves = moves
        for move, symbol in moves:
            self._buttons[move]["text"] = symbol
            if move != i:
                self._buttons[move]["style"] = 'previous.TButton'

        self._handle_game_is_over()

    def make_computer_moves(self):
        """hakee GameServiceltä tietokoneen siirrot ja asettaa ne näkyviin
        """
        moves = self._service.make_computer_moves_and_get_updates()
        self._turn_symbol_variable.set(self._service.turn_symbol)
        for previous_move in self._previous_moves:
            self._buttons[previous_move[0]]["style"] = ''
        self._previous_moves = moves
        for move, symbol in moves:
            self._buttons[move]["text"] = symbol
            self._buttons[move]["style"] = 'previous.TButton'
        self._handle_game_is_over()

    def destroy(self):
        self._frame_a.destroy()
        self._frame_b.destroy()

    def _initialize(self, screen_width, screen_height):
        self._root.geometry(str(screen_width)+"x"+str(screen_height))
        self._frame_a = ttk.Frame(master=self._root)
        self._frame_a.pack(side=tk.LEFT, fill=tk.Y)
        self._frame_b = ttk.Frame(master=self._root, width=200, height=100)
        self._frame_b.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        start_button = ttk.Button(
            master=self._frame_a, text="New", command=self._handle_show_new_game_view)
        start_button.pack()
        load_button = ttk.Button(master=self._frame_a, text="Load", command=self._show_load_view)
        load_button.pack()
        save_button = ttk.Button(master=self._frame_a, text="Save", command=self._show_save_view)
        save_button.pack()
        scores_button = ttk.Button(master=self._frame_a, text="Scores", command=self._show_scores)
        scores_button.pack()
        quit_button = ttk.Button(master=self._frame_a, text="Quit", command=self._quit)
        quit_button.pack()

        self._game_over_label = ttk.Label(
            master=self._frame_a,
            text='Game is over',
            foreground='red'
        )
        self._game_over_label.pack()
        self._game_over_label.pack_forget()

        self._winner_label = ttk.Label(
            master=self._frame_a,
            text='Winner:',
        )
        self._winner_label.pack()
        self._winner_label.pack_forget()

        self._winner_symbol_variable = StringVar(self._frame_a)
        self._winner_symbol_label = ttk.Label(
            master=self._frame_a,
            textvariable=self._winner_symbol_variable,
        )
        self._winner_symbol_label.pack()
        self._winner_symbol_label.pack_forget()

        self._turn_label = ttk.Label(
            master=self._frame_a,
            text='Turn:',
        )
        self._turn_label.pack()

        self._turn_symbol_variable = StringVar(self._frame_a)
        self._turn_symbol_label = ttk.Label(
            master=self._frame_a,
            textvariable=self._turn_symbol_variable,
        )
        self._turn_symbol_label.pack()

        size = self._service.size

        for i in range(size*size):
            button = ttk.Button(
                master=self._frame_b,
                text=self._service.board[i//size][i % size],
                command=lambda i=i: self._handle_button_click(i)
            )

            button.grid(row=i//size, column=i % size,
                        sticky=(constants.E, constants.W, constants.N, constants.S))
            self._buttons.append(button)

        for j in range(size):
            self._frame_b.columnconfigure(j, weight=1)
            self._frame_b.rowconfigure(j, weight=1)
        self.make_computer_moves()
