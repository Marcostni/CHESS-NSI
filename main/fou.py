class Fou:
    def __init__(self, couleur, position, tableau):
        self.couleur = couleur 
        self.position = position
        self.chessboard = tableau 

    def deplacemements_possibles(self):
        
        deplacements = []
        x, y = self.position

        if self.couleur == "w":
            min = 97
            max = 122
        else :
            min = 65
            max = 90
            
        no = 1
        while (x - no >= 0 and y - no >= 0) and self.chessboard[x-no][y-no] == " ":
            deplacements.append((x - no, y - no))
            no += 1
        if min <= ord(self.chessboard[x-no][y-no]) <= max :
            deplacements.append((x - no, y - no))
            
        ne = 1
        while (x - ne >= 0 and y + ne < len(self.chessboard)) and self.chessboard[x-ne][y-ne] == " ":
            deplacements.append((x - ne, y + ne))
            ne += 1
        if min <= ord(self.chessboard[x-ne][y+ne]) <= max :
            deplacements.append((x - ne, y + ne))
        
        so = 1
        while x + so < len(self.chessboard) and y - so >= 0:
            deplacements.append((x + so, y - so))
            so += 1
        if min <= ord(self.chessboard[x+so][y-so]) <= max :
            deplacements.append((x + so, y - so))
        
        se = 1
        while x + se < len(self.chessboard) and y + se < len(self.chessboard):
            deplacements.append((x + se, y + se))
            se += 1
        if min <= ord(self.chessboard[x+se][y+se]) <= max :
            deplacements.append((x + se, y + se))

        return deplacements
