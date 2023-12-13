import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from pion import Pion 
from cavalier import Cavalier 
from fou import Fou 
from tour import Tour
from dame import Dame 
from roi import Roi 
from chessgame import ChessGame

class ChessApp(App):
    
    def build(self):
        self.chess_game = ChessGame()
        self.chessboard = self.root.ids.chessboard
        self.label = self.root.ids.label
        self.dico = {
            "p" : "ressources/bpion",
            "P" : "ressources/wpion", 
            "f" : "ressources/bfou",
            "F" : "ressources/wfou",
            "c" : "ressources/bcavalier",
            "C" : "ressources/wcavalier",
            "t" : "ressources/btour",
            "T" : "ressources/wtour",
            "d" : "ressources/bdame",
            "D" : "ressources/wdame",
            "r" : "ressources/broi",
            "R" : "ressources/wroi",
            " " : "ressources/"
        }
        self.create_chessboard()
        return self.root

    def create_chessboard(self):
        
        for row in range(8):
            for col in range(8):
                piece = self.chess_game.board[row][col]
                image = self.dico[piece]
                if (col + row) % 2 == 0:
                    image += "w.png"
                else :
                    image += "b.png"
                button = Button(x = row, y = col, text=piece,font_size=32,color = [255,0,4,0],on_release=self.cell_clicked, background_normal = image)
                self.chessboard.add_widget(button)

    def cell_clicked(self, instance):

        self.letter = instance.text

        for row in range(8):
            for col in range(8):
                button = self.chessboard.children[row * 8 + col]
                if button is instance:
                    self.coordinates = (7 - row,7 - col)
                    break
        
        print(self.coordinates)
        
        if self.chess_game.piece == "":
            if (65<ord(self.letter)<90 and self.chess_game.current_player == "w") or (97<ord(self.letter)<122 and self.chess_game.current_player == "b"):

                if self.letter == "p":
                    self.chess_game.piece = Pion("b", self.coordinates, self.chess_game.board)
                elif self.letter == "P":
                    self.chess_game.piece = Pion("w", self.coordinates, self.chess_game.board)
                elif self.letter == "c":
                    self.chess_game.piece = Cavalier("b", self.coordinates, self.chess_game.board)
                elif self.letter == "C":
                    self.chess_game.piece = Cavalier("w", self.coordinates, self.chess_game.board)
                elif self.letter == "f":
                    self.chess_game.piece = Fou("b", self.coordinates, self.chess_game.board)
                elif self.letter == "F":
                    self.chess_game.piece = Fou("w", self.coordinates, self.chess_game.board)
                elif self.letter == "t":
                    self.chess_game.piece = Tour("b", self.coordinates, self.chess_game.board)
                elif self.letter == "T":
                    self.chess_game.piece = Tour("w", self.coordinates, self.chess_game.board)
                elif self.letter == "d":
                    self.chess_game.piece = Dame("b", self.coordinates, self.chess_game.board)
                elif self.letter == "D":
                    self.chess_game.piece = Dame("w", self.coordinates, self.chess_game.board)
                elif self.letter == "r":
                    self.chess_game.piece = Roi("b", self.coordinates, self.chess_game.board)
                elif self.letter == "R":
                    self.chess_game.piece = Roi("w", self.coordinates, self.chess_game.board)
                self.possibility = self.chess_game.piece.deplacements_possibles()
                self.position = self.coordinates
                print(self.possibility)                
            
        else :
            
            if self.coordinates in self.possibility:
                self.chess_game.make_move(self.position, self.coordinates)
                pos_roi = self.chess_game.find_king()
                if not self.chess_game.is_check(pos_roi):
                    self.chessboard.clear_widgets()
                    self.create_chessboard()
                    if self.chess_game.current_player == "w" :
                        self.chess_game.current_player = "b"
                        self.label.text = "C'est aux noirs de jouer"
                    else:
                        self.chess_game.current_player = "w"
                        self.label.text = "C'est aux blancs de jouer"
                    if self.chess_game.is_checkmate():
                        print("checkmate")
                        if self.chess_game.current_player == "w" :
                            self.label.text = "Echec et mat. Les noirs ont gagné."
                        else:
                            self.label.text = "Echec et mat. Les blancs ont gagné."
                else :
                    self.chess_game.undo_moove(self.coordinates, self.position)
                
            self.chess_game.piece = ""

    def start_new_game(self):
        self.chess_game = ChessGame()
        self.chessboard.clear_widgets()
        self.create_chessboard()
        self.label.text = "C'est aux blancs de jouer"

    def leave(self):
        App.get_running_app().stop()
    
if __name__ == '__main__':
    ChessApp().run()
