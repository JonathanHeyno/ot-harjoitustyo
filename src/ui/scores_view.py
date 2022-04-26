from tkinter import ttk, constants, StringVar
import tkinter as tk

class ScoresView:
    def __init__(self, root, service, show_new_game_view, show_save_view, show_load_view, quit, screen_width, screen_height):
        self._root = root
        self._quit = quit
        self._service = service
        self._show_new_game_view = show_new_game_view
        self._show_save_view = show_save_view
        self._show_load_view = show_load_view
        self._frame_a = None
        self._frame_b = None
        self._ent_board_size = None
        self._ent_how_many_to_win = None
        self._initialize(screen_width, screen_height)

    def pack(self):
        self._frame_a.pack(fill = tk.Y)
        self._frame_b.pack(fill=tk.BOTH, expand=True)


    def destroy(self):
        self._frame_a.destroy()
        self._frame_b.destroy()


    def _initialize_score_list(self):
        pad = 4

        lbl_scores = ttk.Label(master = self._frame_b, text="Scores", font=('Cambria 25'))
        lbl_scores.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        header_text = f"{'Name':{pad}} {'Wins':{pad}}{'Losses':{pad}}{'Ties':{pad}}"
        lbl_name = ttk.Label(master = self._frame_b, text='Name')
        lbl_name.grid(row = 1, column = 0, padx=pad, pady=10)
        lbl_name = ttk.Label(master = self._frame_b, text='Wins')
        lbl_name.grid(row = 1, column = 1, padx=pad, pady=10)
        lbl_name = ttk.Label(master = self._frame_b, text='Losses')
        lbl_name.grid(row = 1, column = 2, padx=pad, pady=10)
        lbl_name = ttk.Label(master = self._frame_b, text='Ties')
        lbl_name.grid(row = 1, column = 3, padx=pad, pady=10)

        scores = self._service.get_scores()
        i = 2
        for score in scores:
            label_1 = ttk.Label(master=self._frame_b, text=score[0])
            label_1.grid(row = i, column = 0, padx=pad)
            label_2 = ttk.Label(master=self._frame_b, text=score[1])
            label_2.grid(row = i, column = 1, padx=pad)
            label_3 = ttk.Label(master=self._frame_b, text=score[2])
            label_3.grid(row = i, column = 2, padx=pad)
            label_4 = ttk.Label(master=self._frame_b, text=score[3])
            label_4.grid(row = i, column = 3, padx=pad)
            i += 1

        


    def _initialize(self, screen_width, screen_height):
        self._root.geometry(str(screen_width)+"x"+str(screen_height))

        self._frame_a = ttk.Frame(master=self._root)
        self._frame_a.pack(side=tk.LEFT, fill = tk.Y)

        self._frame_b = ttk.Frame(master=self._root, width=200, height=100)
        self._frame_b.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        start_button = ttk.Button(master=self._frame_a, text="New", command=self._show_new_game_view)
        start_button.pack()
        load_button = ttk.Button(master=self._frame_a, text="Load", command=self._show_load_view)
        load_button.pack()
        save_button = ttk.Button(master=self._frame_a, text="Save", command = self._show_save_view)
        save_button.pack()
        scores_button = ttk.Button(master=self._frame_a, text="Scores")
        scores_button.pack()
        quit_button = ttk.Button(master=self._frame_a, text="Quit", command = self._quit)
        quit_button.pack()


        

        self._initialize_score_list()
