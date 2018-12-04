from tkinter import *

# On crée une fenêtre
fenetre = Tk()
photo = PhotoImage(file = "balle.png")
# On dit de faire une toile de 500px de largeur et de 500px de hauteur
canvas = Canvas(fenetre , width = 500 , height = 500)
canvas.create_image(250 , 250 , anchor = NW , image = photo)
canvas.pack()


# On demande au programme d'afficher la fenêtre
canvas.pack()
fenetre.mainloop()