import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def mergesort(array):
    # 先分
    mid=len(array)//2
    left=array[0:mid]
    right=array[mid:]
    left.sort()
    right.sort()
    # merge
    l=0
    r=0
    ans=[]
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            ans.append(left[l])
            l+=1
        else:
            ans.append(right[r])
            r+=1
    return ans

a= random_int_list(1,101,100)
print(a)
print(mergesort(a))
