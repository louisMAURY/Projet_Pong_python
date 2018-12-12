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

    def __init__(self , canvas , color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(largeur/2-10 , hauteur/2-10 , largeur/2+10 , hauteur/2+10 , fill = color)
        self.canvas.move(self.id , 2 , 2)
        self.x = start[0]
        self.y = start[1]
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()

    
    def dessiner(self):
        self.canvas.move(self.id , self.x , self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.hauteur_canevas:
            self.y = -1
        
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.largeur_canevas:
            self.x = -1

class Raquette:
    def __init__(self , canvas , color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(5, 5 , 10 , 100 , fill = color)
        self.canvas.move(self.id , 200 , 300)
    
    def dessiner(self):
        pass


raq = Raquette(canvas , "white")
balle = Ball(canvas , "white")

while True:
    balle.dessiner()
    raq.dessiner()
    fenetre.update_idletasks()
    fenetre.update()
    time.sleep(0.01)


fenetre.mainloop()