from tkinter import *
fasdfdsafasdfadfasfasd
# Create the main windowsdafsaddfsadf
root = Tk()fasdsdaffas
root.geometry("400x300")sdafdaffasdfsad
ffsadfsda
# Create a canvas widgetfasdfsdaffsadf
fsad
# Add a vertical scrollbar to the canvassdaf)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvassdafa
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(sadfsad
    scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add widgets to the frame
for i in range(50):
    Label(frame, text=f"Label {i}").pack()

# Run the application
root.mainloop()
