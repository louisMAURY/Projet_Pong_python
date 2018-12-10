from tkinter import *

# On crée une fenêtre
fenetre = Tk()

largeur = 500
hauteur = 500
# On dit de faire une toile de 500px de largeur et de 500px de hauteur
canvas = Canvas(fenetre , width = largeur , height = hauteur)
canvas.pack()


def spawn():
    photo = PhotoImage(file = "balle.png")
    canvas.create_image(largeur/2-25 , hauteur/2-25 , anchor = NW , image = photo)
    canvas.pack()

    
label = Label(fenetre , text = "PONG !")
bouton_depart = Button(fenetre , text = "C'est partie !" , command = spawn())
label.pack()
bouton_depart.pack()


# On demande au programme d'afficher la fenêtre
canvas.pack()

fenetre.mainloop()