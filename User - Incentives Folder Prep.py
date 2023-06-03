#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORTANT: CSVs that have the word 'NewCars' will not be removed.
import os
import pandas as pd
import shutil
from datetime import date
import time

##Datetime - Determines the months for identifying and naming folders.
current_year = date.today().strftime('%Y')
current_date = date.today().strftime('%Y-%m')
next_month = str(int(current_date.split('-')[1])+1).zfill(2)
if int(next_month) > 12:
    next_month = '01'
new_date = str(f'{current_year}-{next_month}')


##User Directory Info - Determines the folder names and locates the appropriate directories.
user = os.getlogin()
main_directory = f'C:\\Users\\{user}\\automotiveMastermind\\Data Ingestion - Documents\\Incentives' ##Probably won't change
directory = os.path.join(main_directory, current_date)
ignore_list = [] ##An ignore list, where you can input OEM names and their programs will not be touched
src_path = os.path.join('C:\\Users',user,'automotiveMastermind','aM Data - Manufacturer Programs') 

##Check - User input to determine which parts of the scripts need to be run.
run_csv = input("Do you want to run CSV incentives prep? (y/n)")
run_pdf = input("Do you want to run Manufacturer Programs incentives prep? (y/n)")
run_rename = input("Do you want to run Rename? (y/n)")
manual_date = input("Do you want to input a manual date? (y/n)")

if manual_date == 'y':
    current_date = input("Input manual date. (yyyy-mm)")
    next_month = str(int(current_date.split('-')[1])+1).zfill(2)
    if int(next_month) > 12:
        next_month = '01'
    new_date = str(f'{current_year}-{next_month}')
    directory = os.path.join(main_directory, current_date)

###This block archives the entire monthly incentives sheets folder


if run_csv == 'y':
    copy_csv = shutil.copytree(directory, directory + "_Hist")
    shutil.move(copy_csv, os.path.join(main_directory, "###Historical Documentation###"))
    for dirpath, dirname, file in os.walk(directory):
        for x in file:
            filepath = os.path.abspath(os.path.join(dirpath,x))
            if filepath.rsplit('.')[-1] == 'xlsx':
                if 'Incentives Trend' in filepath:
                    print(x + 'was removed')
                    os.remove(filepath)
            if filepath.rsplit('.')[-1] == 'csv':
                if 'NewCars' in filepath:
                    pass
                else:
                    print(x + ' was removed')
                    os.remove(filepath)
            else:
                pass
    for dirpath, dirname, file in os.walk(directory):
        for x in file:
            if current_date in x:
                filepath = os.path.abspath(os.path.join(dirpath,x))
                if filepath.rsplit('.')[-1] == 'xlsx':
                    new_x = x.replace(current_date, new_date)
                    new_filepath = os.path.join(dirpath,new_x)
                    os.rename(filepath,new_filepath)
                    print(x + " was renamed to " + new_x)
                else:
                    pass
            else:
                pass
    #time.sleep(30)
    #os.rename(os.path.join(main_directory, current_date), os.path.join(main_directory, new_date))

###Manufacturer Programs Folder
if run_pdf == 'y':
    for src, dirs, files in os.walk(src_path):
        if dirs not in ignore_list:
            for dirt in dirs:
                if current_date in dirt:
                    if not dirt.startswith("__"):
                        if not dirt.endswith("_Hist"):
                            copy = shutil.copytree(os.path.join(src,dirt) , os.path.join(src,str(dirt) + "_Hist"))
                            shutil.move(copy, os.path.join(src, "Historical Documentation"))
                            os.rename(os.path.join(src, dirt), os.path.join(src, new_date))
    

for src, dirs, files in os.walk(src_path):
    if new_date in dirs:
        for dirt in dirs:
            if new_date in dirt:
                for file in os.listdir(os.path.join(src,dirt)):
                    if file.endswith('.pdf') or file.endswith('.xlsx') or file.endswith('.rtf') or file.endswith('.pptx') or file.endswith('.docx') or file.endswith('.xls'):
                        os.remove(os.path.join(src,dirt,file))
                        
if run_rename == 'y':
    os.rename(os.path.join(main_directory, current_date), os.path.join(main_directory, new_date))
if run_csv == 'y':
    print("CSV Prep Completed.")
if run_pdf == 'y':
    print("PDF Prep Completed.")


# In[4]:


current_date


# In[ ]:


run_csv_fix = 'y'
current_date = '2023-04'
new_date ='2023-05'
directory = os.path.join(main_directory, current_date)
if run_csv_fix == 'y':
    for dirpath, dirname, file in os.walk(directory):
        for x in file:
            if current_date in x:
                filepath = os.path.abspath(os.path.join(dirpath,x))
                if filepath.rsplit('.')[-1] == 'xlsx':
                    new_x = x.replace(current_date, new_date)
                    new_filepath = os.path.join(dirpath,new_x)
                    os.rename(filepath,new_filepath)
                    print(x + " was renamed to " + new_x)
                else:
                    pass
            else:
                pass


# In[3]:





# In[30]:





# In[ ]:




