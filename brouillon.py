def spawn():
    photo = PhotoImage(file = "balle.png")
    canvas.create_image(largeur/2-25 , hauteur/2-25 , anchor = NW , image = photo)
    canvas.pack()

    
label = Label(fenetre , text = "PONG !")
bouton_depart = Button(fenetre , text = "C'est parti !" , command = spawn())
label.pack()
bouton_depart.pack()