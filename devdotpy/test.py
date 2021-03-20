import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, height=768, width=1366, bg="salmon")
canvas.pack(fill=tk.BOTH, expand=tk.YES)

my_image = tk.PhotoImage(file='/home/biky/Desktop/devdotpy/images/deskdesign.png')
canvas.create_image(500, 300, image=my_image, anchor='center')

button = tk.Button(canvas, text = "CLICK ME")
button.place(relx = 0.5, rely = 0.5, anchor = "center")

root.mainloop()