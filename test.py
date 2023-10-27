from tkinter import *

root = Tk()
root.geometry("950x600")

# create canvas
canvas = Canvas(root, width=932, height=600, borderwidth=0, highlightthickness=0, bg="black")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
# create a scrollbar
f=Frame(canvas)#1
canvas.grid()
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))#2
canvas.create_window((0,0),anchor='nw',window=f,width=932)#3
vsb.grid(row=0, column=1, sticky='ns')
# Test the ability to scroll
for x in range(300):
    Label(f, text="test").grid(row=x)

root.mainloop()