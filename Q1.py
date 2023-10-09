df = elec

# Ploting whole years (90_97)
df_Whole_years=df.groupby(['Weekday'])['Whole_Day'].agg(['mean','max','min'])



print(df_Whole_years.plot(kind='bar',title='Electricity Consumption over the years 90 through 97'))


# Now let's deal with each year
def Annual_Plot(year) :
    if year != df.iloc[-1,1][0:4]:
        df_year=df[(df['Date'] >= str(year)+'/1/1') & (df['Date'] < str(year+1)+'/1/1')]
    else :
        df_year = df[(df['Date'] >= str(year)+'/1/1')]
    df_year = df.groupby(['Weekday'])['Whole_Day'].agg(['mean','max','min'])
    plotted = df_year.plot(kind='bar',title='Electricity Consumption over the year '+str(year))
    return plotted
    
print(Annual_Plot(1390))
print(Annual_Plot(1391))
print(Annual_Plot(1392))
print(Annual_Plot(1393))
print(Annual_Plot(1394))
print(Annual_Plot(1395))
print(Annual_Plot(1396))
print(Annual_Plot(1397))

plt.show()

Annual_Plot(1392) == Annual_Plot(1393)