import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Pion:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur
        self.position = position
        self.chessboard = tableau

    def deplacements_possibles(self):
        deplacements = []
        if self.couleur == "w":
            if 97<ord(self.chessboard[self.position[0] - 1][self.position[1] + 1])<122 :
                deplacements.append((self.position[0] - 1, self.position[1] + 1))
            if 97<ord(self.chessboard[self.position[0] - 1][self.position[1] - 1])<122:
                deplacements.append((self.position[0] - 1, self.position[1] - 1))
            if self.position[0] - 1 >= 0 and self.chessboard[self.position[0] - 1][self.position[1]] == " ":
                deplacements.append((self.position[0] - 1, self.position[1]))
            if self.position[0] == 6 and self.chessboard[self.position[0] - 2][self.position[1]] == " ":
                deplacements.append((self.position[0] - 2, self.position[1]))
        
        elif self.couleur == "b":
            if 65<ord(self.chessboard[self.position[0] + 1][self.position[1] + 1])<90 :
                deplacements.append((self.position[0] + 1, self.position[1] + 1))
            if 65<ord(self.chessboard[self.position[0] + 1][self.position[1] - 1])<90:
                deplacements.append((self.position[0] + 1, self.position[1] - 1))
            if self.position[0] + 1 <= 7 and self.chessboard[self.position[0] + 1][self.position[1]] == " ":
                deplacements.append((self.position[0] + 1, self.position[1]))
            if self.position[0] == 1 and self.chessboard[self.position[0] + 2][self.position[1]] == " ":
                deplacements.append((self.position[0] + 2, self.position[1]))

        return deplacements
    
        
    
class ChessGame:
    def __init__(self):
        # Initial board setup
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

    def make_move(self, depart, arrivee):
        self.board[depart[0]][depart[1]], self.board[arrivee[0]][arrivee[1]] = " ", self.board[depart[0]][depart[1]]
        
    def is_checkmate(self):
        pass

class ChessApp(App):
    def build(self):
        self.chess_game = ChessGame()
        self.chessboard = self.root.ids.chessboard
        self.create_chessboard()
        return self.root

    def create_chessboard(self):
        for row in range(8):
            for col in range(8):
                piece = self.chess_game.board[row][col]
                button = Button(text=piece,font_size=32,on_release=self.cell_clicked)
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
                self.possibility = self.chess_game.piece.deplacements_possibles()
                self.position = self.coordinates
                print(self.possibility)
            else :
                pass
        else :
            if self.coordinates in self.possibility:
                self.chess_game.make_move(self.position, self.coordinates)
                self.chessboard.clear_widgets()
                self.create_chessboard()
                self.chess_game.piece = ""
                if self.chess_game.current_player == "w" :
                    self.chess_game.current_player = "b"
                else:
                    self.chess_game.current_player = "w"

    def start_new_game(self):
        # Start a new game
        self.chess_game = ChessGame()
        self.chessboard.clear_widgets()
        self.create_chessboard()

    def leave(self):
        # Exit the game
        App.get_running_app().stop()
    
if __name__ == '__main__':
    ChessApp().run()