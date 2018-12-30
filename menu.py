from tkinter import *
import jeu

fenetre = Tk()

photo = PhotoImage(file = "pong titre.png") # largeur = 383 Hauteur = 150
canvas = Canvas(fenetre , width = 500 , height = 200 , bg = "black")
canvas.create_image(58 , 0 , anchor = NW , image = photo)
canvas.pack()

bouton_jouer = Button(fenetre , text = "Jouer" , command = jeu.game()).pack(side = LEFT , padx = 4 , pady = 4)
bouton_bonus = Button(fenetre , text = "Bonus")
bouton_bonus.pack(side = RIGHT , padx = 4 , pady = 4)

fenetre.mainloop()