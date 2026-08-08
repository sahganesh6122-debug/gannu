# student = ["ganesh", 20, "Male", 20]
 
# #  APPEND ADD THE ITEM AT THE END OF THE LIST
# student.append("BTech")

# # EXTEND THE LIST
# student.extend(["gannu","xyz"])

# # REVERSE THE LIST
# student.reverse()


# student.count(20)
# print(student.count(20))

num = [1, 4, 6, 3, 0, 4, 6, 5]
num.sort(reverse=True)
print(num) 
print(4 in num)

num.remove(4)
print(num)


num.pop(1)
print(num)
 
num.insert(1,9)
print(num)
 
 #NESTED LIST
L1 =[[1, 2], [3, 4], [6, 4, [9, [7, 5]]]]
print(L1[-1][-1][-1][0]) 
       