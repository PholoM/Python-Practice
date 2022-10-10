####demo for mode

marks = [2, 9, 8, 6, 1, 13, 20, 17, 6, 8, 12, 14, 21, 24]
counter = 0

for index in marks:
    if counter <= marks.count(index):
        counter = marks.count(index)
        mode = index

print("The mode is " + str(mode))

