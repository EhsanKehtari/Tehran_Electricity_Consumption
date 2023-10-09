# Finding where The Years change
elec_y = [0]
for i in range(len(elec)-1):
    if elec['Date'][i][2:4] != elec['Date'][i+1][2:4]:
        elec_y.append(i)
    

# Seperating each year & assigning variables to them        
elec90 = elec.loc[elec_y[0]:elec_y[1]]
elec91 = elec.loc[elec_y[1]+1:elec_y[2]]
elec92 = elec.loc[elec_y[2]+1:elec_y[3]]
elec93 = elec.loc[elec_y[3]+1:elec_y[4]]
elec94 = elec.loc[elec_y[4]+1:elec_y[5]]
elec95 = elec.loc[elec_y[5]+1:elec_y[6]]
elec96 = elec.loc[elec_y[6]+1:elec_y[7]]
elec97 = elec.loc[elec_y[7]+1:]

# Saving data using dictionary
elecyear = {"90":elec90 , "91":elec91 ,"92":elec92 ,"93":elec93 ,"94":elec94 ,"95":elec95 ,"96":elec96 ,"97":elec97 }

# Calculating total electricity usage of each hour for each seperate year
elec90_s = elec90.sum().loc["T1":"T24"]
elec91_s = elec91.sum().loc["T1":"T24"]
elec92_s = elec92.sum().loc["T1":"T24"]
elec93_s = elec93.sum().loc["T1":"T24"]
elec94_s = elec94.sum().loc["T1":"T24"]
elec95_s = elec95.sum().loc["T1":"T24"]
elec96_s = elec96.sum().loc["T1":"T24"]
elec97_s = elec97.sum().loc["T1":"T24"]

# Saving data using dictionary
elecyear_s = {"90":elec90_s , "91":elec91_s ,"92":elec92_s ,"93":elec93_s ,"94":elec94_s ,"95":elec95_s ,"96":elec96_s ,"97":elec97_s }

# Calculating total electricity usage for each seperate year
elec90_ss = elec90.sum().loc["T1":"T24"].sum()
elec91_ss = elec91.sum().loc["T1":"T24"].sum()
elec92_ss = elec92.sum().loc["T1":"T24"].sum()
elec93_ss = elec93.sum().loc["T1":"T24"].sum()
elec94_ss = elec94.sum().loc["T1":"T24"].sum()
elec95_ss = elec95.sum().loc["T1":"T24"].sum()
elec96_ss = elec96.sum().loc["T1":"T24"].sum()
elec97_ss = elec97.sum().loc["T1":"T24"].sum()

# Saving data using dictionary
elecyear_ss = {"90":elec90_ss , "91":elec91_ss ,"92":elec92_ss ,"93":elec93_ss ,"94":elec94_ss ,"95":elec95_ss ,"96":elec96_ss ,"97":elec97_ss }

def yeartime(t):
    """
    Given the hour, yeartime function plots electricity usage over whole years at the given hour
    """
    x = []
    for i in range(90,98):
        x.append(elecyear_s[str(i)]["T" + str(t)])
    y = []
    for i in range (90,98):
        y.append("year" + str(i))
    plt.bar(y , x)
    plt.xlabel('year')
    plt.ylabel('usage of Electricity')
    plt.title('usage of Electricity at ' + str(t))
    plt.show()
    
print(yeartime(2))
    

# Calculating total electricity usage over each year
x=[]
y=[]
for i in range(90,98):
    x.append("year" + str(i))
    y.append(elecyear_ss[str(i)]) 
   

# Plotting total electricity usage over each year
plt.bar(x , y)
plt.xlabel('year')
plt.ylabel('usage of Electricity')
plt.title('total usage of Electricity ')
print("total usage of Electricity:")
plt.show()    
    
      
def eachyearysusage(year = "all"):
    """
    Given the year, eachyearysusage function plots electricity usage over the given year
    if given "all", it plots electricity usage over the whole data 
    """
    if year == "all":
        t = elec["T1"]
        for i in range (2,25):
            t += elec["T" + str(i)]
        x = list( elec["Date"].values)
        y = list (t.values)
        plt.scatter(x , y)
        plt.xlabel('date')
        plt.ylabel('usage of Electricity')
        plt.title('total usage of Electricity over the whole data' )
        plt.show()    
  
    else:
        t = elecyear[str(year)]["T1"]
        for i in range (2,25):
            t += elecyear[str(year)]["T" + str(i)]
    
        x = list( elecyear[str(year)]["Date"].values)
        y = list (t.values)
        plt.scatter(x , y)
        plt.xlabel('date')
        plt.ylabel('usage of Electricity')
        plt.title('total usage of Electricity in 13' + str(year) )
        plt.show()    
  
print(eachyearysusage(92))        
#print(eachyearysusage("all"))   


def alternation(year1 , year2):
    """
    Given the inputs, alternation function returns the diffrence of electricity usage between the tow given years
    
    inputs:
    year1 = the beginning year
    year2 = the ending year
    
    """
    x = elecyear_ss[str(year1)] - elecyear_ss[str(year2)]
    if x > 0:
        y = "Decreased by"
        return y + ': ' + str(abs(x))
    elif x == 0:
        return "Without any change!"
    elif x < 0:
        y = "Increased by"
        return y + ': ' + str(abs(x))
    
print(alternation(90,92))

# Pinting electricity usage increase on average
print("electricity usage increase on average without considering the year 1397 is :")
t = 0
for i in range (90 , 96):
    x = elecyear_ss[str(i+1)] - elecyear_ss[str(i)]
    t = t + x
print (t/(96-90+1))