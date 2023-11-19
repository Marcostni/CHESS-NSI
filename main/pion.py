class Pion:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur
        self.position = position
        self.chessboard = tableau

    def deplacements_possibles(self):
        deplacements = []
        if self.couleur == "w":
            if self.position[1] + 1 <= 7:
                if 97<ord(self.chessboard[self.position[0] - 1][self.position[1] + 1])<122 :
                    deplacements.append((self.position[0] - 1, self.position[1] + 1))
            if self.position[1] - 1 >= 0:
                if 97<ord(self.chessboard[self.position[0] - 1][self.position[1] - 1])<122:
                    deplacements.append((self.position[0] - 1, self.position[1] - 1))
            if self.position[0] - 1 >= 0 and self.chessboard[self.position[0] - 1][self.position[1]] == " ":
                deplacements.append((self.position[0] - 1, self.position[1]))
            if self.position[0] == 6 and self.chessboard[self.position[0] - 2][self.position[1]] == " ":
                deplacements.append((self.position[0] - 2, self.position[1]))
        
        elif self.couleur == "b":
            if self.position[1] + 1 <= 7:
                if 65<ord(self.chessboard[self.position[0] + 1][self.position[1] + 1])<90 :
                    deplacements.append((self.position[0] + 1, self.position[1] + 1))
            if self.position[1] - 1 >= 0:
                if 65<ord(self.chessboard[self.position[0] + 1][self.position[1] - 1])<90:
                    deplacements.append((self.position[0] + 1, self.position[1] - 1))
            if self.position[0] + 1 <= 7 and self.chessboard[self.position[0] + 1][self.position[1]] == " ":
                deplacements.append((self.position[0] + 1, self.position[1]))
            if self.position[0] == 1 and self.chessboard[self.position[0] + 2][self.position[1]] == " ":
                deplacements.append((self.position[0] + 2, self.position[1]))

        return deplacements