#creating main funtion
def display():
    import tkinter as tk
    tuples = []
    #reading timetable from the program and splitting it according to our requirement
    for t in open('train_schedules.py').read().split():
        trainRecords = t.strip('()').split("\n")
        tuples.append(trainRecords)
    win = tk.Tk()
    #creating all listbox required
    listbox_1 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_2 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_3 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_4 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_5 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_6 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_7 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_8 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_9 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_10 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_11 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_12 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)


    listbox_13 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_14 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_15 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_16 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_17 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_18 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_19 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_20 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_21 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_22 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_23 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_24 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_25 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_26 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_27 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_28 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_29 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_30 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)


    listbox_31 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_32 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_33 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_34 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_35 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_36 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_37 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_38 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_39 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)
    listbox_40 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_41 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)

    listbox_42 = tk.Listbox(win,bg="#f7ffde",
                              font=("Constantia",10),
                              width=12,)



    #creating different labels

    dep_lable = tk.Label(win,font=("Ariel",10, "bold"), text="departure city")
    dest_lable = tk.Label(win,font=("Ariel",10, "bold"), text='destination city')
    dep_time = tk.Label(win,font=("Ariel",10, "bold"), text="departure time")
    dest_time = tk.Label(win,font=("Ariel",10, "bold"), text='destination time')
    train_id = tk.Label(win,font=("Ariel",10, "bold"), text="Train_id")
    price = tk.Label(win,font=("Ariel",10, "bold"), text='price')
    dep_lable_1 = tk.Label(win,font=("Ariel",10, "bold"), text="departure city")
    dest_lable_1 = tk.Label(win,font=("Ariel",10, "bold"), text='destination city')
    dep_time_1 = tk.Label(win,font=("Ariel",10, "bold"), text="departure time")
    dest_time_1 = tk.Label(win,font=("Ariel",10, "bold"), text='destination time')
    train_id_1 = tk.Label(win,font=("Ariel",10, "bold"), text="Train_id")
    price_1 = tk.Label(win,font=("Ariel",10, "bold"), text='price')

    dep_lable.grid(row=0,column=0)
    dest_lable.grid(row=0,column=1)
    dep_time.grid(row=0,column=2)
    dest_time.grid(row=0,column=3)
    train_id.grid(row=0,column=4)
    price.grid(row=0, column= 5)

    dep_lable_1.grid(row=0,column=7)
    dest_lable_1.grid(row=0,column=8)
    dep_time_1.grid(row=0,column=9)
    dest_time_1.grid(row=0,column=10)
    train_id_1.grid(row=0,column=11)
    price_1.grid(row=0, column= 12)

    z = 0
    for i in tuples:
        if z < 10:
            listbox_1.insert(z,eval(i[0].split(',')[0]))
            listbox_2.insert(z,eval(i[0].split(',')[1]))
            listbox_3.insert(z,eval(i[0].split(',')[2]))
            listbox_4.insert(z,eval(i[0].split(',')[3]))
            listbox_9.insert(z,eval(i[0].split(',')[4]))
            listbox_10.insert(z, eval(i[0].split(',')[5]))
        elif z in range(10, 20):
            listbox_5.insert(z, eval(i[0].split(',')[0]))
            listbox_6.insert(z, eval(i[0].split(',')[1]))
            listbox_7.insert(z, eval(i[0].split(',')[2]))
            listbox_8.insert(z, eval(i[0].split(',')[3]))
            listbox_11.insert(z, eval(i[0].split(',')[4]))
            listbox_12.insert(z, eval(i[0].split(',')[5]))
        elif z in range(20,30):
            listbox_13.insert(z, eval(i[0].split(',')[0]))
            listbox_14.insert(z, eval(i[0].split(',')[1]))
            listbox_15.insert(z, eval(i[0].split(',')[2]))
            listbox_16.insert(z, eval(i[0].split(',')[3]))
            listbox_17.insert(z, eval(i[0].split(',')[4]))
            listbox_18.insert(z, eval(i[0].split(',')[5]))
        elif z in range(30,40):
            listbox_19.insert(z, eval(i[0].split(',')[0]))
            listbox_20.insert(z, eval(i[0].split(',')[1]))
            listbox_21.insert(z, eval(i[0].split(',')[2]))
            listbox_22.insert(z, eval(i[0].split(',')[3]))
            listbox_23.insert(z, eval(i[0].split(',')[4]))
            listbox_24.insert(z, eval(i[0].split(',')[5]))
        elif z in range(40,50):
            listbox_25.insert(z, eval(i[0].split(',')[0]))
            listbox_26.insert(z, eval(i[0].split(',')[1]))
            listbox_27.insert(z, eval(i[0].split(',')[2]))
            listbox_28.insert(z, eval(i[0].split(',')[3]))
            listbox_29.insert(z, eval(i[0].split(',')[4]))
            listbox_30.insert(z, eval(i[0].split(',')[5]))
        elif z in range(50,60):
            listbox_31.insert(z, eval(i[0].split(',')[0]))
            listbox_32.insert(z, eval(i[0].split(',')[1]))
            listbox_33.insert(z, eval(i[0].split(',')[2]))
            listbox_34.insert(z, eval(i[0].split(',')[3]))
            listbox_35.insert(z, eval(i[0].split(',')[4]))
            listbox_36.insert(z, eval(i[0].split(',')[5]))
        elif z in range(60,70):
            listbox_37.insert(z, eval(i[0].split(',')[0]))
            listbox_38.insert(z, eval(i[0].split(',')[1]))
            listbox_39.insert(z, eval(i[0].split(',')[2]))
            listbox_40.insert(z, eval(i[0].split(',')[3]))
            listbox_41.insert(z, eval(i[0].split(',')[4]))
            listbox_42.insert(z, eval(i[0].split(',')[5]))



        z +=1
    listbox_1.grid(row=1,column=0)
    listbox_2.grid(row=1, column= 1)
    listbox_3.grid(row=1,column=2)
    listbox_4.grid(row=1,column=3)
    listbox_9.grid(row=1,column=4)
    listbox_10.grid(row=1,column=5)
    listbox_5.grid(row=2,column=0)
    listbox_6.grid(row=2, column= 1)
    listbox_7.grid(row=2,column=2)
    listbox_8.grid(row=2,column=3)
    listbox_11.grid(row=2,column=4)
    listbox_12.grid(row=2,column=5)

    listbox_13.grid(row=3,column=0)
    listbox_14.grid(row=3, column= 1)
    listbox_15.grid(row=3,column=2)
    listbox_16.grid(row=3,column=3)
    listbox_17.grid(row=3,column=4)
    listbox_18.grid(row=3,column=5)

    listbox_19.grid(row=4,column=0)
    listbox_20.grid(row=4, column= 1)
    listbox_21.grid(row=4,column=2)
    listbox_22.grid(row=4,column=3)
    listbox_23.grid(row=4,column=4)
    listbox_24.grid(row=4,column=5)

    listbox_25.grid(row=1,column=7)
    listbox_26.grid(row=1, column= 8)
    listbox_27.grid(row=1,column=9)
    listbox_28.grid(row=1,column=10)
    listbox_29.grid(row=1,column=11)
    listbox_30.grid(row=1,column=12)

    listbox_31.grid(row=2,column=7)
    listbox_32.grid(row=2, column= 8)
    listbox_33.grid(row=2,column=9)
    listbox_34.grid(row=2,column=10)
    listbox_35.grid(row=2,column=11)
    listbox_36.grid(row=2,column=12)

    listbox_37.grid(row=3,column=7)
    listbox_38.grid(row=3, column= 8)
    listbox_39.grid(row=3,column=9)
    listbox_40.grid(row=3,column=10)
    listbox_41.grid(row=3,column=11)
    listbox_42.grid(row=3,column=12)




    print(len(tuples))
    win.mainloop()
