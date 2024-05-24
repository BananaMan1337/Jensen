import tkinter as GUI

def drawing(event):
    #even here being the mouse click
    global last_x, last_y
    #global means it can be accessed from anywhere, this gets the last position of the click
    x, y = event.x, event.y
    #draw from last known position to new position
    whiteboard.create_line(last_x, last_y, x, y, width=3)
    #whiteboard drawing 3 px thickness
    last_x, last_y = x, y
    #update last position to new position

window = GUI.Tk()
window.title("Paint")
whiteboard = GUI.Canvas(window, width=500, height=500)
#whiteboard and size
whiteboard.pack()

last_x, last_y = 0, 0
#start position
whiteboard.bind("<B1-Motion>", drawing)
#binds mouse 1 to the function
window.mainloop()