from tkinter import ttk, constants, StringVar
import tkinter as tk

class LoadView:
    """load_view näkymä
    """
    def __init__(self, root, service, show_game_view, show_new_game_view, show_save_view, show_scores_view, quit, screen_width, screen_height):
        """luokan konstruktori

        Args:
            root: tkinter root
            service: GameService, pelin rajapinta
            show_game_view: näyttää pelinäkymän
            show_new_game_view : näyttää new_game näkymän
            show_save_view: näyttää new_game näkymän
            show_scores_view: näyttää pistetilannenäkymän
            quit: metodi lopettaa ohjelman
            screen_width: ikkunan leveys
            screen_height: ikkunan korkeus
        """
        self._root = root
        self._quit = quit
        self._service = service
        self._show_game_view = show_game_view
        self._show_new_game_view = show_new_game_view
        self._show_save_view = show_save_view
        self._show_scores_view = show_scores_view
        self._error_variable = None
        self._error_label = None
        self._frame_a = None
        self._frame_b = None
        self._initialize(screen_width, screen_height)

    def pack(self):
        self._frame_a.pack(fill = tk.Y)
        self._frame_b.pack(fill=tk.BOTH, expand=True)


    def destroy(self):
        self._frame_a.destroy()
        self._frame_b.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_save_text_box(self):
        pad = 4

        lbl_scores = ttk.Label(master = self._frame_b, text="Load", font=('Cambria 25'))
        lbl_scores.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        lbl_name = ttk.Label(master = self._frame_b, text='Name of save file:')
        lbl_name.grid(row = 1, column = 1, padx=pad, pady=10)

        cbx_file_name = ttk.Combobox(self._frame_b, width=20)
        cbx_file_name['values'] = self._service.get_save_files()
        cbx_file_name.grid(row=2, column=1, sticky="sw", padx=4, pady=10)

        save_button = ttk.Button(
            master=self._frame_b, text="Load", command=lambda: self._handle_load(cbx_file_name.get()))
        save_button.grid(row=2, column=2, sticky='w', padx=0)

        
    def _handle_load(self, filename):
        try:
            self._service.load(filename)
            self._show_game_view()
        except ValueError:
            self._show_error("File not found")

    def _initialize(self, screen_width, screen_height):
        self._root.geometry(str(screen_width)+"x"+str(screen_height))

        self._frame_a = ttk.Frame(master=self._root)
        self._frame_a.pack(side=tk.LEFT, fill = tk.Y)

        self._frame_b = ttk.Frame(master=self._root, width=200, height=100)
        self._frame_b.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        start_button = ttk.Button(master=self._frame_a, text="New", command=self._show_new_game_view)
        start_button.pack()
        load_button = ttk.Button(master=self._frame_a, text="Load")
        load_button.pack()
        save_button = ttk.Button(master=self._frame_a, text="Save", command = self._show_save_view)
        save_button.pack()
        scores_button = ttk.Button(master=self._frame_a, text="Scores", command = self._show_scores_view)
        scores_button.pack()
        quit_button = ttk.Button(master=self._frame_a, text="Quit", command = self._quit)
        quit_button.pack()

        self._initialize_save_text_box()

        self._error_variable = StringVar(self._frame_b)
        self._error_label = ttk.Label(
            master=self._frame_b,
            textvariable=self._error_variable,
            foreground='red'
        )
        self._error_label.grid(row=3, column=2, padx=10, pady=5)
        self._hide_error()
