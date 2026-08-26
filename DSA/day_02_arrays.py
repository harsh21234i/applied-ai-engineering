##Check if array is sorted or not

def is_sorted(num):
    for i in range(1,len(num)):
        if num[i-1]>num[i]:
            return False

    return True

print(is_sorted([1,3,2,4,5]))

##Remove Duplicates From a Sorted Array also find unique numbers

def remove_dupli(num):
    if not num:
        return 0

    i=0

    for j in range(1,len(num)):
        if num[j]!=num[i]:
            i+=1
            num[i]=num[j]

    return i +1

num =[1,2,2,3,4,5,5,5]
unique_count=remove_dupli(num)
print(unique_count)
print(num[:unique_count])

##Move all zeroes to end
def move_zero(num):
    i=0

    for j in range(len(num)):
        if num[j]!=0:
            num[i],num[j]=num[j],num[i]
            i+=1
    return num

print(move_zero([1,0,3,4,5,0,5]))

##Roatate by K position right

def rotate_right(num,k):
    if not num:
        return 0

    k=k%len(num)
    return num[-k:]+num[:-k]
print(rotate_right([1,2,3,4,5],2))

##Roatate K postion by left

def rotate_left(num,k):
    if not num:
        return 0

    k=k%len(num)
    return num[k:]+num[:k]
print(rotate_left([1,2,3,4,5],2))



