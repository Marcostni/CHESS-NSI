from kivy.uix.button import Button
from pion import Pion 
from cavalier import Cavalier 
from fou import Fou 
from tour import Tour
from dame import Dame 
from roi import Roi 

class ChessGame:
    def __init__(self):
        self.board = [
            ['t', 'c', 'f', 'd', 'r', 'f', 'c', 't'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['T', 'C', 'F', 'D', 'R', 'F', 'C', 'T']
        ]
        self.current_player = "w"
        self.piece = ""
        self.pnts_w = 0
        self.pnts_b = 0
        self.dico = {
            "d": 9,
            "t": 5,
            "f": 3,
            "c": 3,
            "p": 1,
            " ": 0,
            "r": 999999999999
        }

    def make_move(self, depart, arrivee):
        if depart != arrivee:
            self.piece_effacee = self.board[arrivee[0]][arrivee[1]]
            if self.board[arrivee[0]][arrivee[1]].islower():
                self.pnts_w += self.dico[self.board[arrivee[0]][arrivee[1]]]
            else:
                self.pnts_b += self.dico[(self.board[arrivee[0]][arrivee[1]]).lower()]

            self.board[depart[0]][depart[1]], self.board[arrivee[0]][arrivee[1]] = " ", self.board[depart[0]][depart[1]]
        
    def undo_move(self, depart, arrivee):
        if depart != arrivee:
            if self.piece_effacee.islower():
                self.pnts_w -= self.dico[self.piece_effacee]
            else:
                self.pnts_b -= self.dico[(self.piece_effacee).lower()]

            self.board[depart[0]][depart[1]], self.board[arrivee[0]][arrivee[1]] = self.piece_effacee, self.board[depart[0]][depart[1]]
            self.piece_effacee = " "
        
    def find_king(self):
        for lignes in range(len(self.board)):
            if self.current_player == "w":
                if "R" in self.board[lignes]:
                    col = self.board[lignes].index("R")
                    roi = (lignes, col)
            else :
                if "r" in self.board[lignes]:
                    col = self.board[lignes].index("r")
                    roi = (lignes, col)
        return roi
    
    def is_check(self, pos_roi):            
        for lignes in range(len(self.board)):
            for col in range(len(self.board[0])):
                self.coordinates = (lignes, col)
                if self.board[lignes][col].islower() != self.board[pos_roi[0]][pos_roi[1]].islower() and self.board[lignes][col] != " ":
                    if self.current_player == "w":
                        if self.board[lignes][col] == "p":
                            self.piece = Pion("b", self.coordinates, self.board)
                        elif self.board[lignes][col] == "c":
                            self.piece = Cavalier("b", self.coordinates, self.board)
                        elif self.board[lignes][col] == "f":
                            self.piece = Fou("b", self.coordinates, self.board)
                        elif self.board[lignes][col] == "t":
                            self.piece = Tour("b", self.coordinates, self.board)
                        elif self.board[lignes][col] == "d":
                            self.piece = Dame("b", self.coordinates, self.board)
                        elif self.board[lignes][col] == "r":
                            self.piece = Roi("b", self.coordinates, self.board)
                            
                    elif self.current_player == "b":
                        if self.board[lignes][col] == "P":
                            self.piece = Pion("w", self.coordinates, self.board)
                        elif self.board[lignes][col] == "C":
                            self.piece = Cavalier("w", self.coordinates, self.board)
                        elif self.board[lignes][col] == "F":
                            self.piece = Fou("w", self.coordinates, self.board)
                        elif self.board[lignes][col] == "T":
                            self.piece = Tour("w", self.coordinates, self.board)
                        elif self.board[lignes][col] == "D":
                            self.piece = Dame("w", self.coordinates, self.board)
                        elif self.board[lignes][col] == "R":
                            self.piece = Roi("w", self.coordinates, self.board)
                    if pos_roi in self.piece.deplacements_possibles():
                        return True
        return False
    
    def launch_is_check(self, depart, arrivee):
        self.make_move(depart, arrivee)
        verif = self.is_check(arrivee)
        self.undo_move(arrivee, depart)
        return verif
    
    def is_checkmate(self):
        pos_roi = self.find_king()
        if self.is_check(pos_roi):
            roi = Roi(self.current_player, pos_roi, self.board)
            for coordonees in roi.deplacements_possibles():
                print("pos_roi =", coordonees)
                if not self.launch_is_check(pos_roi, coordonees):
                    print("pas mat")
                    return False

            for lignes in range(len(self.board)):
                for col in range(len(self.board[0])):
                    self.coordinates_piece_alliee = (lignes, col)
                    if self.board[lignes][col].islower() == self.board[pos_roi[0]][pos_roi[1]].islower():
                        if self.current_player == "b":
                            if self.board[lignes][col] == "p":
                                self.piece = Pion("b", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "c":
                                self.piece = Cavalier("b", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "f":
                                self.piece = Fou("b", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "t":
                                self.piece = Tour("b", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "d":
                                self.piece = Dame("b", self.coordinates_piece_alliee, self.board)
                                
                        elif self.current_player == "w":
                            if self.board[lignes][col] == "P":
                                self.piece = Pion("w", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "C":
                                self.piece = Cavalier("w", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "F":
                                self.piece = Fou("w", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "T":
                                self.piece = Tour("w", self.coordinates_piece_alliee, self.board)
                            elif self.board[lignes][col] == "D":
                                self.piece = Dame("w", self.coordinates_piece_alliee, self.board)
                                                            
                        if self.piece != "":
                            print("piece en position :", self.coordinates_piece_alliee)
                            for deplacements in self.piece.deplacements_possibles():
                                print(list(deplacements))
                                self.make_move(self.coordinates_piece_alliee, deplacements)
                                if not self.is_check(pos_roi):
                                    print("pas mat")
                                    self.undo_move(deplacements, self.coordinates_piece_alliee)
                                    return False
                                self.undo_move(deplacements, self.coordinates_piece_alliee)
            return True

    def is_pat(self):
        pos_roi = self.find_king()
        if not self.is_check(pos_roi):
            if self.board[pos_roi[0]][pos_roi[1]].islower():
                roi = Roi("b", pos_roi, self.board)
            else:
                roi = Roi("w", pos_roi, self.board)
            deplacements_possibles = roi.deplacements_possibles()
            for deplacements in deplacements_possibles:
                self.make_move(pos_roi, deplacements)
                if not self.is_check(deplacements):
                    self.undo_move(deplacements, pos_roi)
                    return False
                else:
                    self.undo_move(deplacements, pos_roi)
                    
            for lignes in range(len(self.board)):
                    for col in range(len(self.board[0])):
                        self.coordinates_piece_alliee = (lignes, col)
                        if self.board[lignes][col].islower() == self.board[pos_roi[0]][pos_roi[1]].islower():
                            if self.board[lignes][col] == " ":
                                self.piece = False
                            elif self.current_player == "b":
                                if self.board[lignes][col] == "p":
                                    self.piece = Pion("b", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "c":
                                    self.piece = Cavalier("b", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "f":
                                    self.piece = Fou("b", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "t":
                                    self.piece = Tour("b", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "d":
                                    self.piece = Dame("b", self.coordinates_piece_alliee, self.board)
                                    
                            elif self.current_player == "w":
                                if self.board[lignes][col] == "P":
                                    self.piece = Pion("w", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "C":
                                    self.piece = Cavalier("w", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "F":
                                    self.piece = Fou("w", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "T":
                                    self.piece = Tour("w", self.coordinates_piece_alliee, self.board)
                                elif self.board[lignes][col] == "D":
                                    self.piece = Dame("w", self.coordinates_piece_alliee, self.board)
                            
                            if self.piece:
                                for deplacements in self.piece.deplacements_possibles():
                                    self.make_move(self.coordinates_piece_alliee, deplacements)
                                    pos_roi = self.find_king()
                                    if self.is_check(pos_roi):
                                        self.undo_move(deplacements, self.coordinates_piece_alliee)
                                    else:
                                        self.undo_move(deplacements, self.coordinates_piece_alliee)
                                        return False
            return True
