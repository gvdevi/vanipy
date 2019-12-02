for i in range(0, 5): 
   print(i)


print("\n")

a = 3
A = 4
print(a)
print(A)

print("\n")


a=12
b=3
print(a+b)
print(a/b)
print(a-b)
print(a*b)


a=10
b=5
if a==b:
    print("a is equal to b")
else:
    print(" a is not equal to b")


print("\n")

def add(a,b):
    c = a+b
    print(c)
add(2,3)

def div(a,b):
    if a%b ==0:
        print("a is divisible by b")
    else:
        print("a  is not divisible by b")
div(10,5)

print("\n")

list = [1,"abc",3,2-1]
print(list)
list.pop()
print(list)
list.pop()

type(list)

print(list)
type(list)




# Python program to swap two variables in single line
x = 5
y = 10
print(x,y)
x, y = y, x
print ("After Swapping values of x and y are", x, y)
print(x,y)