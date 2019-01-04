from tkinter import *
from jeu import *

fenetre = Tk()

#photo = PhotoImage(file = "pong titre.png") # largeur = 383 Hauteur = 150
canvas = Canvas(fenetre , width = 500 , height = 200 , bg = "black")
titre = canvas.create_text(250 , 100 , text = "PONG" , fill = "white" , font = "impact")
#canvas.create_image(58 , 0 , anchor = NW , image = photo)
canvas.pack()

bouton_jouer = Button(fenetre , text = "Jouer" , command = game ).pack(side = LEFT , padx = 4 , pady = 4)
bouton_bonus = Button(fenetre , text = "Bonus")
bouton_bonus.pack(side = RIGHT , padx = 4 , pady = 4)

fenetre.mainloop()