class Fou:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur 
        self.position = position
        self.chessboard = tableau 

    def deplacemements_possibles(self):
           deplacements = []
        x, y = self.position

        i = 1
        while x - i >= 0 and y - i >= 0:
            deplacements.append((x - i, y - i))
            i += 1
        i = 1
        while x - i >= 0 and y + i < len(self.chessboard):
            deplacements.append((x - i, y + i))
            i += 1
        i = 1
        while x + i < len(self.chessboard) and y - i >= 0:
            deplacements.append((x + i, y - i))
            i += 1
        i = 1
        while x + i < len(self.chessboard) and y + i < len(self.chessboard):
            deplacements.append((x + i, y + i))
            i += 1

        return deplacements
    
