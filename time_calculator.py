def add_time(start, duration, day = False):
    start_time = start.split()
    beg_time = start_time[0]
    beg_hours = beg_time.split(':')[0]
    beg_minutes = beg_time.split(':')[1]
    am_pm = start_time[1]
    
    add_hours = duration.split(':')[0]
    add_minutes = duration.split(':')[1]
    day_count = 0
    
    #converting to a 24 hour period
    if am_pm == "PM" : 
        beg_hours = int(beg_hours) + 12
    
    #Adding time
    new_hours = int(beg_hours) + int(add_hours)
    new_minutes = int(beg_minutes) + int(add_minutes)

    #Determing Day count
    if new_hours > 24 : 
        num_days = new_hours / 24
        day_count = num_days

    #Determining which day it is
    
    return day_count

    


    #return new_time


print(add_time("11:06 PM", "2:02", 'TueSday'))