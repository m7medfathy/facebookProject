from tkinter import *sgdsfgdsfgsgdfsgsdgfsgdsfgdsgf
gsdfgsdfdsfgsdgdfsgdsfgdf
# Create the main windowgsdfgdsgdsfgsdsdfgdsfgdsgdsgdsfg
root = Tk()dfsgsdgfsgdsgdsgdsgdsgdfsgdgs
root.geometry("400x300")s

# Create a canvas widget
canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a vertical scrollbar to the canvas
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add widgets to the frame
for i in range(50):
    Label(frame, text=f"Label {i}").pack()

# Run the application
root.mainloop()
