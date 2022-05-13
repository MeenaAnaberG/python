###########NESTED  LIST AS MATRIX################################

from posixpath import split


x=[[1,2,3],[4,5,6],[7,8,9]]

for i in x:
    print(i)
p=list(x[0])
q=list(x[1])
r=list(x[2])
print(p[0],p[1],p[2])
print(q[0],q[1],q[2])
print(r[0],r[1],r[2])



########sentence to list #######################
def l_words(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x) >n:
            word_len.append(x)
            
    return word_len


print(l_words(3,"meena anaber gang"))


##########tuples to list#############
def test(lst_tpl):
    result=[list(el) for el in lst_tpl]
    return result
lst_tpl=[(1,2),(6,7)]
y=[1,2,3,4]
print("original tuple")
print(lst_tpl)
print("coverted tupleto lst")
print(test(lst_tpl))

test(lst_tpl)



##sub question##
##same element
def test1(x,y):
    x_set=set(x)
    y_set=set(y)
    if (x_set == y_set):
        print(x_set & y_set)
    else:
        print("No common elements")
x=[1,2,3,4]
y=[1,2,3,4]
test1(x,y)


#################tuple of integers to single integer#########
T = (1,2,3)
print("Original List: ",T)
x = int("".join(map(str, T)))
print("Single Integer: ",x)
















###############OOOOOOOOOOPPPPPPSSSSSSSSSS######################

###LEAP#######
def CheckLeap(Year):
    if((Year%400 == 0 ) or (Year %100 != 0) and (Year % 4 ==0)):
        print(Year,"is Leap year")
    else:
        print(Year,"is not a Leap year")
Year=int(input("enter the number"))
CheckLeap(Year)



######ARMSTRONG##########
num=int(input("enter no: "))
sum=0
temp=num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is Armstrong number")
else:
    print(num,"is not Armstrong number")



#####SIMPLE_CALCULATOR#########
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("SElect operator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice=input("enter the choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1=float(input("enter first number"))
        num2=float(input("enter second number"))
    if choice=='1':
        print(num1,"+",num2,'=',add(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,'=',subtract(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,'=',multiply(num1,num2))
    elif choice=='4':
        print(num1,"/",num2,'=',divide(num1,num2))

    nxt_cacl=input("let calculate(yes/no):")
    if nxt_cacl=="no":
        break
    else:
        print("invalid input")



