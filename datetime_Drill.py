# Python Version:       2.7.12
#
# Author:               Tanvir Khondakar
#
# Purpose:              Creating a function using datetime that will check to see  




# Importing date time and pytz modules:

import datetime
import pytz


# Defining the time format

fmt = "%H:%M::%S"

def date_time():

    # Finding the current time in Portland, and other cities 
    
    time_portland = datetime.datetime.now(pytz.timezone('US/Pacific'))
    print 'Portland HQ Time:', time_portland.strftime(fmt)
    
    time_newyork = time_portland.astimezone(pytz.timezone('US/Eastern'))
    print 'New York Office Time:', time_newyork.strftime(fmt)

    time_london = time_portland.astimezone(pytz.timezone('Europe/London'))
    print 'London Office Time:', time_london.strftime(fmt)


    # Defining the Naive datetime for the Portland office

    hq_open = datetime.datetime.strptime("09:00:00", '%H:%M:%S')
    hq_close = datetime.datetime.strptime("21:00:00", '%H:%M:%S')

    # Compairing Naive time with actual time to see if office is Open or Closed

    if datetime.datetime.now() >= hq_open < hq_close:
        print("Portland HQ is Open")
    else:
        print("Portland HQ is Closed")

    nyc_open = datetime.datetime.strptime("09:00:00", '%H:%M:%S')
    nyc_close = datetime.datetime.strptime("21:00:00", '%H:%M:%S')
    nyc_open += datetime.timedelta(hours=3) # add 3 hours
    nyc_close += datetime.timedelta(hours=3)

    if datetime.datetime.now() >= nyc_open < nyc_close:
       print("New York Office Open") 
    else:
       print("New York Office Closed")

    lon_open = datetime.datetime.strptime("09:00:00", '%H:%M:%S')
    lon_close = datetime.datetime.strptime("21:00:00", '%H:%M:%S')
    lon_open += datetime.timedelta(hours = 8) # add 8 hours
    lon_close += datetime.timedelta(hours = 8)
    
    if datetime.datetime.now() >= lon_open < lon_close:
       print("London Office Open")
    else:
       print("London Office Closed")
 
    
date_time()
                                          
    
