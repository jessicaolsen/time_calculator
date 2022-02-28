import math


def add_time(start, duration, days = None):
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

    #Determining if adding minutes up adds additional hours
    if new_minutes > 60 : 
        hours_added = new_minutes / 60 
        hours_round = math.floor(hours_added)
        new_hours = new_hours + hours_round
        new_minutes = new_minutes - (60 * hours_round)
        if new_minutes < 10 : 
            new_minutes = '0' + str(new_minutes) 
        else : 
            new_minutes = str(new_minutes)
    elif new_minutes < 10 : 
        new_minutes = '0' + str(new_minutes)
    else : 
        new_minutes = str(new_minutes)

    #Determing Day count
    if new_hours > 24 : 
        num_days = new_hours / 24
        day_num = int(num_days)
        day_count = math.floor(day_num)
    
    #Determining which day it is
    if day_count == 1 : 
        day = '(next day)'
    elif day_count == 0 : 
        day = ''
    else : 
        day = '(' + str(day_count) + ' days later)'

    #Converting New added time back to 24-hour Day
    if new_hours > 24 : 
        new_hours = new_hours - (24 * (day_count))

    #Determining if new time is AM or PM
    if new_hours < 12 : 
        new_am_pm = 'AM'
    else : 
        new_am_pm = 'PM'

    # Converting to time format for return
    if new_am_pm == 'PM' : 
        new_hours = new_hours - 12
        if new_hours == 0 : 
          new_hours = 12
    elif new_hours == 0 : 
        new_hours = 12

    #Determining the Day of the week if one is provided
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if bool(days) == True : 
        week_day = days.lower()
        cap_week = week_day.capitalize()
        index_day = days_of_week.index(cap_week)
        pull_day = index_day + day_count 
        if pull_day <= 6 :
            final_day = ', ' + days_of_week[pull_day]
        else : 
            pull_day = pull_day % 7
            pull_day = math.floor(pull_day)
            final_day = ', ' + days_of_week[pull_day]
    else : 
        final_day =  ''

    if bool(final_day) == True : 
      if bool(day) == True : 
        new_time = str(new_hours) + ':' + new_minutes + ' ' + new_am_pm + final_day + ' ' + str(day)
      else : 
        new_time = str(new_hours) + ':' + new_minutes + ' ' + new_am_pm + final_day
    else : 
      new_time = str(new_hours) + ':' + new_minutes + ' ' + new_am_pm + ' ' + str(day)
    
    return new_time.rstrip()


print(add_time("8:16 PM", "466:02", 'tuesday'))