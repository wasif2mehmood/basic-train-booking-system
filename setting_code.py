import tkinter as tk
timewindow=tk.Tk()
timewindow.geometry("1025x325")
timewindow.config(bg="#004d80")
time_window_title = tk.Label(timewindow,text="Choose timings", font=('calibre', 25, 'bold'), bg='#008000')
time_window_title.grid(row=0, column=0, pady= 5)

label=tk.Label(timewindow,text=f'Enter continue to proceed with this time  OR select any time from below ',font=('calibre', 10, 'bold'),height=2)
label.grid(row=1,column=0)
button = tk.Button(timewindow,text='continue',font=('calibre', 15, 'bold'), bg='#004d80', activebackground='#004d80' )
button.grid(row=1, column=1, pady=0)
buttonquit = tk.Button(timewindow, text='quit', command=quit, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
buttonquit.grid(row=1, column=2)


available_timings_label = tk.Label(timewindow,text="Available timings:", font=('calibre', 15, 'bold'))
available_timings_label.grid(row=3, column=0, padx=0, pady=0)

available_timings_listbox = tk.Listbox(timewindow,
                                               bg="#f7ffde",
                                               font=("Ariel",16),
                                               )

available_timings_listbox.insert(0, "a very very long string")
available_timings_listbox.insert(1, 'a very very long string')
available_timings_listbox.insert(2, 'a very very long long long long string')
available_timings_listbox.insert(3, 'a very very long string')
available_timings_listbox.insert(4, 'a very very long string')


available_timings_listbox.grid(row=3,column=1)
available_timings_listbox.config(height= 0, width= 0)
Sumbit_timings_button = tk.Button(timewindow,text="submit",font=('Ariel',15), bg='#004d80', activebackground='#004d80' )
Sumbit_timings_button.grid(row=5, column=1, padx=0, pady=0, )
buttonquit.grid(row=6, column=1)
timewindow.mainloop()