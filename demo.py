print("Hello, World!")

print(3)
a =5
name="Mehmet"
print(a ,name)

print(type(a))
print(type(name))
print(type(3.14))

c=3
d=4
e=5
f=6
g=c+d**e/f%e
h= c-d**e/f+d
# 0. Parantez:()
# 1. Powers/Exponents:**
# 2. products ve division: * /
# 3. addition ve subtraction: + -

print(g)
print(h)


# list
list1 = [1,2,3,4,5]
print(list1)
print(type(list1))
print(list1[0])
m= [1,2,3,4,5,"six",7,8,9,10]
print(m)

print()
age=5
print("My age is", age) 
st="I am "
st1="not"
st2="years old"
print(st,age,st2)
print(st,st1,age,st2)
print()


st_f="i am {} yers old"
st_f1="i am not {} yers old"

print(st_f.format(age))
print(st_f1.format(age))


print()

st_f="i am {}{} yers old"
st_not_f="not "

print(st_f.format(age,""))
print(st_f.format(st_not_f,age))

# User input
age1=input("Enter your age: ")  
age1=int(age1)
print(type(age1))
print("In 1 year, you will be {} yerars old".format(age1+1))
