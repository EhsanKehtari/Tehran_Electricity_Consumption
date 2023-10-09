#Converting WeekDays to numbers
weekday2num={'Sat' : 1 , 'Sun' : 2 , 'Mon' : 
3 , 'Tue' : 4 , 'Wed' : 5   , 'Thu' : 6 , 'Fri' : 7}
elec['Weekday'] = elec['Weekday'].map(weekday2num)

#calculating relative amount of all factors effect on electricity consumption changes

#electricity consumption average for every weekday and finally, relative amount

Weekday_average_elec=[elec.loc[elec['Weekday']==i,'Whole_Day'].mean() for i in range(1,8)]
max_Weekdays_effect=(max(Weekday_average_elec)-min(Weekday_average_elec))/max(Weekday_average_elec)

#Day and Night's' hours effect

max_Day_effect=(max(elec_avarage)-min(elec_avarage))/max(elec_avarage)
s

#Seasons effect

max_Seasons_effect=(max(TECS)-min(TECS))/max(TECS)

#Temperature's changes effect
#using electricity consumption on minimum and maximum temperature

min_elec=float(df_temp.loc[df_temp['t']==df_temp['t'].min(),'elec'])
max_elec=float(df_temp.loc[df_temp['t']==df_temp['t'].max(),'elec'])
max_Temperature_effect=(max_elec-min_elec)/max_elec

#Years effect
#It is clear that as the year goes on, the power consumption increases

max_Years_effect=(elec96_ss-elec90_ss)/elec96_ss

#plotting relative amount of effect VS factors bar chart

print('\n\n\n\n\n')

plt.bar(['Weekdays','Day & Time','Seasons','Temperature','Years'],[max_Weekdays_effect,max_Day_effect,max_Seasons_effect,max_Temperature_effect,max_Years_effect],color='yellow')
plt.xlabel('Factors')
plt.ylabel('Effect')