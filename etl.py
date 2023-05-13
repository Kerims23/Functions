
"""
Created on Thu Jul  7 16:15:37 2022

@author: KSever
"""
###basic load
#sourcing
from datetime import datetime
from dateutil.relativedelta import relativedelta
#gen lib
import glob
import pandas as pd
import pyodbc
import numpy as np
import sqlalchemy
from sqlalchemy.pool import NullPool
import sys
import os
import time
import datetime
import logging 
import smtplib

print(datetime.today())

sys.path
#insert it path .anaconda not in path
sys.path.insert(0,'c:\\Libraries\\') 

################################### Date ############################################################

#Set month and year for most recent file
today = datetime.today()
if today.day >= 16:
    month_year = str(today.month-1).rjust(2,'0') + str(today.year)
elif today.month == 1:
    month_year = '12' + str(today.year - 1)
else:
    month_year = str(today.month - 1).rjust(2,'0') + str(today.year)


################################### Connection to DB ############################################################

engine = 'engine to sql'


################################### Get this months files ############################################################

print('getting files')


start_date_str = datetime.today().date()  # assuming you want today's date
start_date = datetime.strptime(str(start_date_str), '%Y-%m-%d')  # convert to datetime object
end_date = start_date + relativedelta(months=1)  # add one month
end_date_str = end_date.strftime('%Y-%m-%d')  # convert back to string




def get_files_in_month(directory, year, month, extension=None):
    files_in_month = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if creation_time.year == year and creation_time.month == month:
                if extension is None or file.endswith(extension):
                    files_in_month.append(file_path)
    return files_in_month

year = start_date.year
month = start_date.month
files = get_files_in_month('C:\\test\\', year, month, extension='.txt')
print(files)


print(f'{files}')

