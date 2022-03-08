import tkinter as tk
import updatre
import booking
import record_delete
import timetable_display
#importing all the necessary module made before

window = tk.Tk()#creating main window and resizing and customizing it below
window.geometry("630x540")
window.title("online Train Reservation System")

g = tk.PhotoImage(file="image.png")

# Create Canvas
canvas1 = tk.Canvas(window, width=300,
                 height=400)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=g,
                     anchor="nw")


#creating desired buttons and imbedding respective functions called from modules in them
menu_label = tk.Label(window, text="Main Menu",font=("Ariel",40,'bold'), fg="#00FF00", bg="black"
                   ,compound='top')
menu_label.pack(side='top')
book_a_train_button =tk. Button(window,text="    Book a Ride!    ",bg='#0099ff',font=("Ariel",20,'bold'),
                             compound='top',  command=lambda :[window.wm_state('iconic'), booking.newbooking()])
update_button = tk.Button(window,text="Update booking! ", bg='#0099ff',font=("Ariel",20,'bold'),
                             compound='bottom', command=lambda: [updatre.update(window)])

cancel_button = tk.Button(window,text="    Cancel Ride!     ",bg='#0099ff',font=("Ariel",20,'bold'),
                             command=record_delete.delete)

schedule_button = tk.Button(window,text="  See Schedule!     ", bg='#0099ff',font=("Ariel",20,'bold'),
                             compound='top',command=timetable_display.display)
main_label = canvas1.create_window(195, 15,anchor="nw",window=menu_label)
button1_canvas = canvas1.create_window(195, 130,
                                       anchor="nw",
                                       window=book_a_train_button)

button2_canvas = canvas1.create_window(195, 230,
                                       anchor="nw",
                                       window=update_button)

button3_canvas = canvas1.create_window(195, 330, anchor="nw",
                                       window=cancel_button)
button4_canvas = canvas1.create_window(195, 430, anchor="nw",
                                       window=schedule_button)



window.mainloop()#closing main window