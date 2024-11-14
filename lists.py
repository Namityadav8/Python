# a=["namit","yadav","ahir","rao"]
# # print(a.count("ahir"))
# # a[3]="pawansherawar"

# # # a[1:]="namit"   -> updating multiple items in it  
# # a.reverse()
# # print(a)

# for x,y in enumerate(a):
#     print(x,y)    # to have an output with indexes



# a=[x*2 for x in range(10)]
# print(a)                 # list comprehension



# b=[i**2 for i in range(10) if i%2==0]        # with condition
# print(b)







lst1=[1,2,3,4]
lst2=["a","b","c","d"]
pairs=[(i,j)  for i in lst1 for j in lst2]
print()