import  os


timetable = '''S.No.   From         To        Train-Timing            Train-ID
                              (Departure)  (Journey)
 01.  Karachi      Peshawar      5:40      (16 hrs)   Train-501      
 02.  Karachi      Peshawar      8:15      (16 hrs)   Train-502
 03.  Karachi      Peshawar      15:40     (16 hrs)   Train-503
 04.  Karachi      Peshawar      22:15     (16 hrs)   Train-504

 01.  Peshawar     Karachi       22:00     (16 hrs)   Train-510
 02.  Peshawar     Karachi       12:15     (16 hrs)   Train-511
 03.  Peshawar     Karachi       17:50     (16 hrs)   Train-512
 04.  Peshawar     Karachi       07:00     (16 hrs)   Train-513

 01.  Karachi      Quetta        9:20      (20 hrs)   Train-533
 02.  Karachi      Quetta        21:30     (20 hrs)   Train-534

 01.  Quetta       Karachi       7:00      (20 hrs)   Train-533
 02.  Quetta       Karachi       23:10     (20 hrs)   Train-534

 01.  Karachi      Rawalpindi    5:40      (14 hrs)   Train-501          
 02.  Karachi      Rawalpindi    8:15      (14 hrs)   Train-502
 03.  Karachi      Rawalpindi    15:40     (14 hrs)   Train-503
 04.  Karachi      Rawalpindi    22:15     (14 hrs)   Train-504

 01.  Rawalpindi   Karachi       00:00     (14 hrs)   Train-510
 02.  Rawalpindi   Karachi       14:15     (14 hrs)   Train-511
 03.  Rawalpindi   Karachi       19:50     (14 hrs)   Train-512
 04.  Rawalpindi   Karachi       9:00      (14 hrs)   Train-513

 01.  Karachi      Lahore        5:40      (8 hrs)    Train-501         
 02.  Karachi      Lahore        8:15      (8 hrs)    Train-502
 03.  Karachi      Lahore        15:40     (8 hrs)    Train-503      
 04.  Karachi      Lahore        22:15     (8 hrs)    Train-504

 01.  Lahore       Karachi       6:00      (8 hrs)    Train-510
 02.  Lahore       Karachi       20:15     (8 hrs)    Train-511
 03.  Lahore       Karachi       1:50      (8 hrs)    Train-512
 04.  Lahore       Karachi       15:00     (8 hrs)    Train-513

 01.  Karachi      Sialkot       14:00     (13 hrs)   Train-506
 02.  Karachi      Sialkot       20:00     (13 hrs)   Train-507
 03.  Karachi      Sialkot       5:30      (13 hrs)   Train-508

 01.  Sialkot      Karachi       6:30      (13 hrs)   Train-506
 02.  Sialkot      Karachi       10:15     (13 hrs)   Train-507
 03.  Sialkot      Karachi       20:30     (13 hrs)   Train-508

 01.  Rawalpindi   Multan        00:00     (8 hrs)    Train-510
 02.  Rawalpindi   Multan        14:15     (8 hrs)    Train-511

 01.  Multan       Rawalpindi    19:40     (8 hrs)    Train-501
 02.  Multan       Rawalpindi    22:15     (8 hrs)    Train-502

 01.  Rawalpindi   Lahore        00:00     (6 hrs)    Train-510
 02.  Rawalpindi   Lahore        14:15     (6 hrs)    Train-511
 03.  Rawalpindi   Lahore        19:50     (6 hrs)    Train-512
 04.  Rawalpindi   Lahore        9:00      (6 hrs)    Train-513

 01.  Lahore       Rawalpindi    6:00      (5 hrs)    Train-501
 02.  Lahore       Rawalpindi    20:15     (5 hrs)    Train-502
 03.  Lahore       Rawalpindi    1:50      (5 hrs)    Train-503
 04.  Lahore       Karachi       15:00     (8 hrs)    Train-504

 01.  Peshawar     Quetta        09:00    (14 hrs)    Train-520
 03.  Peshawar     Quetta        12:00    (14 hrs)    Train-521

 01.  Quetta       Peshawar      23:50    (14 hrs)    Train-520
 02.  Quetta       Peshawar      3:30     (14 hrs)    Train-521

 01.  Peshawar     Rawalpindi    22:00    (2 hrs)     Train-510
 02.  Peshawar     Rawalpindi    12:15    (2 hrs)     Train-511
 03.  Peshawar     Rawalpindi    17:50    (2 hrs)     Train-512
 04.  Peshawar     Rawalpindi    7:00     (2 hrs)     Train-513

 01.  Rawalpindi   Peshawar      19:40    (2 hrs)     Train-501
 02.  Rawalpindi   Peshawar      22:15    (2 hrs)     Train-502
 03.  Rawalpindi   Peshawar      5:40     (2 hrs)     Train-503
 04.  Rawalpindi   Peshawar      12:15    (2 hrs)     Train-504

 01.  Karachi      Islamabad     15:00    (14 hrs)    Train-525 
 02.  Karachi      Islamabad     20:00    (14 hrs)    Train-526 

 01.  Islamabad    Karachi       10:00    (14 hrs)    Train-525
 02.  Islamabad    Karachi       18:30    (14 hrs)    Train-526

 01.  Lahore       Islamabad     7:45     (6 hrs)     Train-525
 02.  Lahore       Islamabad     18:00    (6 hrs)     Train-526

 01.  Islamabad    Lahore        18:00    (6 hrs)     Train-525
 02.  Islamabad    Lahore        21:00    (6 hrs)     Train-526        

 01.  Peshawar     Lahore        22:00    (8 hrs)     Train-510
 02.  Peshawar     Lahore        12:15    (8 hrs)     Train-511
 03.  Peshawar     Lahore        17:50    (8 hrs)     Train-512
 04.  Peshawar     Lahore        7:00     (8 hrs)     Train-513

 01.  Lahore       Peshawar      6:00     (8 hrs)     Train-501
 02.  Lahore       Peshawar      20:15    (8 hrs)     Train-502
 03.  Lahore       Peshawar      1:50     (8 hrs)     Train-503
 04.  Lahore       Peshawar      15:00    (8 hrs)     Train-504

 '''
Karachi = 'Karachi'
Lahore = 'Lahore'
Quetta = 'Quetta'
Islamabad = 'Islamabad'
Rawalpindi = 'Rawalpindi'
Peshawar = 'Peshawar'
Sialkot = 'Sialkot'
Multan = 'Multan'
cities = [Karachi, Lahore, Quetta, Islamabad, Rawalpindi, Peshawar, Sialkot, Multan]


# def time_table():
# print(timetable)

def city_selection():
    departure = input('Enter city from which you want to depart: ')
    global departure_city
    departure_city = (departure.lower()).capitalize()
    drop = input('Enter your Arrival-City: ')
    global destination_city
    destination_city = (drop.lower()).capitalize()
    if departure_city == '' or destination_city == '':
        print('Please enter a city..')
        city_selection()
        return
    if departure_city == Islamabad and destination_city == Rawalpindi:
        print('Sorry; This ride is Unavailable.')
        city_selection()
        return
    if departure_city == Rawalpindi and destination_city == Islamabad:
        print('Sorry this ride is Unavailable.')
        city_selection()
        return
    if departure_city == destination_city:
        print('Please enter Different cities for Departure and Arrival.')
        city_selection()
        return
    if departure_city not in cities or destination_city not in cities:
        print('Please enter valid city OR Re-check the spellings you entered.')
        city_selection()
        return


def date_selection():
    try:
        import datetime
        global day_number
        day_number = int(input('Enter the date you want to depart: '))
        global month_number
        month_number = int(input('Enter the month number: '))
        date_entered = datetime.date(2022, month_number, day_number)
        global today_date
        today_date = datetime.date.today()
        global date_difference
        date_difference = date_entered - today_date
        date_difference = date_difference.total_seconds()
        # 604800 is number of seconds in 7 days
        if date_difference > 604800.0 or date_difference < 0:
            print('Please enter date within future seven days advance'
                  'Only 7 days Advance Booking is Available.')
            date_selection()
            return
        global final_date
        final_date = date_entered.strftime('%A,%d %B,%Y')
        print('You have selected', final_date, 'as your Departure Date')
    except:
        print('Please enter Month-Number(e.g., 7 for July); Do not Enter Month-Name OR Enter month in range(1 to 12)')
        date_selection()


def user_info():
    import datetime
    global user_name, CNIC_No, birth_month, birth_date, birth_year, age, birthday, today_date,booking_code
    user_name = ((input('Enter your Name: ')).lower()).capitalize()
    CNIC_No = input('Enter Your CNIC Number in following format 1310120312705: ')
    if len(CNIC_No)<13 or len(CNIC_No)>13:
        print('please enter valid cnic number thanks and enter data again')
        user_info()
        return
    if not CNIC_No.isdigit():
        print('please enter valid cnic and enter data again')
        user_info()
        return
    birth_year = int(input('Please enter your Birth-Year: '))
    if birth_year<1900:
        print('please enter years greater than 1900 and enter data again')
        user_info()
        return
    birth_month = int(input('Enter your Birth-Month: '))
    birth_date = int(input('Enter Your Birth-Date: '))
    birthday = datetime.date(birth_year, birth_month, birth_date)
    today_date = datetime.date.today()
    age = today_date - birthday
    age = age.total_seconds()
    booking_code = CNIC_No[6:13]
    print(booking_code, 'is your booking code please note it for further uses')

def seats_selection():
    print('''Available Ride-Zones with their addition cost
       SEAT TYPE        ADDITIONAL SEAT COST in Rs
       Economy Seat     0
       Economy Berth    100
       AC Business     4300
       AC Standard      2200
       AC Sleeper       6200''')
    global rides
    rides = {'economy seat': 0, 'economy berth': 100, 'ac business': 4300, 'ac standard': 2200, 'ac sleeper': 6200}
    global ride_class
    ride_class = input('Enter which type of Ride-Zone you want to Book: ')
    ride_class = ride_class.lower()
    if ride_class not in rides:
        print('Sorry; This seat is not available OR check your spellings, Again! ')
        seats_selection()
        return
    global additional_cost
    additional_cost = rides[ride_class]
    print(additional_cost, 'Rs will be charged Additional')
    try:
        global seats
        seats = int(input('Enter number of seats you want to book: '))
    except:
        print('Please Enter number of seats. # No any other character #')
        seats_selection()
        return
    additional_cost = additional_cost


def input_of_time():
    import datetime
    global hours_of_time, present_time
    hours_of_time = int(input('Enter hours(in 24-Hours Format) of the Time you want to depart: '))  # remove minutes
    global minutes_of_time
    minutes_of_time = int(input('Enter minutes of the Time: '))
    global user_prefered_time
    user_prefered_time = datetime.datetime(2022, month_number, day_number, hours_of_time, minutes_of_time)
    if date_difference == 0:
        present_time = datetime.datetime.now()
        time_diff = user_prefered_time - present_time
        time_diff = time_diff.total_seconds()
        if time_diff <= 0:
            print('Please enter future time. Not the Past-Time!')
            input_of_time()
            return

    global formated_time
    formated_time = user_prefered_time.strftime(
        'You have entered %A,%d%B,%Y,%H:%M:%S  as your  prefered Departure-Date.')
    print(formated_time)
    global user_time_decision
    user_time_decision = input('Enter yes to proceed OR Press any key to enter time again: ')
    user_time_decision = user_time_decision.lower()


def time_for_train_with_one_time():
    import datetime
    global finalized_time, final_time_diff
    finalized_time = first_time
    print('There is only one time avaialable', first_time)
    dec = input('Enter y to proceed OR any other button to Cancel-Booking: ')
    if dec != 'y':
        print('Cancelling-Bboking')
        quit()

    present_time = datetime.datetime.now()
    final_time_diff = finalized_time - present_time
    final_time_diff = final_time_diff.total_seconds()
    if final_time_diff <= 0:
        print('Suhail Data')
        second_dec = input('Enter y to change your Booking details OR any other button to Cancel-Booking: ')
        if second_dec == 'y':
            all()
            return
        else:
            print('Canceling-booking')
            quit()
    finalized_time = finalized_time.strftime('%H:%M:%S')


def time_for_2_train_cities():
    import datetime
    input_of_time()
    global finalized_time, dif1
    global econ_list, business_list, berth_list, sleeper_list, standard_list, window_list, aisle_list
    finalized_time = datetime.datetime(2022, month_number, day_number, 6, 40, 00)
    if user_time_decision != 'yes':
        print('Enter your time again')
        time_for_2_train_cities()
        return
    dif1 = first_time - user_prefered_time
    dif1 = (dif1.total_seconds())
    dif1 = abs(dif1)
    dif2 = second_time - user_prefered_time
    dif2 = (dif2.total_seconds())
    dif2 = abs(dif2)
    if dif1 < dif2:
        print(first_time, 'is suitable time for you')
        user_decision = input('Enter y to proceed with this time OR any other key for another time: ')
        if user_decision == 'y':
            finalized_time = first_time

        else:
            print('''Following are the only available times for this train available ''')
            print('t1', first_time)
            print('t2', second_time)
            final_decision = input('Press 1 for t1 or 2 for t2 OR any other key for Cancel-Booking')
            if final_decision == '1':
                finalized_time = first_time
            elif final_decision == '2':
                finalized_time = second_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose time again: ')
                if ip == 'y':
                    print('Cancelling-Booking')
                    quit()
                else:
                    time_for_2_train_cities()
    else:
        print(second_time, 'is your suitable time')
        user_decision = input('Enter y to proceed with this time or any other key for another time: ')
        if user_decision == 'y':
            finalized_time = second_time

        else:
            print('''Following are the only available times for this train available ''')
            print('t1', first_time)
            print('t2', second_time)
            final_decision = input('Press 1 for t1 or 2 for t2 OR any other key for Cancelling-Booking: ')
            if final_decision == '1':
                finalized_time = first_time
            elif final_decision == '2':
                finalized_time = second_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose time again: ')
                if ip == 'y':
                    print('Cancelling-Booking')
                    quit()
                else:
                    time_for_2_train_cities()
    if date_difference == 0:
        present_time = datetime.datetime.now()
        time_diff = finalized_time - present_time
        time_diff = time_diff.total_seconds()
        if time_diff <= 0:
            print('Sorry; This time is not possible. Please select future time. Not Past-Time')
            date_dec = (input('Enter d for changing Date OR t for changing Time  '
                              'any other button to Cancel-Booking')).lower()
            if date_dec == 'd':
                date_selection()
                time_aloter()
                return
            elif date_dec == 't':
                time_aloter()
                return
            else:
                print('Cancelling-Booking')
                quit()
    finalized_time = finalized_time.strftime('%H:%M:%S')


def time_selection_for_3_time_trains():
    import datetime
    input_of_time()
    global finalized_time
    global econ_list, business_list, berth_list, sleeper_list, standard_list, window_list, aisle_list
    if user_time_decision != 'yes':
        print('Enter your time again.')
        time_selection_for_3_time_trains()
        return
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
        print(first_time, 'is suitable time for you')
        dec = input('Enter y to proceed with this time OR any other key for another time: ')
        if dec == 'y':
            finalized_time = first_time
        else:
            print('''Following are the only available times for this train available ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            fdec = input('Press 1 for t1 or 2 for t2 or 3 for t3 OR any other key for Canceling-Booking: ')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose Time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_3_time_trains()
    elif dif2 < dif1 and dif2 < dif3:
        print(second_time, 'is your suitable time')
        dec = input('Enter y to proceed with this time OR any other key for another Time: ')
        if dec == 'y':
            finalized_time = second_time
        else:
            print('''Fllowing are the only available times for this train available ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            fdec = input('Press 1 for t1 or 2 for t2 or 3 for t3 OR any other key for Cancel-Booking:')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose Time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_3_time_trains()
    elif dif3 < dif2 and dif3 < dif1:
        print(third_time, 'is your suitable time')
        dec = input('Enter y to proceed with this time OR any other key for another Time: ')
        if dec == 'y':
            finalized_time = third_time
        else:
            print('''Following are the only available times for this train available: ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            fdec = input('Press 1 for t1 or 2 for t2 or 3 for t3 OR any other key for Canceling-Booking')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose Time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_3_time_trains()
    if date_difference == 0:
        present_time = datetime.datetime.now()
        time_diff = finalized_time - present_time
        time_diff = time_diff.total_seconds()
        if time_diff <= 0:
            print('Sorry; This time is not possible. Please select future time. Not the Past-Time')
            date_dec = input(('Enter d for changing Date OT t for changing Time OR '
                              'any other button to Cancel-Booking. Press d if no time is suitable for you on this date: ')).lower()

            if date_dec == 'd':
                date_selection()
                time_aloter()
                return
            elif date_dec == 't':
                time_aloter()
                return
            else:
                print('Canceling-Booking')
                quit()
    finalized_time = finalized_time.strftime('%H:%M:%S')


def time_selection_for_4_times_trains():
    import datetime
    input_of_time()
    global finalized_time, dif1
    global econ_list, business_list, berth_list, sleeper_list, standard_list, window_list, aisle_list
    if user_time_decision != 'yes':
        print('Enter your time again: ')
        time_selection_for_4_times_trains()
        return
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
        print(first_time, 'is suitable time for you')
        dec = input('Enter y to proceed with this time OR any other key for another Time: ')
        if dec == 'y':
            finalized_time = first_time
        else:
            print('''Following are the only available times for this train available ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            print('t4', fourth_time)
            fdec = input('press 1 for t1 or 2 for t2 or 3 for t3 or 4 for t4 or any other key for cancel booking')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            elif fdec == '4':
                finalized_time = fourth_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_4_times_trains()
    elif dif2 < dif1 and dif2 < dif3 and dif2 < dif4:
        print(second_time, 'is your suitable time')
        dec = input('Enter y to proceed with this time OR any other key for another time: ')
        if dec == 'y':
            finalized_time = second_time
        else:
            print('''Following are the only available times for this train available: ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            print('t4', fourth_time)
            fdec = input('Press 1 for t1 or 2 for t2 or 3 for t3 or 4 for t4 OR any other key for Canceling-Booking:')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            elif fdec == '4':
                finalized_time = fourth_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_4_times_trains()
    elif dif3 < dif2 and dif3 < dif1 and dif3 < dif4:
        print(third_time, 'is your suitable time')
        dec = input('Enter y to proceed with this time OR any other key for another time: ')
        if dec == 'y':
            finalized_time = third_time
        else:
            print('''Following are the only available times for this train available: ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            print('t4', fourth_time)
            fdec = input('Press 1 for t1 or 2 for t2 or 3 for t3 or 4 for t4 OR any other key for Canceling-Booking: ')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            elif fdec == '4':
                finalized_time = fourth_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_4_times_trains()
    elif dif4 < dif1 and dif4 < dif2 and dif4 < dif3:
        print(fourth_time, 'is your suitable time')
        dec = input('Enter y to proceed with this time OR any other key for another time:  ')
        if dec == 'y':
            finalized_time = fourth_time
        else:
            print('''Following are the only available times for this train available: ''')
            print('t1', first_time)
            print('t2', second_time)
            print('t3', third_time)
            print('t4', fourth_time)
            fdec = input('Press 1 for t1 or 2 for t2 or 3 for t3 or 4 for t4 OR any other key for cancel booking: ')
            if fdec == '1':
                finalized_time = first_time
            elif fdec == '2':
                finalized_time = second_time
            elif fdec == '3':
                finalized_time = third_time
            elif fdec == '4':
                finalized_time = fourth_time
            else:
                ip = input('Press y if you are sure to Cancel-Booking OR any other key to choose time again: ')
                if ip == 'y':
                    print('Canceling-Booking')
                    quit()
                else:
                    time_selection_for_4_times_trains()
    if date_difference == 0:
        present_time = datetime.datetime.now()
        time_diff = finalized_time - present_time
        time_diff = time_diff.total_seconds()
        if time_diff <= 0:
            print('sorry this time is not possible please select future time not past time')
            date_dec = (input('Enter d for changing Date OR t for changing Time OR '
                              'any other button for Canceling-Booking')).lower()
            if date_dec == 'd':
                date_selection()
                time_aloter()
                return
            elif date_dec == 't':
                time_aloter()
                return
            else:
                print('Canceling-Booking')
                quit()
    finalized_time = finalized_time.strftime('%H:%M:%S')


def time_aloter():
    import datetime
    global train_number, train_cost, first_time, second_time, third_time, fourth_time
    if departure_city == Karachi and destination_city == Peshawar:
        train_cost = 1500
        first_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 8, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 15, 40, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-503'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-504'

    elif departure_city == Peshawar and destination_city == Karachi:
        train_cost = 1700
        first_time = datetime.datetime(2022, month_number, day_number, 22, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 17, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-512'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-513'

    elif departure_city == Karachi and destination_city == Quetta:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 9, 20, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 21, 30, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-533'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-534'

    elif departure_city == Quetta and destination_city == Karachi:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 23, 10, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-533'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-534'

    elif departure_city == Karachi and destination_city == Rawalpindi:
        train_cost = 1500
        first_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 8, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 15, 40, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-503'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-504'

    elif departure_city == Rawalpindi and destination_city == Karachi:
        train_cost = 1500
        first_time = datetime.datetime(2022, month_number, day_number, 0, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 14, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 19, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 9, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-512'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-513'

    elif departure_city == Karachi and destination_city == Lahore:
        train_cost = 1100
        first_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 8, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 15, 40, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-503'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-504'

    elif departure_city == Lahore and destination_city == Karachi:
        train_cost = 1100
        first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 20, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 1, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-512'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-513'

    elif departure_city == Karachi and destination_city == Sialkot:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 14, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 20, 00, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 5, 30, 00)
        time_selection_for_3_time_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-506'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-507'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-508'

    elif departure_city == Sialkot and destination_city == Karachi:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 6, 30, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 10, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 20, 30, 00)
        time_selection_for_3_time_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-506'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-507'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-508'

    elif departure_city == Rawalpindi and destination_city == Multan:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 0, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 14, 15, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'

    elif departure_city == Multan and destination_city == Rawalpindi:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 19, 40, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'

    elif departure_city == Rawalpindi and destination_city == Lahore:
        train_cost = 900
        first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 14, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 19, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 9, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-512'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-513'

    elif departure_city == Lahore and destination_city == Rawalpindi:
        train_cost = 900
        first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 20, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 1, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-503'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-504'

    elif departure_city == Peshawar and destination_city == Quetta:
        train_cost = 1800
        first_time = datetime.datetime(2022, month_number, day_number, 9, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 12, 00, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-520'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-521'

    elif departure_city == Quetta and destination_city == Peshawar:
        train_cost = 1600
        first_time = datetime.datetime(2022, month_number, day_number, 23, 50, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 3, 30, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-520'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-521'

    elif departure_city == Peshawar and destination_city == Rawalpindi:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 22, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 17, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-512'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-513'


    elif departure_city == Rawalpindi and destination_city == Peshawar:
        train_cost = 1000
        first_time = datetime.datetime(2022, month_number, day_number, 19, 40, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 22, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 5, 40, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-503'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-504'


    elif departure_city == Karachi and destination_city == Islamabad:
        train_cost = 1500
        first_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 20, 00, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-525'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-526'


    elif departure_city == Islamabad and destination_city == Karachi:
        train_cost = 1500
        first_time = datetime.datetime(2022, month_number, day_number, 10, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 18, 30, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-525'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-526'

    elif departure_city == Lahore and destination_city == Islamabad:
        train_cost = 900
        first_time = datetime.datetime(2022, month_number, day_number, 7, 45, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 18, 00, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-525'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-526'


    elif departure_city == Islamabad and destination_city == Lahore:
        train_cost = 900
        first_time = datetime.datetime(2022, month_number, day_number, 18, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 21, 00, 00)
        time_for_2_train_cities()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-525'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-526'


    elif departure_city == Peshawar and destination_city == Lahore:
        train_cost = 1200
        first_time = datetime.datetime(2022, month_number, day_number, 22, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 12, 15, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 17, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 7, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-510'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-511'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-512'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-513'

    elif departure_city == Lahore and destination_city == Peshawar:
        train_cost = 1200
        first_time = datetime.datetime(2022, month_number, day_number, 6, 00, 00)
        second_time = datetime.datetime(2022, month_number, day_number, 20, 18, 00)
        third_time = datetime.datetime(2022, month_number, day_number, 1, 50, 00)
        fourth_time = datetime.datetime(2022, month_number, day_number, 15, 00, 00)
        time_selection_for_4_times_trains()
        if str(finalized_time) in str(first_time):
            train_number = 'Train-501'
        elif str(finalized_time) in str(second_time):
            train_number = 'Train-502'
        elif str(finalized_time) in str(third_time):
            train_number = 'Train-503'
        elif str(finalized_time) in str(fourth_time):
            train_number = 'Train-504'

    else:
        print('Sorry this train is not available')
        city_selection()
        time_aloter()

def cities_rate():
    global train_cost
    if departure_city == Karachi and destination_city == Peshawar:
        train_cost = 1500
    elif departure_city == Peshawar and destination_city == Karachi:
        train_cost = 1700
    elif departure_city == Karachi and destination_city == Quetta:
        train_cost = 1000
    elif departure_city == Quetta and destination_city == Karachi:
        train_cost = 1000
    elif departure_city == Karachi and destination_city == Rawalpindi:
        train_cost = 1500
    elif departure_city == Rawalpindi and destination_city == Karachi:
        train_cost = 1500
    elif departure_city == Karachi and destination_city == Lahore:
        train_cost = 1100
    elif departure_city == Lahore and destination_city == Karachi:
        train_cost = 1100
    elif departure_city == Karachi and destination_city == Sialkot:
        train_cost = 1000
    elif departure_city == Sialkot and destination_city == Karachi:
        train_cost = 1000
    elif departure_city == Rawalpindi and destination_city == Multan:
        train_cost = 1000
    elif departure_city == Multan and destination_city == Rawalpindi:
        train_cost = 1000
    elif departure_city == Rawalpindi and destination_city == Lahore:
        train_cost = 900
    elif departure_city == Lahore and destination_city == Rawalpindi:
        train_cost = 900
    elif departure_city == Peshawar and destination_city == Quetta:
        train_cost = 1800
    elif departure_city == Quetta and destination_city == Peshawar:
        train_cost = 1600
    elif departure_city == Peshawar and destination_city == Rawalpindi:
        train_cost = 1000
    elif departure_city == Rawalpindi and destination_city == Peshawar:
        train_cost = 1000
    elif departure_city == Karachi and destination_city == Islamabad:
        train_cost = 1500
    elif departure_city == Islamabad and destination_city == Karachi:
        train_cost = 1500
    elif departure_city == Lahore and destination_city == Islamabad:
        train_cost = 900
    elif departure_city == Islamabad and destination_city == Lahore:
        train_cost = 900
    elif departure_city == Peshawar and destination_city == Lahore:
        train_cost = 1200
    elif departure_city == Lahore and destination_city == Peshawar:
        train_cost = 1200

def cost_calculator():
    global total_cost
    total_cost =seats*(additional_cost + train_cost)
    if 568000000 > age >= 63120000:
        total_cost = 0.2 * total_cost
    elif age < 63120000:
        total_cost = 0 * total_cost
    elif age > 1892160000:
        total_cost = 0.4 * total_cost
    else:
        total_cost = total_cost
def update_record():
    import datetime
    result = [{}]
    with open('trainrecord.txt', 'r') as file:
        for line in file:
            if '#####' in line:
                result.append({})
            else:
                line = line.split('=')
                key = line[0]
                value = line[1]
                result[-1][key] = value.strip()
    booking_id=input('please input your cnic ')
    for dicts in result:
        if booking_id in dicts.values():
            print('''available update options
            1. Seat type or No of seats
            2. Date selection and Time selection''')
            update_dec = input('please select your option from above 1 for seats, 2 for date and time or'
                               'any other button to cancel update process')
            if update_dec == '1':
                global departure_city, destination_city,age,birthdate
                birthdate=dicts['Date-of-Birth']
                year = int(birthdate[0:4])
                month = int(birthdate[5:7])
                date = int(birthdate[8:])
                final_birth_date = datetime.date(year,month,date)
                today_date = datetime.date.today()
                age = today_date-final_birth_date
                age = age.total_seconds()
                departure_city = dicts['Departure City']
                destination_city = dicts['Arrival-City']
                cities_rate()
                seats_selection()
                cost_calculator()
                dicts['Seat-Type'] = ride_class
                dicts['no of seats'] = seats
                dicts['Fare-Cost'] = total_cost

            elif update_dec == '2':
                departure_city = dicts['Departure City']
                destination_city = dicts['Arrival-City']
                date_selection()
                time_aloter()
                dicts['Departure-Date'] = final_date
                dicts['Departure-time'] = finalized_time
            else:
                print('canceling update proces.....')
                quit()
            with open('tempfile.txt','a') as tfile:
                for k, v in dicts.items():
                    tfile.write(str(k) + ':' + str(v) + '\n')
        else:
            with open('tempfile.txt','a') as tfile:
                for k, v in dicts.items():
                    tfile.write(str(k) + ':' + str(v) + '\n')
                tfile.write('#####\n')
    os.remove('trainrecord.txt')
    os.rename('tempfile.txt','trainrecord.txt')

def all():
    global result
    user_option = input('do you want to start a new booking or update your past booking press 1 for update '
                        'booking details or any other button for start new booking')
    if user_option =='1':
        update_record()
        return
    else:
        user_info()
        city_selection()
        seats_selection()
        date_selection()
        time_aloter()
        cost_calculator()
        global final_fixed_dictionary,final_changeable_dictionary
        final_fixed_dictionary = {'Name': user_name, 'CNIC': CNIC_No, 'Date-of-Birth': birthday,
                            'Departure City': departure_city, 'Arrival-City': destination_city,
                            'Departure-Date': final_date, 'Departure-time': finalized_time,
                            'Seat-Type': ride_class, 'Train-Number': train_number,'no of seats':seats,'Fare-Cost': total_cost}
        print(final_fixed_dictionary)
        with open('trainrecord.txt','a') as file:
            for k,v in final_fixed_dictionary.items():
                file.write(str(k)+'='+str(v)+'\n')
            file.write('#####\n')

        result = [{}]
        with open('trainrecord.txt','r') as inpt:
            for line in inpt:
                if '#####' in line:
                    result.append({})
                else:
                    line = line.split('=')
                    key = line[0]
                    value = line[1]
                    result[-1][key] = value.strip()
        print(result)


all()



