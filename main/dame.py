class Dame:
    
    def __init__(self, couleur, position, tableau):
        
        self.couleur = couleur 
        self.position = position
        self.chessboard = tableau 

    def deplacements_possibles(self):
        from fou import Fou
        from tour import Tour
        fou_dep = Fou(self.couleur, self.position, self.chessboard).deplacements_possibles()
        tour_dep = Tour(self.couleur, self.position, self.chessboard).deplacements_possibles()

        deplacements = fou_dep + tour_dep
        return deplacements
