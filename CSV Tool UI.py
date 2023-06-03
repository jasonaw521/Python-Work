#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
import os
import sys
import shutil
import pandas as pd
import numpy as np
from datetime import date
import time

User = os.getlogin()
Date = date.today().strftime('%Y-%m')
if User == 'span':
    dir1 = f'C:\\Users\\{User}\\automotiveMastermind\\Data Ingestion - Incentives'
else:
    dir1 = f'C:\\Users\\{User}\\automotiveMastermind\\Data Ingestion - Documents\\Incentives\\'
savepath = dir1


def oem_list_create():
    global oem_list
    oem_list = []
    global datepath
    datepath = os.path.join(dir1,Date)
    for x, y , z in os.walk(datepath):
        for ys in y:
            if os.path.isdir(os.path.join(datepath,ys)):
                if "_" not in ys:
                    oem_list.append(ys.upper())
    oem_list = oem_list
    
def car_check(file):
    model_count = []
    try:
        df = pd.read_excel(file, sheet_name = 'calc').values
        for x in df:
            if 'Model Count' in x:
                model_count.append(x)
                b = np.where(model_count[0] == 'Model Count')
                break
            if 'Car Count' in x:
                model_count.append(x)
                b = np.where(model_count[0] == 'Car Count')
                break
    except:
        return None
        pass
    return int(model_count[0][b[0]+1])


def robot_check(file):
    field_count = []
    robot_count = []
    try:
        df = pd.read_excel(file, sheet_name = 'calc').values
        for x in df:
            if 'Field Count' in x:
                field_count.append(x)
                b = np.where(field_count[0] == 'Field Count')
                break
    except:
        return None
        pass
    return int(field_count[0][b[0]+1])

def csv_creater(filepath,save_location,dirpath,x):
    dat = pd.read_excel(filepath, sheet_name = 'robot')
    data = dat[dat.notnull().all(1)]
    if os.path.exists(os.path.join(dirpath, 'CSV')):
        data.to_csv(save_location, index= False)
        z = car_check(filepath)
        y = robot_check(filepath)
        print(str(x).replace(".xlsx",".csv") + ' was created, with car count of '  + str(z)  + ', a field count of ' + str(y) + ' and a robot count of '+str(len(data)))
    else:
        os.mkdir(os.path.join(dirpath, 'CSV'))  
        data.to_csv(save, index= False)
        z = car_check(filepath)
        y = robot_check(filepath)
        print(str(x).replace(".xlsx",".csv") + ' was created, with car count of ' + str(z)  + ', a field count of ' + str(y)+ ' and a robot count of '+str(len(data)))
    return


                
                              
class MyView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="none", expand=True)
        self.label = tk.Label(self.frame, text = 'Input OEM')
        self.label.pack()
        self.oem_entry = tk.Entry(self.frame)
        self.oem_entry.pack()
        self.button1 = tk.Button(self.frame, text='Enter',command=self.get_oem)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text='Run CSV tool', command=self.run_csv)
        self.comlabel = tk.Label(self.frame,text = 'Job Complete!')
        self.countlabel = tk.Label(self.frame)

        
    def get_oem(self):
        self.countlabel.pack_forget()
        self.comlabel.pack_forget()
        oem_list_create()
        self.button1.config(text = "Please wait...")
        global oem
        oem = self.oem_entry.get().upper()
        self.label.update_idletasks()
        time.sleep(1)
        print (oem)
        if oem.upper() in oem_list:
            self.button2.pack()
            self.button1.config(text = "Valid Filepath")
        else:
            if self.button2.winfo_exists():
                self.button2.pack_forget()
            self.button1.config(text = "Invalid Input, try again.")
            
    
    def run_csv(self):
        if self.comlabel.winfo_exists():
            self.comlabel.pack_forget()
        time.sleep(1)
        self.button2.config(text = 'Please wait...')
        self.label.update_idletasks()
        time.sleep(1)
        global Date
        global directory
        global oem_list
        oem_list = []
        savepath1 = os.path.join(savepath,Date,oem)
        directory = os.path.join(datepath,oem)
        if os.path.exists(directory) == True:
            directory = directory
        else:
            Date = input("Input Date.")
            directory = os.path.join(datepath,oem)
            savepath1 = os.path.join(savepath,Date, oem)
            print(directory)
        Brand = oem
        totalcount = 0
        curcount = 0
        
        for dirpath, dirnames, file in os.walk(directory):
            for x in file:
                if Date in x:
                    filepath = os.path.abspath(os.path.join(dirpath,x))
                    if filepath.endswith('.xlsx'):
                        totalcount += 2
                    else:
                        pass
                else:
                    pass
                    
        big_count = tk.StringVar(self.frame,"0")
        big_count.set(str(f'{curcount}/{totalcount}'))
        self.countlabel = tk.Label(self.frame,textvariable = big_count)
        self.countlabel.pack_forget()
        self.countlabel.update_idletasks()
        self.countlabel.pack()
        self.countlabel.update_idletasks()
        
        time.sleep(1)
        
        for dirpath, dirnames, file in os.walk(directory):
            for x in file:
                if Date in x:
                    filepath = os.path.abspath(os.path.join(dirpath,x))
                    if filepath.rsplit('.')[-1] == 'xlsx':
                        save = os.path.join(savepath1,'CSV',str(x).replace(".xlsx",".csv"))
                        csv_creater(filepath,save,dirpath,x)
                        time.sleep(1)
                        curcount += 1
                        big_count.set(str(f'{curcount}/{totalcount}'))
                        self.countlabel.update_idletasks()
                    else:
                        pass
                else:
                    pass

        for root,dirs,files in os.walk(directory):
            for file in files:
                if file.endswith(".csv"):
                    file_read = pd.read_csv(os.path.join(root,file))
                    file_non_null = file_read[file_read.notnull().all(1)]
                    file_non_null.to_csv(os.path.join(root,file), float_format = '%g', index = False)
                    print(file + " resaved.")
                    time.sleep(1)
                    curcount += 1
                    big_count.set(str(f'{curcount}/{totalcount}'))
                    self.countlabel.update_idletasks()
        self.button2.config(text = 'Run CSV Tool')
        self.label.update_idletasks()
        self.comlabel.pack()
        
class MyController:
    def __init__(self):
        self.view = None
    def set_view(self, view):
        self.view=view
        
class CSV_APP():
    def __init__(self):
        self.root = tk.Tk()
        self.controller = MyController()
        self.view = MyView(self.root, self.controller)
        self.controller.set_view(self.view)
        
    def run(self):
        self.root.title("CSV Maker v1.0")
        self.root.geometry("500x300")
        self.root.mainloop()
            
if __name__ == '__main__':
    app = CSV_APP()
    app.run()


# In[ ]:





# In[5]:





# In[ ]:




