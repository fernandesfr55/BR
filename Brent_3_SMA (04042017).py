import csv

in_f = 'BR_170102_170327.csv' #input file
ofr = open(in_f, 'r') #open input file for reading
r = csv.reader(ofr, delimiter=';') #read file
out_f = 'BR_SMA_3.csv' #output file
ofw = open(out_f, 'w', newline = '') #open output file ('newline' do not add unwanted line)
w = csv.writer(ofw, delimiter= ';') #write output file
rec = next(r) #go to next line
w.writerow((rec[0], rec[1], rec[5], "<SMA10>", "<SMA20>", "<SMA30>")) #write from input to output
sum_10 = 0 #sum of 10 CLOSE
sum_20 = 0 #sum of 20 CLOSE
sum_30 = 0 #sum of 30 CLOSE
p1 = 10 #period 10
p2 = 20 #period 20
p3 = 30 #period 30
arr = [] #create empty array

#use 30 values of CLOSE
for i in range(p3): #use 30 period for 3 SMA (10, 20, 30)
    rec = next(r) #go to next line
    arr.append(float(rec[5])) #adding CLOSE value from newline to array
sma_10 = sum(arr[-p1:]) / p1 #make slice of last 10 from 30 in array
sma_20 = sum(arr[-p2:]) / p2 #make slice of last 20 from 30 in array
sma_30 = sum(arr) / p3 #use all 30 values
w.writerow((rec[0], rec[1], rec[5] ,sma_10, sma_20 ,sma_30)) #write the result (works with csv.writer)

#delete first value and add the last. work with all file till the end
for rec in r:
    arr.pop(0) #delete the first value
    arr.append(float(rec[5])) #add the current value
    sma_10 = sum(arr[-p1:]) / p1 #make slice of last 10 from 30 in array
    sma_20 = sum(arr[-p2:]) / p2 #make slice of last 10 from 30 in array
    sma_30 = sum(arr) / p3 #use all 30 values
    w.writerow((rec[0], rec[1], rec[5], sma_10, sma_20, sma_30)) #write the result till the end of file

ofr.close() #close readed file
ofw.close() #close writed file
