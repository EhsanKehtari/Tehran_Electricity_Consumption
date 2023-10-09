import pandas as pd
import numpy as np
import matplotlib.pylab as plt


exec(open("C:/It is Me!/University/Programming/Projects/Final Project/date_function.py").read())



elec90_96 = pd.read_excel("C:/It is Me!/University/Programming/Projects/Final Project/Tehran_ElectricityConsumption&Temperature/Tehran_ElectricityConsumption_90to96.xls")
elec97 = pd.read_excel("C:/It is Me!/University/Programming/Projects/Final Project/Tehran_ElectricityConsumption&Temperature/Tehran_ElectricityConsumption_97to97.xlsx")

elec90_96 = elec90_96.dropna(thresh=12)
elec97 = elec97.dropna(thresh=12)



elec90_96.rename(columns={elec90_96.columns[0]: 'Weekday'}, inplace=True)
elec97.rename(columns={elec97.columns[0]:'Weekday',elec97.columns[1]:'Date'}, inplace=True)



columns90_96 = list(elec90_96.columns)

for i in range (len(elec90_96)):
    if not(elec90_96.iloc[len(elec90_96)-i-1,columns90_96.index("Date")] in list(elec97["Date"])):
        break

elec90_96 = elec90_96.iloc[0:len(elec90_96)-i-1 , :]


elec = pd.concat([ elec90_96 , elec97 ], axis=0, join='outer', ignore_index=True, keys=None,
          levels=None, names=None, verify_integrity=False, copy=True)


for i in range(1,25):
     x = elec["T" + str(i)]
     mean = x.mean()
     std = x.std()
     for j in range(len(elec)):
         if abs(elec.loc[j , "T" + str(i)] - mean ) > 3*std:
             elec.loc[j , "T" + str(i)] = np.nan
             


elec = elec.interpolate(method ='linear', limit_direction ='forward')
 
elec['Whole_Day']=elec.iloc[:,2:].sum(1)


# To check if we have 7 unique names of weekdays
len(elec.Weekday.unique()) == 7

# Replacing the corrupt ones
elec=elec.replace(to_replace = elec.Weekday.unique()[-1] , value = elec.Weekday.unique()[2])

# replacing weekdays with their representive numbers
weekday2num={elec.Weekday.unique()[0]:3 , elec.Weekday.unique()[1]:4 , elec.Weekday.unique()[2]:5 , elec.Weekday.unique()[3]:6 , elec.Weekday.unique()[4]:7 , elec.Weekday.unique()[5]:1 , elec.Weekday.unique()[6]:2}
elec['Weekday']=elec['Weekday'].map(weekday2num) 

num2weekday={1:'Sat' , 2:'Sun' , 3:'Mon' , 4:'Tue' , 5:'Wed' , 6:'Thu' , 7:'Fri'}

elec['Weekday'] = elec['Weekday'].map(num2weekday)


#elec.to_csv("C:/It is Me!/University/Programming/Projects/Final Project/final_dataframe_Electricity.csv")



exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q7.py").read())

exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q1.py").read())


exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q2.py").read())

exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q3.py").read())


exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q4.py").read())

#df_temp.to_csv("C:/It is Me!/University/Programming/Projects/Final Project/final_dataframe_Temperature.csv")

exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q6.py").read())

exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Q5.py").read())


