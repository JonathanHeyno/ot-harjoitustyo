from pathlib import Path
from entities.game import Game
from entities.player import Player
from entities.algorithm_manager import AlgorithmManager
from repositories.player_scores_repository import (
    score_repository as default_score_repository
)
from config import SAVE_FILE_PATH
from config import os


class GameService():
    """Luokka joka hallinnoi peliä ja tarjoaa rajapinnan käyttöliittymälle

    Attributes:
        score_repository: tietokanta johon tallennetaan voittotilastot
        number_of_players: pelaajien määrä
        board: pelilauta
        size: pelilaudan koko
        game_is_over: tieto onko peli ohi
        game_is_won: tieto onko joku voittanut
        winner_symbol: voittajapelaajan symboli
        turn_symbol: vuorossa olevan pelaajan symboli
    """

    def __init__(self, score_repository=default_score_repository):
        """luokan konstruktori

        Args:
            score_repository: tietokanta johon tallennetaan voittotilastot.
        """

        self._player_score_repository = score_repository
        self.players = []
        self.player_symbols = []
        self.turn = 0
        self.__number_of_players = 0
        self._winner = -1
        self.game = None

    @property
    def number_of_players(self):
        return self.__number_of_players

    @property
    def board(self):
        return self.game.board

    @property
    def size(self):
        return self.game.size

    @property
    def game_is_over(self):
        return self.game.is_over

    @property
    def game_is_won(self):
        return self.game.is_won

    @property
    def winner_symbol(self):
        if self._winner >= 0:
            return self.player_symbols[self._winner]
        return ''

    @property
    def turn_symbol(self):
        if self.game_is_over:
            return ''
        return self.player_symbols[self.turn]

    def new_game(self, size, how_many_to_win):
        """alustaa ja aloittaa uuden pelin

        Args:
            size: pelilaudan koko
            how_many_to_win: montako pitää saada riviin voittoon

        Raises:
            ValueError: voittoon tarvittavan rivin on mahduttava laudalle
        """
        if how_many_to_win > size or how_many_to_win < 0:
            raise ValueError
        self.turn = 0
        self.__number_of_players = 0
        self.players = []
        self.player_symbols = []
        self.game = Game(size, how_many_to_win)
        self._winner = -1

    def add_player(self, name, symbol, str_algorithm, difficulty=0, is_human=True):
        """lisää pelaajan peliin

        Args:
            name: pelaajan nimi_
            symbol: pelaajan symboli laudalla
            str_algorithm: algoritmi jonka perusteella pelaaja päättää liikkeen
            difficulty: algoritmin vaikeusaste.
            is_human: boolean, onko pelaaja ihminen.
        """
        algorithms = AlgorithmManager()
        algorithm = algorithms.select_algorithm(str_algorithm, difficulty)
        self.players.append(Player(name, symbol, algorithm, str_algorithm, difficulty, is_human))
        self.player_symbols.append(symbol)
        self.game.player_symbols = self.player_symbols
        self.__number_of_players += 1
        if is_human:
            self._player_score_repository.add_player(name)

    def _handle_game_over(self):
        """tarkastaa onko peli ohi ja päivittää tiedot
        """
        if self.game.is_over and self.game.is_won:
            self._winner = self.turn
            for i in range(self.__number_of_players):
                #if self.players[i].is_human and i == self._winner:
                if (self.players[i].is_human
                    and self.player_symbols[i] == self.player_symbols[self._winner]):
                    self._player_score_repository.update_score(self.players[i].name, 1, 0, 0)
                elif self.players[i].is_human:
                    self._player_score_repository.update_score(self.players[i].name, 0, 1, 0)
        elif self.game_is_over:
            for i in range(self.__number_of_players):
                if self.players[i].is_human:
                    self._player_score_repository.update_score(self.players[i].name, 0, 0, 1)

    def add_move_and_get_updates(self, i):
        """lisää seuraavan siirron annettuun ruutuun ja hakee seuraavien tietokonepelaajien siirrot

        Args:
            i: ruudun numero

        Returns:
            lista tpleista joissa ruutujen numerot ja symbolit jotka seuraavaksi pelattiin
        """
        if not self.game.move_is_allowed((i//self.size), (i % self.size)):
            return []
        moves = []
        self.game.add_move((i//self.size), (i % self.size),
                           self.player_symbols[self.turn])
        moves.append((i, self.player_symbols[self.turn]))
        self._handle_game_over()
        self.turn = (self.turn + 1) % self.__number_of_players
        while not self.players[self.turn].is_human and not self.game.is_over:
            choice = self.players[self.turn].next_move(self.game)
            self.game.add_move(choice[0], choice[1], choice[2])
            moves.append(
                ((choice[0]*self.size + choice[1]), choice[2]))
            self._handle_game_over()
            self.turn = (self.turn + 1) % self.__number_of_players
        return moves

    def make_computer_moves_and_get_updates(self):
        """suorittaa tietokonepelaajien siirtoja kunnes tulee ihmispelaajan vuoro tai peli on ohi

        Returns:
           lista tpleista joissa ruutujen numerot ja symbolit jotka seuraavaksi pelattiin
        """
        moves = []

        while not self.players[self.turn].is_human and not self.game.is_over:
            choice = self.players[self.turn].next_move(self.game)

            self.game.add_move(choice[0], choice[1], choice[2])
            moves.append(((choice[0]*self.size + choice[1]), choice[2]))
            self._handle_game_over()
            self.turn = (self.turn + 1) % self.__number_of_players
        return moves

    def get_winning_row(self):
        """hakee voittavan rivin

        Returns:
            lista jossa voittavan rivin ruutujen numerot
        """
        winners_as_numbers = []
        winners = self.game.get_winning_row()
        for winner in winners:
            winners_as_numbers.append(winner[0]*self.size + winner[1])
        return winners_as_numbers

    def get_all_players_from_db(self):
        """hakee voittotietokannassa olevien pelaajien nimet

        Returns:
            lista voittotietokannassa olevien pelaajien nimistä
        """
        return self._player_score_repository.get_names()

    def get_algorithms(self):
        """hakee käytössä olevat algoritmit

        Returns:
            lista käytössä olevista algoritmeista
        """
        algorithms = AlgorithmManager()
        return list(algorithms.list_all())

    def get_scores(self):
        """hakee voittotietokannasta tilastot

        Returns:
            lista tietokannassa olevien pelaajien voitoista, tappioista ja tasapeleistä
        """
        return self._player_score_repository.get_scores()

    def get_save_files(self):
        """hakee telletuskansiosta tallennettujen pelien tiedostojen nimet

        Returns:
            lista tallennettujen pelien tiedostojen nimistä ilman tiedostopäätteitä
        """
        files = []
        for file in os.listdir(SAVE_FILE_PATH):
            if file.endswith(".txt"):
                files.append(file[:-4])
        return files

    def save(self, filename):
        """tallentaa pelin

        Args:
            filename: tallennustiedoston nimi
        """
        filepath = SAVE_FILE_PATH+filename+".txt"
        if self.__number_of_players > 0:
            save_string = str(self.game.size)+"§"+str(self.game.how_many_to_win)
            save_string += "§"+str(int(self.game.is_over))+"§"+str(int(self.game.is_won))
            save_string += "§"+str(self._winner)+"§"+str(self.turn)
            save_string += "§"+str(self.__number_of_players)
            for i in range(self.__number_of_players):
                save_string += "§"+ self.players[i].name
                save_string += "§"+ self.players[i].symbol
                save_string += "§"+ self.players[i].str_algorithm
                save_string += "§"+ str(self.players[i].difficulty)
                save_string += "§"+ str(int(self.players[i].is_human))
            for j in range(self.game.size*self.game.size):
                save_string += "§" + str(self.game.board[j//self.game.size][j % self.game.size])

        Path(filepath).touch()

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(save_string)

    def load(self, filename):
        """lataa tallennetun pelin tiedostosta

        Args:
            filename: tallennetun pelin tiedostonimi

        Raises:
            ValueError: jos tiedostoa ei löydy annetulla nimellä
        """
        filepath = SAVE_FILE_PATH+filename+".txt"
        if not Path(filepath).is_file():
            raise ValueError
        parts = []
        with open(filepath, encoding='utf-8') as file:
            parts = file.read().split('§')

        self.new_game(int(parts[0]), int(parts[1]))

        self._winner= int(parts[4])
        self.turn = int(parts[5])
        self.__number_of_players = 0
        for i in range(int(parts[6])):
            self.add_player(parts[7+i*5], parts[8+i*5], parts[9+i*5],
            float(parts[10+i*5]), parts[11+i*5]==str(1))
        for j in range(int(parts[0])*int(parts[0])):
            if parts[7+5*self.__number_of_players+j]:
                self.game.add_move((j//self.size), (j % self.size),
                parts[7+5*self.__number_of_players+j])

        if parts[2] == str(1):
            self.game.is_over= True
        if parts[3] == str(1):
            self.game.is_won= True
        self.make_computer_moves_and_get_updates()

game_service = GameService()
