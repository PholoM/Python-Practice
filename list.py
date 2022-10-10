#this is an example of lists and functions that operate on lists

#these are lists
books = ["Game of thrones","Romeo and Juliet","The Great Controversy", "Fire and Ice"]
phone_numbers = [71534841, 73143514, 73924770, 76914377]
marks = [50, 55, 70, 62, 85, 66, 44, 55]


#these are tuples
previous_schools=("kelekele", "okavango","shakawe","maruapula")
fruits= ("apple", "banana", "peach", "pineapple")

#functions to be used on either lists or turples
'''
list.append()
list.clear()
list.copy()
list.count() - returns how many times an element appears 
list.extend() - adds iterable elements to the end of the list
list.index(element) - returns the index of the element
list.insert(element, index)
list.pop(index)- removes the element from the given index
list.remove(element)
list.reverse()- reverses the order of the elements
list.sort()- sorts elements of a list

some of these will work with turples but remember that turples cannot be editted
'''
books.append("Oxford Dictionary")
print(books)
print(fruits.count("apple"))
marks.remove(70)
print(marks)
marks.pop()
print(marks)

books.sort()
print(books)
