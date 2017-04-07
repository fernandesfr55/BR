import csv
import matplotlib.pyplot as plt

in_f = 'BR_SMA_3.csv' #input file
ofr = open(in_f, 'r') #open input file for reading
r = csv.reader(ofr, delimiter=';') #read file
rec = next(r) #pass the first line
a_dates = [] #array of dates
a_closes = [] #array of closes
a_sma_10 = [] #
a_sma_20 = [] #
a_sma_30 = [] #
i = 0
for rec in r:
    i += 1
    a_dates.append(i) #fill array with date number
    a_closes.append(float(rec[2])) #fill array with closes
    a_sma_10.append(float(rec[3])) #
    a_sma_20.append(float(rec[4]))
    a_sma_30.append(float(rec[5]))
min_d = min(a_dates) #min value in array
max_d = max(a_dates) #min value in array
min_c = min(a_closes) - 1
max_c = max(a_closes) + 1


plt.plot(a_dates, a_closes, a_dates, a_sma_10,
         a_dates, a_sma_20, a_dates, a_sma_30) #Xaxis values, Yaxis values
plt.axis([min_d, max_d, min_c,max_c]) #Xaxis signs, Yaxis signs (min-max)

plt.show() #make chart

print(min_d, max_d, min_c, max_c)

