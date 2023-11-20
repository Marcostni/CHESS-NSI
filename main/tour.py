class Tour:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur
        self.position = position
        self.chessboard = tableau

    def deplacements_possibles(self):
        deplacements = []

        for i in range(self.position[0] - 1, -1, -1):
            if self.chessboard[i][self.position[1]] == " ":
                deplacements.append((i, self.position[1]))
            elif self.chessboard[i][self.position[1]].islower() != self.couleur.islower():
                deplacements.append((i, self.position[1]))
                break
            else:
                break
              
        for i in range(self.position[0] + 1, 8):
            if self.chessboard[i][self.position[1]] == " ":
                deplacements.append((i, self.position[1]))
            elif self.chessboard[i][self.position[1]].islower() != self.couleur.islower():
                deplacements.append((i, self.position[1]))
                break
            else:
                break

        for j in range(self.position[1] - 1, -1, -1):
            if self.chessboard[self.position[0]][j] == " ":
                deplacements.append((self.position[0], j))
            elif self.chessboard[self.position[0]][j].islower() != self.couleur.islower():
                deplacements.append((self.position[0], j))
                break
            else:
                break

        for j in range(self.position[1] + 1, 8):
            if self.chessboard[self.position[0]][j] == " ":
                deplacements.append((self.position[0], j))
            elif self.chessboard[self.position[0]][j].islower() != self.couleur.islower():
                deplacements.append((self.position[0], j))
                break
            else:
                break

        return deplacements
