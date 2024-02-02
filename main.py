import os

import csv


total_months = 0
total_net = 0
Month_of_change = []
net_change_list = []

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]
file_to_load= os.path.join("Resources/budget_data.csv")

print(file_to_load)

with open(file_to_load) as file:
    reader = csv.reader(file)
    header =next(reader) #corrected from csvfile
    first_row=next(reader)  #corrected from csvfile
    total_months +=1
    total_net += int(first_row [1])
    prev_net = int(first_row[1])



    for row in reader:

        total_months +=1

        total_net += int(first_row[1])


        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        Month_of_change+=[row[0]]


      
      
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            print(net_change)                     


        if net_change > greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            print(net_change)                       

print(total_months)
print(total_net)
print(sum(net_change_list) / len(net_change_list)) #net monthly change
            
print(greatest_increase)

print(greatest_decrease)
