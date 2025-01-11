# Disappearing Text Writing App

from tkinter import *

key_pressed = True
timer = 0
get_last = ""
limit = 5


# Resets the countdown to text deletion
def set_true():
    global key_pressed, timer, get_last
    key_pressed = True
    timer = 0
    get_last = text_entry.get('1.0', END)


# Prints what's currently in the text entry
def save_writing():
    global get_last
    get_last = text_entry.get('1.0', END)
    print(get_last)


# Text gets deleted after (limit) seconds of inactivity
def start_countdown():
    global key_pressed, timer, get_last, limit
    key_pressed = False
    timer += 1
    timer_label.config(text=timer)
    timer_label.pack()
    if timer >= limit:
        text_entry.delete('1.0', END)
        timer = 0
    if text_entry.get('1.0', END) != get_last:
        set_true()
    window.after(1000, start_countdown)


window = Tk()
window.title("Disappearing Text App")
window.minsize(400, 600)
window.config(padx=20, pady=20)

text_entry = Text(height=25, width=60)
text_entry.focus()
text_entry.pack()

timer_label = Label(text=timer)

save_button = Button(text="Press to save writing", command=save_writing)
save_button.pack()

window.after(1000, start_countdown)

window.mainloop()
