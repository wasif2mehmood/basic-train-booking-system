import tkinter as tk
from tkinter import messagebox
import datetime
#all modules required
# Creating global_instances firstly
date_entered = 0
CNIC = 0
dob = 0
birthday = 0
name = 0
departure_city = 0
destination_city = 0
seats = 0
ride_class = 0

def newbooking():
    ### All Function for taking name and other credentials required ###
    def Name_Submission():
        global  name
        name = name_variable.get()
        if name.isalpha() == False :
            messagebox.showerror(title="Error", message="Please enter only alphabets")
        else:
            messagebox.showinfo(title="success", message="your name has been submitted")
            print(name)

    def CNIC_Submission():
        global CNIC
        CNIC = CNIC_variable.get()
        if len(CNIC) != 13:
            messagebox.showerror(title="error", message="please enter CNIC of appropriate length without -")
        elif CNIC.isdigit() == False :
            messagebox.showerror(title="Error", message="CNIC must not contain any alphabets")
        else:
            CNIC = int(CNIC)
            print(CNIC)
            messagebox.showinfo(title="success", message="your CNIC been submitted")

    def Dept_Submission():
        global departure_city
        departure_city = dep_listbox.get(dep_listbox.curselection())
        print(departure_city)
        messagebox.showinfo(title="success", message="your dept has been submitted")


    def Dest_Submission():
        global destination_city
        destination_city = dest_listbox.get(dest_listbox.curselection())
        if departure_city == destination_city:
            messagebox.showerror("Error", "Departure and Destination City cannot be same")
        else:
            print(destination_city)
            messagebox.showinfo(title="success", message="your destination city has been submitted")
    def Date_of_Birth_Submission():
        global age,birthday
        try:
            filter = Dob_variable.get()
            filter = filter.split('-')
            is_digit = 0
            for index in range(0, len(filter)):
                if filter[index].isdigit():
                    filter[index] = int(filter[index])
                    is_digit += 1
                else:
                    messagebox.showerror("error", "please enter in correct format YYYY-MM-DD")
            global dob
            if is_digit == len(filter):
                dob = list(filter)
                print(dob)
            # Arranging Date of birth in an order
            birthday = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
            if int(dob[0])<1900 or int(dob[0])>2022:
                messagebox.showerror("error", "please enter year after 1900 or before 2022")
            else:
                today_date = datetime.date.today()
                age = today_date - birthday
                age = age.total_seconds()
                birthday = birthday.strftime('%A,%d %B,%Y')
                messagebox.showinfo('info',f'your date of birth is {birthday}')
        except:
            messagebox.showerror("error", "please enter valid year,month,days in range")




    def seat_submission():
        global seats
        seat_filter = No_of_Seats_variable.get()
        if seat_filter.isdigit():
            seats = int(seat_filter)
            print(seats)
        else:
            messagebox.showerror("error", "please enter only integers")

    def type_of_seat_selection():
        global ride_class
        ride_class = Seat_type_listbox.get(Seat_type_listbox.curselection())
        print(ride_class)
        global rides
        rides = {'economy seat': 0, 'economy berth': 100, 'ac business': 4300, 'ac standard': 2200, 'ac sleeper': 6200}
        ride_class = ride_class.lower()
        global additional_cost
        additional_cost = rides[ride_class]
        print(additional_cost, 'Rs will be charged Additional')
        additional_cost = additional_cost


    def date_selection():
        try:
            filter = sel_date.get()
            filter = filter.split('-')
            is_digit = 0
            for index in range(0,len(filter)):
                if filter[index].isdigit():
                    filter[index] = int(filter[index])
                    is_digit += 1
                else:
                    messagebox.showerror("error","please enter in correct format YY-MM-DD")
                    break
            if int(filter[1]) > 12 or int(filter[2]) > 31:
                messagebox.showerror("error", "There can only be 12 months and 31 days")


            else:
                if is_digit == len(filter):
                    global date
                    date = list(filter)
                print(date)

            today_date = datetime.date.today()
            global date_entered,month_number, day_number
            month_number = int(date[1])
            day_number = int(date[2])
            date_entered = datetime.date(2022, month_number, day_number)
            print(date_entered)
            global date_difference
            date_difference = date_entered - today_date
            date_difference = date_difference.total_seconds()
            if date_difference > 604800.0 :
                messagebox.showerror("error","you can only book 7 days in advance")
            elif  date_difference < 0:
                messagebox.showerror('error', "Please dont enter past dates")
            else:
                global final_date
                final_date = date_entered.strftime('%A,%d %B,%Y')
                messagebox.showinfo('date',f'You have selected {final_date}  as your Departure Date')
        except:
            messagebox.showerror('error', "Please enter valid month and date in range")
    def time_selection():
        try:
            time_filter = sel_time.get()
            time_filter = time_filter.split('-')
            is_digit = 0
            for index in range(0,len(time_filter)):
                if time_filter[index].isdigit():
                    time_filter[index] = int(time_filter[index])
                    is_digit += 1
                else:
                    messagebox.showerror("error", "please enter in correct format HH-MM")
            if is_digit == len(time_filter):
                time_list = list(time_filter)
                print(time_list)
            time = list(time_filter)
            global hours_of_time,minutes_of_time
            global month_number, day_number
            hours_of_time = int(time[0])
            minutes_of_time = int(time[1])
            global user_prefered_time
            user_prefered_time = datetime.datetime(2022,month_number,day_number,hours_of_time,minutes_of_time)
            print(user_prefered_time)
        except:
            messagebox.showerror('error', "Please valid hours and minutes in range and enter date first")

    def timfun():#main function for tking time from user and displaying his suitable time
        booking_details_main_window.iconify()
        global first_time,second_time,third_time,fourth_time,train_number,train_cost,finalized_time
        timewindow = tk.Tk()#creating and customizing time window
        timewindow.geometry("1025x325")
        timewindow.config(bg="#004d80")
        time_window_title = tk.Label(timewindow, text="Choose timings", font=('calibre', 25, 'bold'), bg='#008000')
        time_window_title.grid(row=0, column=0, pady=5)
        def t1():
            global finalized_time,first_time
            finalized_time=first_time
            print(finalized_time)
            messagebox.showinfo('info',f'you have selected {first_time} as your departure time ')
            save_record(finalized_time)
        def t2():
            global finalized_time, second_time
            finalized_time = second_time
            print(finalized_time)
            messagebox.showinfo('info', f'you have selected {second_time} as your departure time ')
            save_record(finalized_time)
        def t3():
            global finalized_time, third_time
            finalized_time = third_time
            print(finalized_time)
            messagebox.showinfo('info', f'you have selected {third_time} as your departure time ')
            save_record(finalized_time)
        def t4():
            global finalized_time, fourth_time
            finalized_time = fourth_time
            print(finalized_time)
            messagebox.showinfo('info', f'you have selected {fourth_time} as your departure time ')
            save_record(finalized_time)
        def input_of_time():
            import datetime
            global user_prefered_time
            user_prefered_time = datetime.datetime(2022, month_number, day_number, hours_of_time, minutes_of_time)

        def time_for_train_with_one_time():
            messagebox.showinfo('info',f'there is only one available time{first_time}')
            label = tk.Label(timewindow,text='press continue button to continue else press quit to quit booking')
            label.grid(row=1, column= 0)
            button = tk.Button(timewindow,text='continue', command=t1, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
            button.grid(row=1, column=1)
            buttonquit = tk.Button(timewindow,text='quit', command=quit, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
            buttonquit.grid(row=6, column=1)
            global finalized_time
            finalized_time = first_time
        def time_for_2_train_cities():
            import datetime
            input_of_time()
            dif1 = first_time - user_prefered_time
            dif1 = (dif1.total_seconds())
            dif1 = abs(dif1)
            dif2 = second_time - user_prefered_time
            dif2 = (dif2.total_seconds())
            dif2 = abs(dif2)
            if dif1 < dif2:
                messagebox.showinfo('info',f'{first_time} is suitable time for you')
                label=tk.Label(timewindow,text=f'Enter continue to proceed with this time {first_time} OR select any time from below ',font=('calibre', 10, 'bold'),height=2)
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t1, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)

            else:
                messagebox.showinfo('info',f'{second_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {second_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t2,
                                   font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)


        def time_selection_for_3_time_trains():
            input_of_time()
            dif1 = first_time - user_prefered_time
            dif1 = (dif1.total_seconds())
            dif1 = abs(dif1)
            dif2 = second_time - user_prefered_time
            dif2 = (dif2.total_seconds())
            dif2 = abs(dif2)
            dif3 = third_time - user_prefered_time
            dif3 = (dif3.total_seconds())
            dif3 = abs(dif3)
            if dif1 < dif2 and dif1 < dif3:
                messagebox.showinfo('info',f'{first_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {first_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t1, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)
            elif dif2 < dif1 and dif2 < dif3:
                messagebox.showinfo('info',f'{second_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {second_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t2, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1,column=1)
            elif dif3 < dif2 and dif3 < dif1:
                messagebox.showinfo('info',f'{third_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {third_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t3, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)


        def time_selection_for_4_times_trains():
            input_of_time()
            dif1 = first_time - user_prefered_time
            dif1 = (dif1.total_seconds())
            dif1 = abs(dif1)
            dif2 = second_time - user_prefered_time
            dif2 = (dif2.total_seconds())
            dif2 = abs(dif2)
            dif3 = third_time - user_prefered_time
            dif3 = (dif3.total_seconds())
            dif3 = abs(dif3)
            dif4 = fourth_time - user_prefered_time
            dif4 = (dif4.total_seconds())
            dif4 = abs(dif4)
            if dif1 < dif2 and dif1 < dif3 and dif1 < dif4:
                messagebox.showinfo('info',f'{first_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {first_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t1, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)
            elif dif2 < dif1 and dif2 < dif3 and dif2 < dif4:
                messagebox.showinfo('info',f'{second_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {second_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t2, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)
            elif dif3 < dif2 and dif3 < dif1 and dif3 < dif4:
                messagebox.showinfo('info',f'{third_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {third_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t3, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)
            elif dif4 < dif1 and dif4 < dif2 and dif4 < dif3:
                messagebox.showinfo('info',f'{fourth_time} is suitable time for you')
                label = tk.Label(timewindow,text=f'Enter continue to proceed with this time {fourth_time} OR select any time from below ')
                label.grid(row=1,column=0)
                button = tk.Button(timewindow,text='continue', command=t4, font=('Ariel',15), bg='#004d80', activebackground='#004d80')
                button.grid(row=1, column=1)



        def time_aloter():
            global finalized_time
            finalized_time = available_timings_listbox.get((available_timings_listbox.curselection()))
            print(finalized_time)
            messagebox.showinfo('info',f'you have selected {finalized_time} as your departure time')
            save_record(finalized_time)

        def save_record(finalized_time):#funtion for saving record in file
            final_fixed_dictionary = {'Name': name, 'CNIC': CNIC, 'Date-of-Birth': birthday,
                                      'Departure City': departure_city, 'Arrival-City': destination_city,
                                      'Departure-Date': final_date, 'Departure-time': finalized_time,
                                      'Seat-Type': ride_class, 'no of seats': seats,
                                      'Fare-Cost': total_cost}
            print(final_fixed_dictionary)
            with open('trainrecord.txt', 'a') as file:
                for k, v in final_fixed_dictionary.items():
                    file.write(str(k) + '=' + str(v) + '\n')
                file.write('#####\n')

            result = [{}]
            with open('trainrecord.txt', 'r') as inpt:
                for line in inpt:
                    if '#####' in line:
                        result.append({})
                    else:
                        line = line.split('=')
                        key = line[0]
                        value = line[1]
                        result[-1][key] = value.strip()
            print(result)

        available_timings_label = tk.Label(timewindow,text="Available timings:", font=('calibre', 15, 'bold'))
        available_timings_label.grid(row=3, column=0, padx=0, pady=0)

        available_timings_listbox = tk.Listbox(timewindow,
                                               bg="#f7ffde",
                                               font=("Ariel", 16),
                                               )

        import datetime
        #conditions for checking the deoarture and destination city
        if departure_city == 'Karachi' and destination_city == 'Peshawar':
            train_cost = 1500
            first_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 8, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 15, 40, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Peshawar' and destination_city == 'Karachi':
            train_cost = 1500
            first_time = datetime.datetime(2022, month_number, day_number, 22, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 17, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()

        elif departure_city == 'Karachi' and destination_city == 'Quetta':
            train_cost = 1000
            first_time = datetime.datetime(2022, month_number, day_number, 9, 20, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 21, 30, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()


        elif departure_city == 'Quetta' and destination_city == 'Karachi':
            train_cost = 1000
            first_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 23, 10, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()


        elif departure_city == 'Karachi' and destination_city == 'Rawalpindi':
            train_cost = 1500
            first_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 8, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 15, 40, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Rawalpindi' and destination_city == 'Karachi':
            train_cost = 1500
            first_time = datetime.datetime(2022, month_number, day_number, 0, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 14, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 19, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 9, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Karachi' and destination_city == 'Lahore':
            train_cost = 1100
            first_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 8, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 15, 40, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Lahore' and destination_city == 'Karachi':
            train_cost = 1100
            first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 20, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 1, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Rawalpindi' and destination_city == 'Lahore':
            train_cost = 900
            first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 14, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 19, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 9, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Lahore' and destination_city == 'Rawalpindi':
            train_cost = 900
            first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 20, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 1, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Peshawar' and destination_city == 'Quetta':
            train_cost = 1800
            first_time = datetime.datetime(2022, month_number, day_number, 9, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 12, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()


        elif departure_city == 'Quetta' and destination_city == 'Peshawar':
            train_cost = 1600
            first_time = datetime.datetime(2022, month_number, day_number, 23, 50, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 3, 30, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()


        elif departure_city == 'Peshawar' and destination_city == 'Rawalpindi':
            train_cost = 1000
            first_time = datetime.datetime(2022, month_number, day_number, 22, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 17, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Rawalpindi' and destination_city == 'Peshawar':
            train_cost = 1000
            first_time = datetime.datetime(2022, month_number, day_number, 19, 40, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Karachi' and destination_city == 'Islamabad':
            train_cost = 1500
            first_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 20, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()


        elif departure_city == 'Islamabad' and destination_city == 'Karachi':
            train_cost = 1500
            first_time = datetime.datetime(2022, month_number, day_number, 10, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 18, 30, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()


        elif departure_city == 'Lahore' and destination_city == 'Islamabad':
            train_cost = 900
            first_time = datetime.datetime(2022, month_number, day_number, 7, 45, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 18, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()



        elif departure_city == 'Islamabad' and destination_city == 'Lahore':
            train_cost = 900
            first_time = datetime.datetime(2022, month_number, day_number, 18, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 21, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            time_for_2_train_cities()



        elif departure_city == 'Peshawar' and destination_city == 'Lahore':
            train_cost = 1200
            first_time = datetime.datetime(2022, month_number, day_number, 22, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 17, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()


        elif departure_city == 'Lahore' and destination_city == 'Peshawar':
            train_cost = 1200
            first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
            second_time = datetime.datetime(2022, month_number, day_number, 20, 18, 00)
            third_time = datetime.datetime(2022, month_number, day_number, 1, 50, 00)
            fourth_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
            available_timings_listbox.insert(0, first_time)
            available_timings_listbox.insert(1, second_time)
            available_timings_listbox.insert(2, third_time)
            available_timings_listbox.insert(3, fourth_time)
            time_selection_for_4_times_trains()



        else:
            print('Sorry this train is not available')
            messagebox.showinfo('info','sorry this train is not available')
            quit()
        #calculating toatal cost of travelling
        global total_cost
        total_cost = seats * (additional_cost + train_cost)
        if 568000000 > age >= 63120000:
            total_cost = 0.8 * total_cost
            messagebox.showinfo('cost', f'your total cost of travelling will be {total_cost}')
        elif age < 63120000:
            total_cost = 0 * total_cost
            messagebox.showinfo('cost', f'your total cost of travelling will be {total_cost}')
        elif age > 1892160000:
            total_cost = 0.6 * total_cost
            messagebox.showinfo('cost', f'your total cost of travelling will be {total_cost}')
        else:
            total_cost = total_cost
            messagebox.showinfo('cost', f'your total cost of travelling will be {total_cost}')
        available_timings_listbox.grid(row=3,column=1)
        available_timings_listbox.config(height= 0, width= 0)
        Sumbit_timings_button = tk.Button(timewindow,text="submit", command=time_aloter , font=('Ariel',15), bg='#004d80', activebackground='#004d80')
        Sumbit_timings_button.grid(row=5, column=1, padx=0, pady=0 )
        #closing main window
        timewindow.mainloop()



    ### ALL Functions ####

    ######### Main Gui CODE ###########
    #import messagebox library
    # creating the booking_details gui
    booking_details_main_window = tk.Tk()

    #### GUI Variables
    name_variable = tk.StringVar(booking_details_main_window)
    CNIC_variable = tk.StringVar(booking_details_main_window)
    Dob_variable = tk.StringVar(booking_details_main_window)
    Dest_variable = tk.StringVar(booking_details_main_window)
    dept_variable = tk.StringVar(booking_details_main_window)
    No_of_Seats_variable = tk.StringVar(booking_details_main_window)
    sel_date = tk.StringVar(booking_details_main_window)
    sel_time = tk.StringVar(booking_details_main_window)
    #### GUI Variables


    ###### Widgets CODE ######
    booking_details_main_window.geometry("1050x625")
    booking_details_main_window.config(bg="#0099ff")

    font_size = 13
    # booking_details_main_window.config(bg="#b3c6ff")
    #Creating all the buttons and entry boxes and using the grid medthod
    title_label = tk.Label(booking_details_main_window, text="Booking Details", font=('calibre', 25, 'bold'), bg="#008000",)
    title_label.grid(row =0, column= 3, padx=0, pady=15)

    Name_label = tk.Label(booking_details_main_window,text="Name:", font=('calibre', 14, 'bold'))
    Name_label.grid(row=1, column=0, padx=0, pady=0)
    Name_Entry = tk.Entry(booking_details_main_window,font=('calibre', font_size, 'normal'), textvariable=name_variable)
    Name_Entry.insert(0, "please enter your name:")
    Name_Entry.grid(row=1, column=1, padx=0, pady=0)
    Sumbit_name_button = tk.Button(booking_details_main_window,text="submit", command=Name_Submission)
    Sumbit_name_button.grid(row=1, column=2, padx=0, pady=0)

    CNIC_label = tk.Label(booking_details_main_window,text="CNIC:", font=('calibre', 10, 'bold'))
    CNIC_label.grid(row=1, column=4, padx=25, pady=10)
    CNIC_Entry = tk.Entry(booking_details_main_window,font=('calibre', font_size, 'normal'), textvariable=CNIC_variable)
    CNIC_Entry.insert(0, " enter your CNIC:")
    CNIC_Entry.grid(row=1, column=5, padx=0, pady=0)
    Submit_CNIC_button = tk.Button(booking_details_main_window,text="submit", command=CNIC_Submission)
    Submit_CNIC_button.grid(row=1, column=6, padx=0, pady=0)

    DOB_label = tk.Label(booking_details_main_window,text="DOB:", font=('calibre', 10, 'bold'))
    DOB_label.grid(row=2, column=4,padx=25, pady=10)
    DOB_Entry = tk.Entry(booking_details_main_window,font=('calibre', font_size, 'normal'), textvariable=Dob_variable)
    DOB_Entry.insert(0, "  YYYY-MM-DD:")
    DOB_Entry.grid(row=2, column=5, padx=0, pady=0)
    Submit_DOB_button = tk.Button(booking_details_main_window,text="submit", command=Date_of_Birth_Submission)
    Submit_DOB_button.grid(row=2, column=6, padx=5, pady=10)

    departure_label = tk.Label(booking_details_main_window,text="Departure:", font=('calibre', 10, 'bold'))
    departure_label.grid(row=3, column=0, padx=0, pady=0)
    departure_Entry = tk.Entry(booking_details_main_window,font=('calibre', font_size, 'normal'), )
    dep_listbox = tk.Listbox(booking_details_main_window,
                             bg="#f7ffde",
                             font=("Constantia",10),
                             width=12,
                             )
    dep_listbox.insert(1, "Karachi")
    dep_listbox.insert(2, "Lahore")
    dep_listbox.insert(3, "Quetta")
    dep_listbox.insert(4, "Peshawar")
    dep_listbox.insert(5, "Islamabad")
    dep_listbox.insert(6, "Rawalpindi")
    dep_listbox.config(height=dep_listbox.size())
    dep_listbox.grid(row=3, column=1, padx=0, pady=0)
    Submit_dept_button = tk.Button(booking_details_main_window,text="submit", command=Dept_Submission)
    Submit_dept_button.grid(row=3, column=2, padx=5, pady=10)

    destination_label = tk.Label(booking_details_main_window,text="Destination:", font=('calibre', 10, 'bold'))
    destination_label.grid(row=4, column=0, padx=0, pady=0)
    dest_listbox = tk.Listbox(booking_details_main_window,
                              bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,
                              )
    dest_listbox.insert(1, "Karachi")
    dest_listbox.insert(2, "Lahore")
    dest_listbox.insert(3, "Islamabad")
    dest_listbox.insert(4, "Peshawar")
    dest_listbox.insert(5, "Quetta")
    dest_listbox.insert(6, "Rawalpindi")
    dest_listbox.config(height=dest_listbox.size())
    dest_listbox.grid(row=4, column=1, padx=10, pady=10)
    Submit_dest_button = tk.Button(booking_details_main_window,text="submit", command=Dest_Submission)
    Submit_dest_button.grid(row=4, column=2, padx=5, pady=10)

    Seat_type_label = tk.Label(booking_details_main_window,text="Seat Type:", font=('calibre', 14, 'bold'))
    Seat_type_label.grid(row=4, column=4, padx=25, pady=10)

    Seat_type_listbox = tk.Listbox(booking_details_main_window,
                              bg="#f7ffde",
                              font=("Constantia",9),
                              width=14,
                              )
    Seat_type_listbox.insert(1, "Economy Seat")
    Seat_type_listbox.insert(2, "Economy Berth")
    Seat_type_listbox.insert(3, "Ac business")
    Seat_type_listbox.insert(4, "Ac sleeper")
    Seat_type_listbox.insert(5, "Ac Standard")
    Seat_type_listbox.config(height=Seat_type_listbox.size())
    Seat_type_listbox.grid(row=4, column=5, padx=0, pady=0)
    Sumbit_Seat_type_button = tk.Button(booking_details_main_window,text="submit", command=type_of_seat_selection)
    Sumbit_Seat_type_button.grid(row=4, column=6, padx=0, pady=0)


    Date_label = tk.Label(booking_details_main_window,text="Date:", font=('calibre', 14, 'bold'))
    Date_label.grid(row=5, column=0, padx=25, pady=10)
    Date_Entry = tk.Entry(booking_details_main_window,font=('calibre', 13, 'normal'), textvariable=sel_date)
    Date_Entry.insert(0, "YY-MM-DD:")
    Date_Entry.grid(row=5, column=1, padx=0, pady=0)
    Sumbit_Date_button = tk.Button(booking_details_main_window,text="submit", command=date_selection)
    Sumbit_Date_button.grid(row=5, column=2, padx=0, pady=0)



    Time_label = tk.Label(booking_details_main_window,text="Time:", font=('calibre', 14, 'bold'))
    Time_label.grid(row=5, column=4, padx=25, pady=10)
    Time_Entry = tk.Entry(booking_details_main_window,font=('calibre', 13, 'normal'), textvariable=sel_time)
    Time_Entry.insert(0, "HH-MM:")
    Time_Entry.grid(row=5, column=5, padx=0, pady=0)
    Sumbit_Time_button = tk.Button(booking_details_main_window,text="submit", command=time_selection)
    Sumbit_Time_button.grid(row=5, column=6, padx=0, pady=0)




    No_of_Seats_label = tk.Label(booking_details_main_window,text="Number of Seats:", font=('calibre', 10, 'bold'))
    No_of_Seats_label.grid(row=3, column=4, padx=25, pady=10)
    No_of_Seats_Entry = tk.Entry(booking_details_main_window,font=('calibre', font_size, 'normal'), textvariable=No_of_Seats_variable)
    No_of_Seats_Entry.insert(0, "")
    No_of_Seats_Entry.grid(row=3, column=5, padx=0, pady=0)
    Submit_num_of_seats_button = tk.Button(booking_details_main_window,text="submit", command=seat_submission)
    Submit_num_of_seats_button.grid(row=3, column=6, padx=0, pady=0)
    Continue_Booking_Button = tk.Button(booking_details_main_window,text="Confirm booking", font=('calibre', 25, 'bold'), command=timfun,
                                        bg='#004d80', activebackground='#004d80')
    Continue_Booking_Button.grid(row=7, column=3, padx=0, pady= 10)
    ### GUI Widgets code



    #### GUI CODE

    tk.mainloop()
