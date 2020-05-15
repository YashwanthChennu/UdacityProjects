"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    texts.extend(list(reader))
new_list = []
for i in texts:
    new_list.append(i[0])
    new_list.append(i[1])
print("There are {} different telephone numbers in the records.".format(len(set(new_list))))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
