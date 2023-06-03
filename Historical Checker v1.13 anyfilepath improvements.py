#!/usr/bin/env python
# coding: utf-8

# In[1]:


############################################################ IMPORT CELL ###########################################################################
#                               (This cell is for module imports and basic function definitions)                                                   #

import pandas as pd
import os
import sys
import numpy as np
import datetime
pd.options.mode.chained_assignment = None
    
def getList(dict):
    return list(dict.keys())

now = datetime.datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
current_date = f'{now.month}/{now.day}/{now.year}'


# In[12]:


############################################################ PATH INPUT CELL ########################################################################
#                               (This cell is for User filepath input, as well as filepath parsing)                                                 #
def path_check(path):
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]
    else:
        path = path

    path_split = path.split("\\")
    try:
        username = (path_split[2])
    except IndexError:
        username = input('Enter username : ')
    try:
        foldername = (path_split[5])
    except IndexError:
        foldername = 'na'
    try: 
        filename = path_split[7]
    except IndexError:
        try:
            filename= path_split[6]
        except IndexError:
            filename = input('Input filename : ')

    if foldername[:2] == 'RT':
        dealerid = foldername[:7]
    else:
        dealerid = foldername[:6]
        
    
    name = 'User'
    if username == 'jwang':
        name = 'Jason'
    if username == 'emarshall':
        name = 'Ellen'
    if username == 'mkhamarkhanov':
        name = 'Mikhail'
    if username == 'damusin':
        name = 'Dan'
    if username == 'milyaguyev':
        name = 'Max'
    if username == 'awerkheiser':
        name = 'AJ'
    if username == 'kcao':
        name ='Katie'
    if username == 'slevinson':
        name = 'Sam'
    
    return path, username,name, foldername, filename, dealerid


# In[13]:


############################################################ OEM CELL ##############################################################################
#                               (This cell is for parsing the filepath to determine the OEM)                                                       #

def DV_OEM_check(foldername, path):
    if foldername[:2] == 'AC':
        Make = 'ACURA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'AU':
        Make = 'AUDI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'BM':
        Make = 'BMW'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except:
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'BU':
        Make = 'BUICK'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            df = data[(data.Make == "BUICK") | (data.Make == "BUICK TRUCK")]
        except:
            df = data[(data.VehicleMake == "BUICK") | (data.VehicleMake == "BUICK TRUCK")]
    elif foldername[:2] == 'CA':
        Make = 'CADILLAC'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            df = data[(data.Make == "CADILLAC") | (data.Make == "CADILLAC TRUCK")]
        except:
            df = data[(data.VehicleMake == "CADILLAC") | (data.VehicleMake == "CADILLAC TRUCK")]
    elif foldername[:2] == 'CH':
        Make = 'CHEVROLET'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            df = data[(data.Make == "CHEVROLET") | (data.Make == "CHEVROLET TRUCK")]
        except:
            df = data[(data.VehicleMake == "CHEVROLET") | (data.VehicleMake == "CHEVROLET TRUCK")]
    elif foldername[:2] == 'GM':
        Make = 'GM'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            df = data[(data.Make == "GM") | (data.Make == "GM TRUCK")]
        except:
            df = data[(data.VehicleMake == "GM") | (data.VehicleMake == "GM TRUCK")]
    elif foldername[:2] == 'FD':
        Make = "FORD"
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            df = data[(data.Make == "FORD") | (data.Make == "FORD TRUCK")]
        except:
            df = data[(data.VehicleMake == "FORD") | (data.VehicleMake == "FORD TRUCK")]
    elif foldername[:2] == 'HD':
        Make = 'HONDA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make')
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'HY':
        Make = 'HYUNDAI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except:
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'IN':
        Make = 'INFINITI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'JA':
        Make = 'JAGUAR'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'KI':
        Make = 'KIA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'LE':
        Make = 'LEXUS'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'LR':
        Make = 'LAND ROVER'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'MZ':
        Make = 'MAZDA'
        data = pd.read_csv(path, sep = "\t", header = 0, low_memory = False)
        try:
            datagroup = data.groupby('Make')
        except:
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'MB':
        Make = 'MERCEDES-BENZ'
        Make2 = 'MERCEDES'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.VehicleMake == Make]
    elif foldername[:2] == 'MI':
        Make = 'MINI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'NI':
        Make = 'NISSAN'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'PR':
        Make = 'PORSCHE'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            datagroup = data.groupby('Make')
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'SU':
        Make = 'SUBARU'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make')
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'TO':
        Make = 'TOYOTA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try:
            df = data[(data.Make == "TOYOTA") | (data.Make == "TOYOTA TRUCK")]
        except:
            df = data[(data.VehicleMake == "TOYOTA") | (data.VehicleMake == "TOYOTA TRUCK")]
    elif foldername[:2] == 'VO':
        Make = 'VOLVO'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make') 
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'VW':
        Make = 'VOLKSWAGEN'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('Make')
        except: 
            datagroup = data.groupby('VehicleMake')
        df = datagroup.get_group(Make)
    else:
        print("The historical file is a rooftop file.")
        nake = input('Input a Make ... ')
        Make = nake.upper()
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        try: 
            datagroup = data.groupby('VehicleMake') 
        except: 
            datagroup = data.groupby('Make')
        df = datagroup.get_group(Make)
    return data,df,Make


# In[14]:


############################################################ OEM CELL ##############################################################################
#                               (This cell is for parsing the filepath to determine the OEM)                                                       #

def CDK_OEM_check(foldername, path):
    if foldername[:2] == 'AC':
        Make = 'ACURA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'AU':
        Make = 'AUDI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'BM':
        Make = 'BMW'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'BU':
        Make = 'BUICK'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'CA':
        Make = 'CADILLAC'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'CH':
        Make = 'CHEVROLET'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'GM':
        Make = 'GM'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'FD':
        Make = "FORD"
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'HD':
        Make = 'HONDA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == 'HONDA']
    elif foldername[:2] == 'HY':
        Make = 'HYUNDAI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == 'HYUNDAI']
    elif foldername[:2] == 'IN':
        Make = 'INFINITI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == 'INFINITI']
    elif foldername[:2] == 'JA':
        Make = 'JAGUAR'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == 'JAGUAR']
    elif foldername[:2] == 'KI':
        Make = 'KIA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == 'KIA']
    elif foldername[:2] == 'LE':
        Make = 'LEXUS'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'LR':
        Make = 'LAND ROVER'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'MZ':
        Make = 'MAZDA'
        data = pd.read_csv(path, sep = "\t", header = 0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'MB':
        Make = 'MERCEDES'
        Make2 = 'MERCEDES-BENZ'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make | Make2]
    elif foldername[:2] == 'MI':
        Make = 'MINI'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'NI':
        Make = 'NISSAN'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'PR':
        Make = 'PORSCHE'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'SU':
        Make = 'SUBARU'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'TO':
        Make = 'TOYOTA'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    elif foldername[:2] == 'VO':
        Make = 'VOLVO'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
        df = datagroup.get_group(Make)
    elif foldername[:2] == 'VW':
        Make = 'VOLKSWAGEN'
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    else:
        print("The historical file is a rooftop file.")
        nake = input('Input a Make ... ')
        Make = nake.upper()
        data = pd.read_csv(path, sep = "\t", header=0, low_memory = False)
        df = data[data.MakeName == Make]
    return data,df,Make


# In[15]:


############################################################ DMS Check CELL #########################################################################
#                                       (Code in this cell confirms the DMS of the hist.file)                                                    #
def DMS_check(df):
    try:
        dmsgroup = df.groupby('DMSType')
        distinct_DMS = getList(dmsgroup.groups)
        DMS = distinct_DMS[0].upper()
        if DMS not in ('RR', 'ARKONA', 'AUTOMATE'):
            input('DMS is {DMS}, not RR, ARKONA, AUTOMATE, or CDK.')
    except:
        DMS = 'CDK'
    return DMS


# In[21]:


############################################################ MAIN FUNCTION CELL ######################################################################
#                                          (This is where the main checker function lives)                                                          #


def DV_saleChecker(df, Make, data):
    
    
        ##### VIN CHECK #####
    if (df['VehicleVin'].str.len() == 17).sum() == len(df['VehicleVin']):
        VinLen = 1
        print("VINs all good.")
    else:
        VinLen = 0
        dropVin = (len(df['VehicleVin']) - (df['VehicleVin'].str.len() == 17).sum())
        print(df.loc[df['VehicleVin'].str.len() != 17].index)
        df.drop(df.loc[df['VehicleVin'].str.len() != 17].index)
        
        
    ### Wholesales Clearer  
    try:
        df.drop(df.loc[df['SaleType'] == 'W'].index)
    except:
        pass
    
    row_count = len(df.index)
    column_count = len(df.columns)
    
    # Deal type counts and DFs for later use
    if DMS == 'RR':
        try:
            lease_count = len(df.groupby('DealType').get_group('L'))
        except:
            lease_count = 0
        try:
            finance_count = len(df[(df['DealType'] == 'D') & ((df['Term'] >  1))])
        except:
            finance_count = 0
        try:
            leasedf = df[df['DealType'] == 'L']
        except:
            leasedf = pd.DataFrame()
        try:
            financedf = df[(df['DealType'] == 'D') & ((df['Term'] > 1 ) | df['Term'].isnull())]
        except:
            financedf = pd.DataFrame()
        try:
            cashdf1 = df[(df['DealType'] == 'D') & df['Term'].isnull()]
            cashdf2 = df[(df['DealType'] == 'D') & df['Term'] == 0 | 1 ]
            cashcomb = [cashdf1, cashdf2]
            cashdf = pd.concat(cashcomb)
        except:
            cashdf = pd.DataFrame()
        try:
            cash_count = len(cashdf)
        except:
            cash_count = 0
        
    if DMS =='ARKONA':
        try:
            lease_count = len(df[df['DealType']=='L'])
        except:
            lease_count = 0
        try:
            leasedf = df[df['DealType'] == 'L']
        except:
            leasedf = pd.DataFrame()
        try:
            financedf = df[(df['DealType'] == 'R') & ((df['Term'] > 1 ))]
        except:
            financedf = pd.DataFrame()
        try:
            cashdf1 = df[(df['DealType'] == 'R') & df['Term'].isnull()]
            cashdf2 = df[(df['DealType'] == 'R') & df['Term'] == 0 | 1 ]
            cashcomb = [cashdf1, cashdf2]
            cashdf = pd.concat(cashcomb)
        except:
            cashdf = pd.DataFrame()
        try:
            cash_count = len(cashdf)
        except:
            cash_count = 0
        try:
            finance_count = len(df[(df['DealType'] == 'R') & ((df['Term'] > 1))])
        except:
            finance_count = row_count - lease_count - cash_count
            
    if DMS =='AUTOMATE':
        try:
            lease_count = len(df[df['DealType']=='L'])
        except:
            lease_count = 0
        try:
            leasedf = df[df['DealType'] == 'L']
        except:
            leasedf = pd.DataFrame()
        try:
            financedf = df[df['DealType'] == 'F']
        except:
            financedf = pd.DataFrame()
        try:
            cashdf = df[df['DealType']== 'C']
        except:
            cashdf = pd.DataFrame()
        try:
            cash_count = len(cashdf)
        except:
            cash_count = 0
        try:
            finance_count = len(df[(df['DealType'] == 'F')])
        except:
            finance_count = row_count - lease_count - cash_count
            
        
    
    ### CustomerName Clearer
    #df.drop(df.loc[df['CustomerName'].isna()].index)
    
    ##DealNumber Col.Pop
    naDealNo = df['DealNumber'].isna().sum()
    DealNoCount = row_count - naDealNo
    if DealNoCount / row_count > 0.95:
        popDealNos = 1
    else:
        popDealNos = 0
        
    ##CustomerName Col. Pop
    naCustNames = df['CustomerName'].isna().sum()
    CustNameCount = row_count - naCustNames
    if CustNameCount / row_count > 0.95:
        popCustNames = 1
    else: 
        popCustNames = 0
        
    ##CustomerNumber Col. Pop
    naCustNos = df['CustomerNumber'].isna().sum()
    CustNoCount = row_count - naCustNos
    if CustNoCount / row_count > 0.95:
        popCustNos = 1
    else:
        popCustNos = 0
        
    ##VehicleVin Pop.
    naVin = df['VehicleVin'].isna().sum()
    VinCount = row_count - naVin
    if VinCount / row_count > 0.95:
        popVins = 1
    else:
        popVins = 0
        
   ###Years of Data checker!
    earliest = pd.to_datetime(df['ContractDate']).dropna().min()
    earliest_year = earliest.year
    earliest_month = earliest.month
    if current_month - earliest_month >= 0:
        if current_year - earliest_year >= 7:
            years = 1
        else:
            years = 0
    else:
        if current_year - earliest_year > 7:
            years = 1
        else:
            years = 0
    
    
    ###Email checker ###
    naEmail = df['CustomerEmail'].isna().sum()
    if naEmail > row_count * 0.25:
        emails = 0
    else:
        emails = 1
        
   #########################LEASE####################################
    try:
        leaseDF = df[df['DealType'] == 'L']
    except:
        leaseDF = 0
        
    if (leaseDF['RetailPayment'] == leaseDF['LeasePayment']).all() == True:
        equalRL = 1
    else:
        equalRL = 0
        try:
            RLloc = df.loc[(df['RetailPayment'] == df['LeasePayment']).all() == False].index.values + 2
        except:
            RLloc = 0
        
    avgLeasePayment = leaseDF['LeasePayment'].sum() / len(leaseDF['LeasePayment'])
    
    ### Automatic LeaseRate divider   
    leaseDF['LeaseRate'] = [x/2400 if x>0.1 else x for x in leaseDF['LeaseRate']]
    
    naLeaseRate = leaseDF['LeaseRate'].isna().sum()
    leaserate_count = lease_count - naLeaseRate
    
    if leaserate_count / lease_count > 0.95:
        popLeaseRates = 1
    else:
        popLeaseRates = 0
    
    minLeaseRate = leaseDF['LeaseRate'].min()
    maxLeaseRate = leaseDF['LeaseRate'].max()
    avgLeaseRate = leaseDF['LeaseRate'].sum() / lease_count
    
    if avgLeaseRate > .0001:
        if avgLeaseRate <.0099999:
            avgLeaseRates = 1
        else: 
            avgLeaseRates = 0
    else:
        avgLeaseRates = 0
        
    if minLeaseRate < 0:
        minLeaseRates = 0
    else:
        minLeaseRates = 1
        
    if maxLeaseRate > .1 :
        maxLeaseRates = 0
    else:
        maxLeaseRates = 1
        
    ## Residual
    naRA = leasedf['ResidualAmount'].isna().sum()
    popRA = len(leasedf['ResidualAmount']) - naRA
    if popRA / lease_count < 0.95:
        RA = 0
    else:
        RA = 1
        
    avgRV = leasedf['ResidualAmount'].sum() / lease_count
    
    if Make in ('ACURA','TOYOTA', 'HONDA', 'CHEVROLET', 'CHEVROLET TRUCK', 'GMC', 'GMC TRUCK', 'HYUNDAI', 'MAZDA', 'MINI','NISSAN', 'SUBARU','VOLVO','VOLKSWAGEN'):
        if avgRV > 15000 and avgRV < 32500:
            avgRVs = 1
        else:
            avgRVs = 0
    elif Make in ('BMW', 'MB', 'AUDI', 'BUICK','BUICK TRUCK','CADILLAC','CADILLAC TRUCK','GENESIS','INFINITI','JAGUAR','LAND ROVER','LEXUS','PORSCHE'):
        if avgRV > 32500 and avgRV < 50000:
            avgRVs = 1
        else:
            avgRVs = 0
    else:
        avgRVs = 0
        
    ## Net Cap Cost
    avgNCC = leasedf['LeaseNetCapCost'].sum() / lease_count
    if avgNCC > 30000:
        if avgNCC < 95000:
            avgNCCs = 1
        else:
            avgNCCs = 0
    else:
        avgNCCs = 0
    
    ## LEASE MILEAGE
    naLAM = leasedf['LeaseAnnualMiles'].isna().sum()
    naLEM = leasedf['LeaseEstimatedMiles'].isna().sum()
    if naLAM > 0.05 * lease_count and naLEM > 0.05 * lease_count:
        LAMLEM = 0
    else:
        LAMLEM = 1
        
    ### Drive Off includes Rebate
    leasedf['RebateminusDriveoff'] = leasedf['Rebate'] - leasedf['TotalDriveOffAmount'] 
    sumDOR = ((leasedf['RebateminusDriveoff']) > 0).sum()
    if sumDOR > 0:
        DORs = 1
    else:
        DORs = 0
    
    #####################APRs / FINANCE################
        
    naAPR = financedf['APRRate'].isna().sum()
    APR_count = finance_count - naAPR
    minAPR = financedf['APRRate'].min()
    if APR_count / finance_count > 0.95:
        popAPR = 1
    else:
        popAPR = 0
    
    avgAPR = financedf['APRRate'].sum() / finance_count
    maxAPR = financedf['APRRate'].max()
    minAPR = financedf['APRRate'].min()
    
    if minAPR < 0:
        minAPRs = 0
    else:
        minAPRs = 1
        
    if maxAPR > 29:
        maxAPRs = 0
    else:
        maxAPRs = 1
        
    if avgAPR > 1:
        if avgAPR < 8:
            avgAPRs = 1
        else:
            avgAPRs = 0
    else:
        avgAPRs = 0
    
    naAmountFinanced = financedf['AmountFinanced'].isna().sum()
    if naAmountFinanced > finance_count * 0.05:
        popAmountFinanced = 0
    else:
        popAmountFinanced = 1
        
    ### DOWN PAYMENT
    naDown = leasedf['DownPayment'].isna().sum()
    if naDown > 0.5 * row_count:
        popDown = 0
    else:
        popDown = 1
        
    ### Cash 
    naCashP = cashdf['CashPrice'].isna().sum()
    if naCashP / cash_count > 0.05:
        CashPs = 0
    else:
        CashPs = 1
        
    ### ZIP CHECK
    naZIP = df['CustomerZip'].isna().sum()
    if naZIP > 0.10 * row_count:
        popZIP = 0
    else:
        popZIP = 1
    
    ### Salesman Name Check
    naSName = df['Salesman_1_Name'].isna().sum()
    if naSName > 0.05 * row_count:
        popSName = 0
    else:
        popSName = 1
    ### Final Check
    red_list = [DORs, equalRL, avgRVs,avgNCC,CashPs, avgAPRs,minAPRs,maxAPRs,popSName,popZIP,popDown,popAmountFinanced,popAPR,
                     LAMLEM,avgLeaseRates,popLeaseRates,years,popCustNames,popDealNos,popDown,
                     popAmountFinanced, emails, popCustNos, RA]
    if finance_count == 0:
        print("Note : No finance deals.")
    if lease_count == 0:
        print("Note : No lease deals.")
    if cash_count == 0:
        print("Note : No cash deals.")
        
    if 0 in red_list:
        status = 'red'
        print("CHECK STATUS : RED -- PLEASE CHECK OR ESCALATE.")
        details = 'y'
    else:
        status = 'green'
        input ("CHECK STATUS : GREEN -- GOOD FOR UPLOAD!")
        details = 'n'
    description = []
    
    if details == 'y':
        if RA == 0:
            print(f'Blanks in Residual Amount : {naRA} / {lease_count}')
            description.append(f'Blanks in Residual Amount : {naRA} / {lease_count}')
        if emails == 0:
            print(f'Blanks in CustomerEmail : {naEmail} / {row_count}.')
            description.append(f'Blanks in CustomerEmail : {naEmail} / {row_count}.')
        if equalRL == 0:
            print(f'Retail Payment not equal to Lease Payment for Lease Deals at rows : {RLloc}')
            description.append(f'Retail Payment not equal to Lease Payment for Lease Deals at rows : {RLloc}')
        if avgRVs == 0:
            print(f'Average ResidualAmount incorrect : {avgRV} for {Make}')
            description.append(f'Average ResidualAmount incorrect : {avgRV} for {Make}')
        if avgNCC == 0:
            print(f'Average LeaseNetCapCost incorrect : {avgNCCs}')
            description.append(f'Average LeaseNetCapCost incorrect : {avgNCCs}')
        if CashPs == 0:
            print(f'Blanks in CashPrice : {naCashP} / {cash_count}')
            description.append(f'Blanks in CashPrice : {naCashP} / {cash_count}')
        if avgAPRs == 0:
            print(f'Average APR incorrect : {avgAPR}')
            description.append(f'Average APR incorrect : {avgAPR}')
        if minAPRs == 0:
            print(f'Minimum APR : {minAPR}')
            description.append(f'Minimum APR too low : {minAPR}')
        if maxAPRs == 0:
            print(f'Max APR : {maxAPR}')
            description.append(f'Max APR too high : {maxAPR}')
        if popSName == 0:
            print(f'Blanks in Salesman_1_Name :  {naSName} / {row_count}')
            description.append(f'Blanks in Salesman_1_Name :  {naSName} / {row_count}')
        if popZIP == 0:
            print(f'Blanks in CustomerZip : {naZIP} / {row_count}')
            description.append(f'Blanks in CustomerZip : {naZIP} / {row_count}')
        if popDown == 0:
            print(f'Blanks in DownPayment : {naDown} / {row_count}')
            description.append(f'Blanks in DownPayment : {naDown} / {row_count}')
        if popAmountFinanced == 0:
            print(f'Blanks in AmountFinanced : {naAmountFinanced} / {finance_count}')
            description.append(f'Blanks in AmountFinanced : {naAmountFinanced} / {finance_count}')
        if popAPR == 0:
            print(f'Blanks in APRRate : {naAPR} / {finance_count}')
            description.append(f'Blanks in APRRate : {naAPR} / {finance_count}')
        if LAMLEM == 0:
            print(f'Blanks in LAM : {naLAM} / {lease_count}. \n Blanks in LEM :{naLEM} / {lease_count}')
            description.append(f'Blanks in LAM : {naLAM} / {lease_count}. \n Blanks in LEM :{naLEM} / {lease_count}')
        if avgLeaseRates == 0:
            print(f'Average LeaseRate : {avgLeaseRate}')
            description.append(f'Average LeaseRate : {avgLeaseRate}')
        if popLeaseRates == 0:
            print(f'Blanks in LeaseRate : {naLeaseRate} / {lease_count}')
            description.append(f'Blanks in LeaseRate : {naLeaseRate} / {lease_count}')
        if years == 0:
            print(f'You do not have 7 years of data! Earliest contract date : {earliest}')
            description.append(f'You do not have 7 years of data! Earliest contract date : {earliest}')
        if popCustNos == 0:
            print(f'Blanks in CustomerNumbers : {naCustNos} / {row_count}')
            description.append(f'Blanks in CustomerNumbers : {naCustNos} / {row_count}')
        if popCustNames == 0:
            print(f'Blanks in CustomerNames : {naCustNames} / {row_count}')
            description.append(f'Blanks in CustomerNames : {naCustNames} / {row_count}')
        if popDealNos == 0:
            print(f'Blanks in DealNumbers : {naDealNos} / {row_count}')
            description.append(f'Blanks in DealNumbers : {naDealNos} / {row_count}')
        if DORs == 0:
            if DMS == 'ARKONA':
                print('No DriveOff Data because DMS is ARKONA')
            else:
                print(f'TotalDriveOffAmount potentially includes Rebate! {sumDOR} negative values! Please check!')
                print(leasedf[['TotalDriveOffAmount','Rebate','Total Down']].iloc[:30])
                description.append(f'TotalDriveOffAmount potentially includes Rebate! Amount of negative values in difference : {sumDOR}')
    description2 = str(description).strip('[]')
    return(status, description2)


# In[17]:


def CDK_sale_checker(df, Make, data):
    
    row_count = len(df)
    leasedf = df[df['SaleType'] == 'Lease']
    financedf = df[df['SaleType'] == 'Finance']
    cashdf = df[df['SaleType'] == 'Cash']
    
    if (df['Vin'].str.len() == 17).sum() == len(df['Vin']):
        VinLen = 1
    else:
        VinLen = 0
        dropVin = (len(df['VehicleVin']) - (df['VehicleVin'].str.len() == 17).sum())
        df.drop(df.loc[df['VehicleVin'].str.len() != 17].index)
        
        ###Years of Data checker!
    earliest = pd.to_datetime(df['ContractDate']).dropna().min()
    earliest_year = earliest.year
    earliest_month = earliest.month
    if current_month - earliest_month >= 0:
        if current_year - earliest_year >= 7:
            years = 1
        else:
            years = 0
    else:
        if current_year - earliest_year > 7:
            years = 1
        else:
            years = 0
            
    naDealNo = df['DealNo'].isna().sum()
    if naDealNo > 0:
        DealNos = 0
    else:
        DealNos = 1
        
    avgLeasePayment = leasedf['LeasePayment'].sum() / len(leasedf['LeasePayment'])
    if 300 < avgLeasePayment < 1000:
        avgLeasePayments = 1
    else:
        avgLeasePayments = 0
        
    maxSellRate = leasedf['SellRateLMF'].max()
    
    if maxSellRate < 0.1:
        maxSellRates = 1
    else:
        maxSellRates = 0
        
    avgLeaseEndValue = leasedf['LeaseEndValue'].sum() / len(leasedf['LeaseEndValue'])
    if 18000 < avgLeaseEndValue < 60000:
        avgLeaseEndValues = 1
    else:
        avgLeaseEndValues = 0
        
    avgLFinanceAmount = leasedf['FinanceAmt'].sum() / len(leasedf['FinanceAmt'])
    if 30000 < avgLFinanceAmount < 97500:
        avgLFinanceAmounts = 1
    else:
        avgLFinanceAmounts = 0
        
    naCCDown = leasedf['CustomerCashDown'].isna().sum()
    if naCCDown == 0:
        popCCDowns = 1
    else:
        popCCDowns = 0
        
    naAmountDAS = leasedf['AmountDueAtStart'].isna().sum()
    if naAmountDAS == 0:
        popAmountDAS = 1
    else:
        popAmountDAS = 0
        
    naMSRP = df['MSRP'].isna().sum()
    if naMSRP == 0:
        popMSRP = 1
    else:
        popMSRP = 0
        
    naLMA = leasedf['LeaseMileageAllowance'].isna().sum()
    na_ME = leased['MileageExpeced'].isna().sum()
    if naLMA == 0 or na_ME == 0:
        popMileage = 1
    else:
        popMileage = 0
        
    naCashP = cashdf['CashPrice'].isna().sum()
    if naCashP == 0:
        popCashP = 1
    else:
        popCashP = 0
    
    avgFinanceAmt = financedf['FinanceAmt'].sum() / len(financedf['FinanceAmt'])
    if 22500 < avgFinanceAmt < 70000:
        avgFinanceAmts = 1
    else:
        avgFinanceAmts = 0
        
    avgAPR = financedf['SellRateAPR'].sum() / len(financedf['SellRateAPR'])
    if 1.5 < avgAPR < 6:
        avgAPRs = 1
    else:
        avgAPRs = 0
        
    avgPaymentAmt = financedf['PaymentAmt'].sum() / len(financedf['PaymentAmt'])
    if 250 < avgPaymentAmt < 1000:
        avgPaymentAmts = 1
    else:
        avgPaymentAmts = 0
        
    avgCashDown = financedf['CashDown'].sum() / len(financedf['CashDown'])
    if 300 < avgCashDown < 1000:
        avgCashDowns = 1
    else:
        avgCashDowns = 0
        
    naCashDown = df['CashDown'].isna().sum()
    if naCashDown < 0.5 * len(df['CashDown']):
        popCashDown = 1
    else:
        popCashDown = 0
    
    red_list = [VinLen, years, DealNos, avgLeasePayments, maxSellRates, avgLeaseEndValues, avgLFinanceAmounts, popCCDowns,
               popAmountDAS,popMileage, popCashP, avgFinanceAmts, avgAPRs, avgPaymentAmts, avgCashDowns, popCashDown]
            
    if 0 in red_list:
        status = 'red'
        print("CHECK STATUS : RED -- PLEASE CHECK OR ESCALATE.")
        details = 'y'
    else:
        status = 'green'
        input ("CHECK STATUS : GREEN -- GOOD FOR UPLOAD!")
        details = 'n'
    description = []

    if details == 'y':
        if VinLen == 0:
            print(f'Not all VINs are 17 length. Please check in Linqpad.')
        if years == 0:
            print(f'Do not have 7 years of data! The earliest contract date is {earliest}.')
        if DealNos == 0:
            print(f'Missing {naDealNo} deal numbers out of {row_count} deals.')
        if avgLeasePayments == 0:
            print(f'Average Lease Payments not in range : {avgLeasePayment}')
        if maxSellRates == 0:
            print(f'Max MoneyFactor too high : {maxSellRate}')
        if avgLeaseEndValues == 0:
            print(f'Average Lease End Values not in range : {avgLeaseEndValue}')
        if avgLFinanceAmounts == 0:
            print(f'Average FinanceAmt for Lease (NCC) out of range : {avgLFinanceAmount}')
        if popCCDowns == 0:
            print(f'Missing {naCCDown} values from CustomerCashDown')
        if popAmountDAS == 0:
            print(f'Missing {naAmountDAS} values from AmountDueAtStart')
        if popMileage == 0:
            if naLMA == 0:
                print(f'Missing {na_ME} values from MileageExpected')
            if na_ME == 0:
                print(f'Missing {naLMA} values from LeaseMileageAllowance')
        if popCashP == 0:
            print(f'Missing {naCashP} / {len(cashdf)} from CashPrice')
        if avgFinanceAmts == 0:
            print(f'Average Finance Amounts out of range : {avgFinanceAmt}')
        if avgAPRs == 0:
            print(f'Average APR out of range : {avgAPR}')
        if avgPaymentAmts == 0:
            print(f'Average Payment Amounts out of range : {avgPaymentAmt}')
        if avgCashDowns == 0:
            print(f'Average Cash Down out of range :')
    return(status, description2)


# In[18]:


def Deleter(data):
    try:
        data.drop(data.loc[data['VehicleVin'].str.len() != 17].index)
    except:
        pass
    try:
        data.drop(data.loc[data['CustomerName'].isna()].index)
    except:
        pass
    try: 
        data['CustomerZip'] = [str(x).zfill(5) if str(x).len() > 4 else x for x in data['CustomerZip']]
    except:
        pass
    new_filename = (filename[:-4] + "_FIXED.TXT")
    save_path = os.path.join(path[:-33],new_filename)
    try:
        data.to_csv(save_path, sep='\t', index= False)
    except:
        save_path = os.path.join(path[:-34],new_filename)
        data.to_csv(save_path, sep='\t', index= False)
    print(f"FIXED FILE CREATED AT {save_path}")


# In[19]:


############################################################ CONFIRMATION CELL ######################################################################
#                                          (PDT Members will confirm information from this cell)                                                    #
def confirm(username, dealerid, Make):
    input(f'Hello {username}, the data for {dealerid} will be filtered for {Make}.\nPress Enter to confirm.\n')


# In[22]:


while True: 
    path = input("Please enter the path for the file you want to check...\n")
    path, username,name, foldername, filename, dealerid = path_check(path)
    data, df, Make = DV_OEM_check(foldername, path)
    DMS = DMS_check(df)
    confirm(username, dealerid, Make)
    if DMS in ['RR', 'ARKONA','AUTOMATE']:
        status, description2 = DV_saleChecker(df, Make, data)
    elif DMS == 'CDK':
        status, description2 = CDK_sale_Checker(df, Make, data)
    #log = pd.read_csv(r"C:\Users\jwang\automotiveMastermind\Data Ingestion - Documents\Onboarding\Automated Checker\Python Files\log\log.csv")
    #log = log.dropna()
    #log_list = []
    #log_list.append(current_date)
    #log_list.append(username)
    #log_list.append(dealerid)
    #log_list.append(status)
    #log_list.append(description2)
    #log_length = len(log)
    #log.loc[log_length] = log_list
    #log.to_csv(r"C:\Users\jwang\automotiveMastermind\Data Ingestion - Documents\Onboarding\Automated Checker\Python Files\log\log.csv", index=False)
    #new = input("Would you like to create a new historical with improper VINs deleted, blank CustomerNames deleted and leading zeroes filled in for CustomerZip?(y/n)")
    if new == 'y':
        Deleter(data)
    else:
        pass
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
        
    if answer == 'y':
        continue
    else:
        input("Goodbye. Press enter to close.")
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




