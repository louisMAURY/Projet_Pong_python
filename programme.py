from tkinter import *
import random
import time

# On crée une fenêtre
fenetre = Tk()
# Le titre de la fenetre affichera "Pong"
fenetre.title("Pong")

largeur = 1000
hauteur = 500

# On dit de faire une toile de 500px de largeur et de 500px de hauteur
canvas = Canvas(fenetre , width = largeur , height = hauteur , bd = 0 , highlightthickness = 0 , bg = "black")
canvas.pack()
fenetre.update()

start = [-1 , 1]
random.shuffle(start)

class Ball:

    def __init__(self , canvas , raq , color):
        self.canvas = canvas
        self.raq = raq
        self.id = canvas.create_rectangle(largeur/2-10 , hauteur/2-10 , largeur/2+10 , hauteur/2+10 , fill = color)
        self.canvas.move(self.id , 2 , 2)
        self.x = start[0]
        self.y = start[1]
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()
        self.sortie = False
    
    def heurter_raquette(self , pos):
        pos_raquette = self.canvas.coords(self.raq.id)
        if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
            if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
                return True
        return False

    
    def dessiner(self):
        self.canvas.move(self.id , self.x , self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.hauteur_canevas:
            self.y = -1

        if self.heurter_raquette(pos) == True:
            self.x += 2
            self.y += 2

        if pos[0] <= 0:
            self.sortie = True
        if pos[2] >= self.largeur_canevas:
            self.sortie = True

class Raquette:
    def __init__(self , canvas , color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0 , 10 , 100 , fill = color)
        self.canvas.move(self.id , 5 , 5)
        self.y = 0
        self.hauteur_canevas = self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-Up>" , self.vers_haut)
        self.canvas.bind_all("<KeyPress-Down>" , self.vers_bas)

    def vers_haut(self , evt):
        self.canvas.move(self.id , 0 , 20)
    
    def vers_bas(self , evt):
        self.canvas.move(self.id , 0 , -20)
    
    def dessiner(self):
        self.canvas.move(self.id , 0 , self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        elif pos[3] >= self.hauteur_canevas:
            self.y = 0


raq = Raquette(canvas , "white")
balle = Ball(canvas , raq , "white")

while True:
    if balle.sortie == False:
        balle.dessiner()
        raq.dessiner()
    fenetre.update_idletasks()
    fenetre.update()
    time.sleep(0.01)


fenetre.mainloop()