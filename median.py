import math

marks = [2, 9, 8, 6, 1, 13, 20, 17, 6, 8, 12, 14, 21, 24]

marks.sort()

print(marks)
total = len(marks)

if ((total %2) == 0):
    is_even = True
else:
    is_even = False

if (is_even==False):
    print(marks[math.floor(total / 2)])

else:
    print((marks[math.floor((total/2)-1)] + marks[math.floor(total/2)])/2)

    meadian = (marks[math.floor((total/2)-1)] + marks[math.floor(total/2)])/2
