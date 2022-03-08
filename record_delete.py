import tkinter as tk
from tkinter import messagebox
import os
#importing all necessary modules
def delete():#calling main function
    def cancel():#function for taking cnic as an ID
        Cnic = ins_CNIC.get()
        if len(Cnic) != 13:#length of cnic and all necessary conditions
            messagebox.showerror(title="error", message="please enter CNIC of appropriate length without -")
        elif Cnic.isdigit() == False:
            messagebox.showerror(title="Error", message="CNIC must not contain any alphabets")
        else:
            Cnic = int(Cnic)
            print(Cnic)
            messagebox.showinfo(title="success", message="your CNIC been submitted")
        result = [{}]#an empty list of dictionary to store booking data
        with open('trainrecord.txt', 'r') as file:#opening and reading file in which data is stored
            for line in file:
                if '#####' in line:
                    result.append({})
                else:
                    line = line.split('=')
                    key = line[0]
                    value = line[1]
                    result[-1][key] = value.strip()
        if str(Cnic) not in str(result):
            messagebox.showinfo(title="Error", message="no record found")
        for dicts in result:
            if str(Cnic) in dicts.values():
                messagebox.showinfo(title="ride canceled", message="your ride has been cancelled and 50 percent of your cost will be charged on your next ride")
                continue
            else:
                with open('tempfile.txt', 'a') as tfile:
                    for k, v in dicts.items():
                        tfile.write(str(k) + '=' + str(v) + '\n')
                    tfile.write('#####\n')#storing data in dictionary read from file

        os.remove('trainrecord.txt')#using OS module to delete file and rename other file
        os.rename('tempfile.txt', 'trainrecord.txt')

    cancel_window = tk.Tk()#creating cancel window
    #using different placement methods to lace widgets in desired order
    ins_CNIC = tk.StringVar(cancel_window)
    cancel_window.geometry("144x145")
    cancel_window.config(bg="#0099ff")
    main_title  = tk.Label(cancel_window, text="Enter your CNIC:", font=("Ariel", 10 , 'bold'), bg='#008000', activebackground='#008000')
    main_title.grid(row=0, column=1)
    entry_box = tk.Entry(cancel_window, font=("Ariel", 9 , 'bold'), textvariable= ins_CNIC)
    entry_box.insert(0,"Enter your CNIC:")
    entry_box.grid(row=1, column=1)
    submit_cnic = tk.Button(cancel_window, text="Enter cnic", font=("Ariel", 10, 'bold'), command=lambda :[cancel(),cancel_window.destroy()],bg='#004d80', activebackground='#004d80')
    submit_cnic.grid(row=2, column=1)

    cancel_window.mainloop()#closing main window
