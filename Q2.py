# Calculating average usage of electricity based on time
elec_avarage = []
for i in range (1,25):
    n = elec["T" + str(i)]
    s = n.values
    elec_avarage.append(int(s.mean()))

# Printing maximum & minimum electricity usage based on average
print("maximum usage of Electricity based on average:")
print("at " ,str(elec_avarage.index(max(elec_avarage)) + 1 ))

print("minimum usage of Electricity based on average:")
print("at " ,str(elec_avarage.index(min(elec_avarage)) + 1 ))

# plotting average usage of electricity based on time
plt.plot(list(elec.columns[2:-1]),elec_avarage ,c = 'darkred')
plt.xlabel('Time')
plt.ylabel('Electricity')
plt.title('Avarage usage of Electricity based on time')
plt.figure(figsize = (100, 50))
plt.show()


# Calculating median usage of electricity based on time
elec_median = []
for i in range (1,25):
    n = elec["T" + str(i)]
    s = n.values
    elec_median.append(int(np.median(s)))

# Printing maximum & minimum electricity usage based on median
print("maximum usage of Electricity based on median:")
print("at " ,str(elec_median.index(max(elec_median)) + 1 ))

print("minimum usage of Electricity based on median:")
print("at " ,str(elec_median.index(min(elec_median)) + 1 ))

# Plotting median usage of electricity based on time
plt.plot(list(elec.columns[2:-1]),elec_median ,c = 'darkred')
plt.xlabel('Time')
plt.ylabel('Electricity')
plt.title('median usage of Electricity based on time')
plt.figure(figsize = (100, 50))
plt.show()

    































