exec(open("C:/It is Me!/University/Programming/Projects/Final Project/Days_Passed.py").read())
exec(open("C:/It is Me!/University/Programming/Projects/Final Project/date_function.py").read())


# Opening the desired sheet in excel file
file = pd.ExcelFile("C:/It is Me!/University/Programming/Projects/Final Project/Tehran_ElectricityConsumption&Temperature/Tehran_ElectricityConsumption_90to96.xls")
df_loadshed = pd.read_excel(file,'Loadshed')

# The last 2 columns are incomplete and spare
df_loadshed.drop(df_loadshed.columns[[-1,-2]] , axis=1 , inplace=True)

#####  
# Dealing with the weekday names
df_loadshed.rename(columns={df_loadshed.columns[0]:'Weekday'}, inplace=True)

Date_jal = df_loadshed[['Date']]
df_loadshed['Date'] = df_loadshed['Date'].map(jalali_to_gregorian)
Date_gre = df_loadshed['Date']
df_loadshed['Date'] = pd.to_datetime(df_loadshed['Date'])
df_loadshed['Weekday'] = df_loadshed['Date'].dt.day_name()

#####

# Replacing Nan with '0'
df_loadshed = df_loadshed.fillna(0)

##### Now analyzing The DATA ...

# Defining a function to give the value of loadshed in a specific time 
def locate(date,at) :
    """
    Given date and time, "locate" function finds the date's loadshed
    Raises error for inputs not included in the data frame
    """
    
    if not jalali_to_gregorian(date) in Date_gre.values  :
        raise Exception(' No data match')
    
    value = df_loadshed.loc[df_loadshed['Date'] == jalali_to_gregorian(date)]['T'+str(at)]
    value = value.to_frame()
    print( 'Loadshed on ' + date + ' at ' + str(at) + ' is ' + str(value.iloc[0,0]) )

# Defining a function to return the occurence(s) of loadshed over a specific date range at the desired time 
def occurrence(start,stop,hour='Whole Day') :
    """
    Given inputs, "occurrence" function returns how many times loadshedding has occurred over the specified range
    
    start: the beginning date
    stop: the ending date
    hour: (defult: Whole Day) desired time 
    
    Capable of changing "start" and "stop" when "start" is ahead of "stop" on timeline
    Raises error for inputs not included in the data frame
    """
    
    if Days_Passed(stop) - Days_Passed(start) < 0 :
        start,stop = stop,start
    
    if not jalali_to_gregorian(stop) in Date_gre.values  :
        raise Exception(' No data match')
    
    df = df_loadshed[(df_loadshed['Date'] >= jalali_to_gregorian(start)) & (df_loadshed['Date'] <= jalali_to_gregorian(stop))]
    
    if hour != 'Whole Day' :
        repetition = sum(df['T'+str(hour)] != 0)
        percentage = (repetition/(Days_Passed(stop) - Days_Passed(start)))*100
        print( 'The number of loadshed occurrence(s) from ' + str(start) + ' through ' + str(stop) + ' at ' + str(hour) + ' is : ' + str(repetition) ) 
        print( 'Percentage : ' + str(round(percentage,2)) + ' %')
    else :
        df['Whole_Day']=df_loadshed.iloc[:,2:].sum(1)
        repetition = sum(df['Whole_Day'] != 0)
        percentage = (repetition/(Days_Passed(stop) - Days_Passed(start)))*100
        print( 'The number of loadshed occurrence(s) from ' + str(start) + ' through ' + str(stop) + ' over Whole Day ' + ' is : ' + str(repetition) )
        print( 'Percentage : ' + str(round(percentage,2)) + ' %')
        
# Defining a function to plot a date range for futher visualization of loadshed
def plot_the_range(start,stop,maximum=False) :
    """
    Given inputs, "plot_the_range" function returns the plot of loadshedding data over the specified range

    start: the beginning date
    stop: the ending date
    maximum: (default: False) maximum loadshed
     
    Capable of changing "start" and "stop" when "start" is ahead of "stop" on timeline
    Raises error for inputs not included in the data frame

    """
    
    if Days_Passed(stop) - Days_Passed(start) < 0 :
        start,stop = stop,start
    
    if not jalali_to_gregorian(stop) in Date_gre.values  :
        raise Exception(' No data match')
    
    df = df_loadshed[(df_loadshed['Date'] >= jalali_to_gregorian(start)) & (df_loadshed['Date'] <= jalali_to_gregorian(stop))]
    df['Whole_Day'] = df_loadshed.iloc[:,2:].sum(1)
    
    plt.xticks(rotation=45)
    
    if maximum == True :
        Max = (df['Whole_Day'] == max(df['Whole_Day']))
        Max_index = df.index[Max].tolist()
        
        print ('Maximum loadshed from ' + str(start) + ' through ' + str(stop) + ' is in ' + '&'.join(list((Date_jal.iloc[Max_index]).iloc[0])) + ' with a value of ' + str(round(max(df['Whole_Day']),2)))   
        return plt.plot(df['Date'],df['Whole_Day'])
    else :
        return plt.plot(df['Date'],df['Whole_Day'])
    
    
locate('1390/1/5',1)    
occurrence('1395/2/14','1392/7/15')    
plot_the_range('1395/07/01','1395/12/29')
plot_the_range('1395/01/01','1395/6/31')
