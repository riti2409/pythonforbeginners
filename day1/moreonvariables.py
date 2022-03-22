#to find the adress we use id
num = 5
print(id(num))
#o/p=1394312964528
#we get the same adress . in python when we create variables having same values they will point to the same variable only
a = 10
b = a
print(id(a))
#id(a)=id(b)=id(10)=1758711016016 i.e why python is more memory efficient
k = 10
print(id(10))
#we are not talking about k we are talking about 10. so when another variable points to k it means 10
# 10->k,a,b(same id)
a = 9
print(id(a))
#it doesnt affect b
#lets us supoose a=9, k=a and b=8 then 10 will still exsist  in the memory(garbage collection)
#to know the type of variable
type(a)
