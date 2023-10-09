#using Date rows as DataFrame index
original_index = elec.index
elec.index=elec['Date']
#Separating original Data to Years Data using index

Data90=elec.loc['1390/1/1':'1390/12/29']
Data91=elec.loc['1391/1/1':'1391/12/30']
Data92=elec.loc['1392/1/1':'1392/12/29']
Data93=elec.loc['1393/1/1':'1393/12/29']
Data94=elec.loc['1394/1/1':'1394/12/29']
Data95=elec.loc['1395/1/1':'1395/12/30']
Data96=elec.loc['1396/1/1':'1396/12/28']
Data97=elec.loc['1397/1/1':]

#Separating Data by Seasons

def Year2Season(Year,Season):
    if Season=='Spring':
        y=Year.loc[:'13'+str(Year.index[0])[2:4]+'/3/31']
    elif Season=='Summer':
        y=Year.loc['13'+str(Year.index[0])[2:4]+'/4/1':'13'+str(Year.index[0])[2:4]+'/6/31']
    elif Season=='Fall':
        if str(Year)!=str(Data97):
            y=Year.loc['13'+str(Year.index[0])[2:4]+'/7/1':'13'+str(Year.index[0])[2:4]+'/9/30']
        else:
            y=Year.loc['13'+str(Year.index[0])[2:4]+'/7/1':]
    elif Season=='Winter':
        if str(Year)!=str(Data97):
            y=Year.loc['13'+str(Year.index[0])[2:4]+'/10/1':]
        else:
            return 0
    return y

Seasons_Data=[]
Seasons=['Spring','Summer','Fall','Winter']
Data=[Data90,Data91,Data92,Data93,Data94,Data95,Data96,Data97]
 
for i in Data:
    for j in Seasons:
        Seasons_Data.append(Year2Season(i,j))

#Calculating the Sum of Electricity Consumption for Every Season
#TECS Stands for Total Electricity Consumption per Season

TECS=[]
for i in range(len(Seasons_Data)-1):
    TECS.append(Seasons_Data[i].loc[:,'T1':'T24'].sum().sum())


#PSlotting the Tehran Electricity Consumption VS Years's Seasons Horizontal Bar Chart
#TW Stands for TeraWatt
Names=[]
Year=['90','91','92','93','94','95','96','97']
for i in Year:
    for j in Seasons:
        Names.append(j+i)
Names.remove('Winter97')

import matplotlib.pylab as plt

plt.figure(figsize = (12, 7))
plt.barh(Names,TECS,color=(1,0.5,0.2,1))
plt.ylabel('Year Seasons')
plt.xlabel('Tehran Electricity Consumption')
plt.title('Tehran Electricity Consumption over seasons')
plt.xticks([i*1000000 for i in range(1,9)],[str(i)+'TW' for i in range(1,9)])
plt.show()

#Plotting the Tehran's Average Electricity Consumption VS Seasons Vertical Bar Chart

from numpy import mean

#E=Electricity,SP=Spring,S=Summer,F=Fall,W=Winter

ESP_Mean=mean(TECS[0:len(TECS)+1:4])
ES_Mean=mean(TECS[1:len(TECS)+2:4])
EF_Mean=mean(TECS[2:len(TECS)+3:4])
EW_Mean=mean(TECS[3:len(TECS)+4:4])

plt.bar(Seasons,[ESP_Mean,ES_Mean,EF_Mean,EW_Mean],color=(0.8,0.2,0.6,1))
plt.xlabel('Seasons')
plt.ylabel('Tehran Electricity Consumption')
plt.yticks([i*1000000 for i in range(1,8)],[str(i)+'TW' for i in range(1,8)])
plt.title('Tehran Electricity Consumption over seasons')
plt.show()

#reseting index for other questions

elec.index = original_index