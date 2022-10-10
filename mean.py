###mean calculation
from median import marks

total=0
size = len(marks)

for index in marks:
    total += index

mean = total/size
print(mean)


