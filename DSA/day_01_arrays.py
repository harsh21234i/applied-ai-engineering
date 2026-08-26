#LLargest number
num=[1,2,42,4,2]

max=num[0]
for i in num:
    if i>max:
        max=i

print(max)

#smaller number
number=[1,23,0,43]
smal=num[0]
for j in number:
    if j<smal:
        smal=j
print(smal)

##Array Traversal

array=[1,2,3,4,5,6,7,8,9,10]

for i in array:
    print(i)

##Find the sum
def find_sum(num):
    total=0

    for i in num:
        total+=i
    return total
print(f"total sum is {find_sum([4,3,5,6])}")

##Find the largest element
def largest_num(num):
    if not num:
        return 0

    large=num[0]
    for i in num:
        if i>large:
            large=i
    return large
print(f"latgest number is {largest_num([4,3,5,6,7,8,9,36,413])}")

#Smallest element
def small_element(num):
    if not num:
        return 0

    smallest=num[0]

    for i in num:
        if i<smallest:
            smallest=i
    return smallest
print(f"smallest element is{small_element([4,3,5,6])}")