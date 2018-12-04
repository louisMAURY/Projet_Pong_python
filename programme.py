from tkinter import *

# On crée une fenêtre
tk = Tk()
# On dit de faire une toile de 500px de largeur et de 500px de hauteur
canvas = Canvas(tk , width = 500 , height = 500)
# On crée un cerlce
cercle = canvas.creat_oval(250 , 250 , 500 , 500)


# On demande au programme d'afficher la fenêtre
canvas.pack()
tk.mainloop()