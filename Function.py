# #FUNCTION 
# def greeting():
#     print("hello guys")
# greeting()  

#  # passing the argument
# def greet(name):
#     print(f"{name} hello")
# greet("gannu")

# #returning the value
# def arithmatic(val1,val2):
#     val = val1 + val2
#     return val
# val1 = int(input())
# val2 = int(input())
# print(arithmatic(val1,val2))

# #returning multiple values
# def cal(val1, val2):
#     add = val1 + val2
#     sub = val1 -val2
#     mult = val1 * val2
#     div = val1 / val2
#     return add,sub,mult,div
# add,sub,mult,div = cal(val1,val2)
# print(f" + = {add} \n - = {sub} \n * = {mult} \n / = {round(div,2)}")


# Type of argument
# 1. Positional 
# 2. default 
# 3. key 
# 4. var len argument
# 5. var len keyword argument
    
    # 1. Positional
# def add(a,b):
#     return a+b
# print(add(5,6))    
    
    
    # 2. default 
# def add(a, b= 10 , c= 20):
#  return a + b + c
# print(add(20,  40))

#     # 3. key
# def add(a, b= 10 , c= 20):
#  return a + b + c
# print(add(20, c = 40))

    #4. variable length 
# def student( name , id , *mark):
#     print(f"marks of the {name} are {mark}")
#     print(f"{name} of id no. {id} secure {round(sum(mark)/len(mark), 2)}%")
# student("ganesh", "25781A05Q6", 67,45,23,78,90,56)


# def add(**args):
#   print(args)
# add(x=10,y=20)  


#     #var len keyword arg
# def student(name, id , **mark):
#     print(f"Marks of {name} are {mark}")
#     print(f"{name} Scored {round(sum(mark.values())/len(mark), 2)}%")

# student("Ganesh","25781A05Q6", math=99, dsa = 98, UHV = 99, JAVA = 99, Digital = 97)    

 
 #LAMDA function :- annonumus function (Function wthiout name)
fun = lambda a,b : a+b

print(fun(2,4))

def add(a,b):
    """
    This function helps to add the two numbers 
    """
    
    return a+b
print(add(2,4))
help(add)
help(type(add))
