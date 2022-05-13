def sum_list(items):
    sum_numbers=0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([3,4,5,6]))



def multiply_list(items):
    multipl=1
    for x in items:
        multipl *= x
    return multipl
print(multiply_list([5,6]))



def max_num_list(list):
    max=list[0]
    for a in list:
        if a > max :
            max =a
    return max
print(max_num_list([1,2,3,4]))



def min_num_list(list):
    min=list[0]
    for a in list:
        if a < min :
            min =a
    return min
print(min_num_list([1,2,3,4]))



a=[10,20,30,20]
dup=set()
uniq=[]
for x in a:
    if x not in dup:
        
        dup.add(x)
        uniq.append(x)

print(dup)




list=[]
if not list:
    print("list is empty")



def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8]))


