class Cavalier:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur
        self.position = position
        self.chessboard = tableau
    
    def deplacements_possibles(self):
        deplacements = []
        if self.couleur == "w":
            min = 97
            max = 122
        else :
            min = 65
            max = 90
        if self.position[0] - 2 >= 0:
            if self.position[1] - 1 >= 0 and (min<ord(self.chessboard[self.position[0] - 2][self.position[1] - 1])<max or self.chessboard[self.position[0] - 2][self.position[1] - 1] == " " ):
                deplacements.append((self.position[0] - 2, self.position[1] - 1))
            if self.position[1] + 1 <= 7 and (min<ord(self.chessboard[self.position[0] - 2][self.position[1] + 1])<max or self.chessboard[self.position[0] - 2][self.position[1] + 1] == " " ):
                deplacements.append((self.position[0] - 2, self.position[1] + 1))
        if self.position[0] + 2 <= 7:
            if self.position[1] - 1 >= 0 and (min<ord(self.chessboard[self.position[0] + 2][self.position[1] - 1])<max or self.chessboard[self.position[0] + 2][self.position[1] - 1] == " " ):
                deplacements.append((self.position[0] + 2, self.position[1] - 1))
            if self.position[1] + 1 <= 7 and (min<ord(self.chessboard[self.position[0] + 2][self.position[1] + 1])<max or self.chessboard[self.position[0] + 2][self.position[1] + 1] == " " ):
                deplacements.append((self.position[0] + 2, self.position[1] + 1))
        if self.position[1] - 2 >= 0:
            if self.position[0] - 1 >= 0 and (min<ord(self.chessboard[self.position[0] - 1][self.position[1] - 2])<max or self.chessboard[self.position[0] - 1][self.position[1] - 2] == " " ):
                deplacements.append((self.position[0] - 1, self.position[1] - 2))
            if self.position[0] + 1 <= 7 and (min<ord(self.chessboard[self.position[0] + 1][self.position[1] - 2])<max or self.chessboard[self.position[0] + 1][self.position[1] - 2] == " " ):
                 deplacements.append((self.position[0] + 1, self.position[1] - 2))
        if self.position[1] + 2 <= 7:
            if self.position[0] - 1 >= 0 and (min<ord(self.chessboard[self.position[0] - 1][self.position[1] + 2])<max or self.chessboard[self.position[0] - 1][self.position[1] + 2] == " " ):
                deplacements.append((self.position[0] - 1, self.position[1] + 2))
            if self.position[0] + 1 <= 7 and (min<ord(self.chessboard[self.position[0] + 1][self.position[1] + 2])<max or self.chessboard[self.position[0] + 1][self.position[1] + 2] == " " ):
                deplacements.append((self.position[0] + 1, self.position[1] + 2))
        return deplacements