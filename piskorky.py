import tkinter as tk

# rozmery hracej plochy
VYSKA = 600
SIRKA = 800
STVOREC=50

# pole na ukladanie hry
m = SIRKA//STVOREC
n = VYSKA//STVOREC
pole = [[0 for j in range(n)] for i in range(m)]
# hodnoty 
KRUH = 1
KRIZIK = 2
posledny_tah=KRUH

# nakreslí červený kruh na mieste kliknutia
def kruh(x,y):
    canvas.create_oval(x+2, y+2, x+STVOREC-2, y+STVOREC-2, outline="red", width=3)

# nakreslí modry kruh na mieste kliknutia
def krizik(x,y):
    canvas.create_line( x+2, y+2, x+STVOREC-2, y+STVOREC-2, width=3, fill="blue")
    canvas.create_line( x+STVOREC-2, y+2, x+2, y+STVOREC-2, width=3, fill="blue")
     
#obsluzenie laveho tlacidla
def lavy_klik(event):
    #celociselne delenie
    global posledny_tah
    x = event.x//STVOREC
    y = event.y//STVOREC
    # ak je pole prazdne
    if( pole[x][y]==0):
        # na tahuje KRIZIK
        if (posledny_tah==KRUH):
            krizik(x*STVOREC, y*STVOREC)
            pole[x][y]=KRIZIK
            posledny_tah=KRIZIK
        # na tahuje KRUH
        else:
            kruh(x*STVOREC, y*STVOREC)
            pole[x][y]=KRUH
            posledny_tah=KRUH
    
### CANVAS
root = tk.Tk()
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, bg="white")
# zvisle ciary
for x in range(0,SIRKA,STVOREC):
       canvas.create_line( x, 0, x, VYSKA, width=3) 
# vodorovne ciary
for y in range(0,VYSKA,STVOREC):
       canvas.create_line( 0, y, SIRKA, y, width=3) 
canvas.pack()


# priradenie funkcie lavy_klik k udalosti kliknutia lavym tlacidlom <Button-1>
canvas.bind("<Button-1>", lavy_klik) 
root.mainloop()