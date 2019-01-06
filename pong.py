from tkinter import *
import random
import time

# On crée une fenêtre
fenetre = Tk()
# Le titre de la fenetre affichera "Pong"
fenetre.title("Pong")

largeur = 800
hauteur = 500

canvas = Canvas(fenetre , width = largeur , height = hauteur , bd = 0 , highlightthickness = 0 , bg = "black")

titre = canvas.create_text(400 , 225 , text = "PONG" , fill = "white" , font = "impact")

def affichage():
# On demmande d'afficher une "toile" qui suivant plusieurs parametres
    canvas.pack()
    fenetre.update()


start = [-1 , 1]
random.shuffle(start)

class Ball:

    def __init__(self , canvas , raq , jdroit , color):
        affichage()
        self.canvas = canvas
        self.raq = raq
        self.jdroit = jdroit
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
    
    def heurter_joueur_droit(self , pos):
        pos_joueur_droit = self.canvas.coords(self.jdroit.id)
        if pos[3] >= pos_joueur_droit[1] and pos[3] <= pos_joueur_droit[3]:
            if pos[2] >= pos_joueur_droit[0] and pos[0] <= pos_joueur_droit[2]:
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
            self.x = 2
        if self.heurter_joueur_droit(pos) == True:
            self.x = -2

        if pos[0] <= 0:
            self.sortie = True
        if pos[2] >= self.largeur_canevas:
            self.sortie = True


class Raquette:
    def __init__(self , canvas , color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0 , 10 , 100 , fill = color)
        self.canvas.move(self.id , 5 , hauteur/2-50)
        self.y = 0
        self.hauteur_canevas = self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-a>" , self.vers_haut)
        self.canvas.bind_all("<KeyPress-q>" , self.vers_bas)

    def vers_haut(self , evt):
        self.canvas.move(self.id , 0 , -20)
    
    def vers_bas(self , evt):
        self.canvas.move(self.id , 0 , 20)


class Joueur_droit:
    def __init__(self , canvas , color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(largeur-10 , 0 , largeur , 100 , fill = color)
        self.canvas.move(self.id , -5 , hauteur/2-50)
        self.y = 0
        self.hauteur_canevas = self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-Up>" , self.vers_haut)
        self.canvas.bind_all("<KeyPress-Down>" , self.vers_bas)

    def vers_haut(self , evt):
        self.canvas.move(self.id , 0 , -20)
    
    def vers_bas(self , evt):
        self.canvas.move(self.id , 0 , 20)


raq = Raquette(canvas , "white")
jdroit = Joueur_droit(canvas , "white")
balle = Ball(canvas , raq , jdroit , "white")


def game():
    affichage()
    while True:
        if balle.sortie == False:
            balle.dessiner()
        fenetre.update_idletasks()
        fenetre.update()
        time.sleep(0.01)


def bonus():
    pass


bouton_jouer = Button(fenetre , text = "Jouer" , command = game ).pack(padx = 4 , pady = 4)
bouton_bonus = Button(fenetre , text = "Bonus" , command = bonus).pack(padx = 4 , pady = 4)

fenetre.mainloop()