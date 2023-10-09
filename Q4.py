df_temp = pd.read_csv('C:/It is Me!/University/Programming/Projects/Final Project/Tehran_ElectricityConsumption&Temperature/Tehran_Temperature.csv' , skiprows=2)
df_temp = df_temp[['data','t']]
df_temp = df_temp.dropna()
df_temp = df_temp[((df_temp['data']!='data') & (df_temp['t']!='t'))]
df_temp['t'] = df_temp['t'].astype(float)
sep = df_temp['data'].str.split(' ', expand = True)
df_temp['Date'] = sep[0]
df_temp['Time'] = sep[1]
df_temp = df_temp.drop('data',axis=1)
df_temp['Date'] = df_temp['Date'].map(gregorian_to_jalali)

# rearranging columns
df_temp = df_temp[['Date','Time','t']]
df_temp = df_temp[(df_temp['Date'] >= elec.iloc[0,1]) & (df_temp['Date'] <= elec.iloc[-1,1])]
df_temp = df_temp.reset_index(drop=True)

#using Date column as two DataFrames index

elec_index_original = elec.index

elec.index=elec['Date']
df_temp.index=df_temp['Date']

#removing rows with uncommon index

rows_to_remove=list(set(df_temp.index)-set(elec.index))
df_temp=df_temp.drop(rows_to_remove)

def TimeFormatChange(T):
  if T=='00:00':
    return 'T24'
  else:
    T=T.replace(':00','')
    if T[0]=='0':
      T=T.replace('0','T')
      return T
    else:
      return 'T'+T

def split(Str):
    Str=Str.split(' ')
    return Str

#a simple way to get rid of using a bivariate function to add electricity consumption per hour to df_temp DataFrame

df_temp['elec']=df_temp['Date']+' '+df_temp['Time']
df_temp['elec']=df_temp['elec'].map(split)

def TimeToElictricity(date):
    return elec.loc[date[0],TimeFormatChange(date[1])]

df_temp['elec']=df_temp['elec'].map(TimeToElictricity)

#plotting the electricity consumption vs temperature bar chart

plt.scatter(df_temp['t'],df_temp['elec'])
plt.show()

#amount of correlation between temperature and electricity consumpion

correlation=np.corrcoef(df_temp['t'],df_temp['elec'])[0,1]

print('The value of correlation between temperature and electricity consumption is '+str(correlation)+'.')

#resetting index for other questions 

elec.index = elec_index_original