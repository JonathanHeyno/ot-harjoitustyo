from tkinter import ttk, constants, StringVar
import tkinter as tk


class NewGameView:
    def __init__(self, root, service, show_game_view, show_scores, quit, screen_width, screen_height):
        self._root = root
        self._service = service
        self._show_game_view = show_game_view
        self._show_scores = show_scores
        self._quit = quit
        self._frame_a = None
        self._frame_b = None
        self.board_size = 10
        self.how_many_to_win = 5
        self._ent_board_size = None
        self._ent_how_many_to_win = None
        self._error_variable = None
        self._error_label = None
        self.added_players = []
        self._initialize(screen_width, screen_height)

    def pack(self):
        self._frame_a.pack(fill=tk.Y)
        self._frame_b.pack(fill=tk.BOTH, expand=True)
        #self._frame_b.pack(fill=tk.Y, side=tk.LEFT, expand=True)
        # self._frame_a.pack(fill=constants.X)
        # self._frame_b.pack(fill=constants.X)

    def destroy(self):
        self.board_size = self._ent_board_size.get()
        self.how_many_to_win = self._ent_how_many_to_win.get()
        self._frame_a.destroy()
        self._frame_b.destroy()

    def _initialize(self, screen_width, screen_height):
        self._root.geometry(str(screen_width)+"x"+str(screen_height))
        self._frame_a = ttk.Frame(master=self._root)
        self._frame_a.pack(side=tk.LEFT, fill=tk.Y)

        self._frame_b = ttk.Frame(master=self._root)
        self._frame_b.pack(fill=tk.BOTH, expand=True)
        #self._frame_b.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        start_button = ttk.Button(master=self._frame_a, text="New")
        start_button.pack()
        load_button = ttk.Button(master=self._frame_a, text="Load")
        load_button.pack()
        save_button = ttk.Button(master=self._frame_a, text="Save")
        save_button.pack()
        scores_button = ttk.Button(master=self._frame_a, text="Scores", command=self._show_scores)
        scores_button.pack()
        quit_button = ttk.Button(master=self._frame_a, text="Quit", command = self._quit)
        quit_button.pack()

        lbl_header = ttk.Label(master=self._frame_b,
                               text="New game", font=('Cambria 25'))
        lbl_header.grid(row=0, column=0, columnspan=2, pady=20)
        lbl_board_size = ttk.Label(master=self._frame_b, text="Board size")
        lbl_board_size.grid(row=1, column=0, sticky="w", padx=5)
        self._ent_board_size = ttk.Entry(master=self._frame_b, width=3)
        self._ent_board_size.insert(tk.END, self.board_size)
        self._ent_board_size.grid(row=1, column=1, sticky="w")
        lbl_how_many_to_win = ttk.Label(
            master=self._frame_b, text="How many to win")
        lbl_how_many_to_win.grid(row=2, column=0, sticky="w", padx=5, pady=3)
        self._ent_how_many_to_win = ttk.Entry(master=self._frame_b, width=3)
        self._ent_how_many_to_win.insert(tk.END, self.how_many_to_win)
        self._ent_how_many_to_win.grid(row=2, column=1, sticky="w")

        lbl_players = ttk.Label(master=self._frame_b, text="Players:")
        lbl_players.grid(row=3, column=0, sticky="sw", padx=10, pady=10)

        frame_c = ttk.Frame(master=self._frame_b)
        frame_c.grid(columnspan=10)

        lbl_name = ttk.Label(master=frame_c, text="Player name")
        lbl_name.grid(row=0, column=0, sticky="sw", padx=4, pady=4)
        lbl_algorithm = ttk.Label(master=frame_c, text="Algorithm")
        lbl_algorithm.grid(row=0, column=1, sticky="sw", padx=4, pady=4)
        lbl_difficulty = ttk.Label(master=frame_c, text="Difficulty")
        lbl_difficulty.grid(row=0, column=2, sticky="sw", padx=4, pady=4)
        lbl_symbol = ttk.Label(master=frame_c, text="Symbol")
        lbl_symbol.grid(row=0, column=3, sticky="sw", padx=4, pady=4)

        # list added players
        self._list_added_players(frame_c)
        n = len(self.added_players)

        cbx_player_name = ttk.Combobox(frame_c, width=12)
        cbx_player_name['values'] = self._service.get_all_players_from_db()
        cbx_player_name.grid(row=n+1, column=0, sticky="sw", padx=4, pady=10)
        #cbx_player_name.bind('<<ComboboxSelected>>', self._add_human_player)

        cbx_algorithm = ttk.Combobox(frame_c, width=12)
        cbx_algorithm['values'] = self._service.get_algorithms()
        cbx_algorithm.state(["readonly"])
        cbx_algorithm.grid(row=n+1, column=1, sticky="sw", padx=4, pady=10)

        difficulty = ttk.Scale(frame_c, orient=tk.HORIZONTAL,
                               length=100, from_=0.0, to=100.0)
        difficulty.grid(row=n+1, column=2, sticky="sw", padx=4, pady=10)

        player_symbol = ttk.Entry(frame_c, width=3)
        player_symbol.insert(tk.END, '')
        player_symbol.grid(row=n+1, column=3, sticky="sw", padx=5, pady=10)

        add_button = ttk.Button(master=frame_c, text="add", width=5,
                                command=lambda: self._handle_add(
                                    cbx_player_name.get(),
                                    cbx_algorithm.get(),
                                    difficulty.get(),
                                    player_symbol.get())
                                )
        add_button.grid(row=n+1, column=4, sticky='w', padx=5)

        start_button = ttk.Button(
            master=self._frame_b, text="Start", command=self._handle_start)
        start_button.grid(row=1, column=2, sticky='w', padx=0)

        self._error_variable = StringVar(self._frame_b)
        self._error_label = ttk.Label(
            master=self._frame_b,
            textvariable=self._error_variable,
            foreground='red'
        )
        self._error_label.grid(row=2, column=3, padx=10, pady=5)
        self._hide_error()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _list_added_players(self, frame_c):
        i = 0
        while i < len(self.added_players):
            difficulty = str(int(self.added_players[i][2]))
            if (self.added_players[i][1] == "Human"):
                difficulty = ''

            lbl_name = ttk.Label(master=frame_c, text=self.added_players[i][0])
            lbl_name.grid(row=i+1, column=0, sticky="sw", padx=4, pady=4)
            lbl_algorithm = ttk.Label(
                master=frame_c, text=self.added_players[i][1])
            lbl_algorithm.grid(row=i+1, column=1, sticky="sw", padx=4, pady=4)
            lbl_difficulty = ttk.Label(master=frame_c, text=str(difficulty))
            lbl_difficulty.grid(row=i+1, column=2, sticky="sw", padx=4, pady=4)
            lbl_symbol = ttk.Label(
                master=frame_c, text=self.added_players[i][3])
            lbl_symbol.grid(row=i+1, column=3, sticky="sw", padx=4, pady=4)
            remove_button = ttk.Button(
                master=frame_c, text="remove", width=7, command=lambda i=i: self._handle_remove(i))
            remove_button.grid(row=i+1, column=4, sticky='w', padx=5)
            i += 1

    def _handle_add(self, name, algorithm, difficulty, symbol):
        if not algorithm:
            algorithm = "Human"
        if (symbol):
            self.added_players.append([name, algorithm, difficulty, symbol])
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        self.destroy()
        self._initialize(screen_width, screen_height)

    def _handle_remove(self, i):
        self.added_players.pop(i)
        screen_width = self._root.winfo_width()
        screen_height = self._root.winfo_height()
        self.destroy()
        self._initialize(screen_width, screen_height)

    def _handle_start(self):
        try:
            size = int(self._ent_board_size.get())
            how_many_to_win = int(self._ent_how_many_to_win.get())
            self._service.new_game(size, how_many_to_win)
            for player in self.added_players:
                self._service.add_player(
                    player[0], player[3], player[1], player[2], player[1] == "Human")
            if self._service.number_of_players == 0:
                self._show_error("Invalid input")
            else:
                self._show_game_view()
        except:
            self._show_error("Invalid input")
