class Roi:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur
        self.position = position
        self.chessboard = tableau

    def deplacements_possibles(self):
        deplacements = []

         def deplacements_possibles(self):
        deplacements = []
        x = self.position[0]
        y = self.position[1]

        if x > 0:
            deplacements.append((x-1, y))
        
        # bas
        if x < 7:
            deplacements.append((x+1, y))
        
        # gauche
        if y > 0:
            deplacements.append((x, y-1))
        
        # droite
        if y < 7:
            deplacements.append((x, y+1))
        
        # haut gauche
        if x > 0 and y > 0:
            deplacements.append((x-1, y-1))
        
        # haut droite
        if x > 0 and y < 7:
            deplacements.append((x-1, y+1))
        
        # bas gauche
        if x < 7 and y > 0:
            deplacements.append((x+1, y-1))
        
        # bas droite
        if x < 7 and y < 7:
            deplacements.append((x+1, y+1))
        
        return deplacements
