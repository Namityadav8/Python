# a={}
# print(type(a))




# dict={
#     "name":"namit",
#     "age":32,
#     "grade":'A'
# }
# print(dict)  # Key must be unique   
# print(dict["age"])
# print(dict.get("grade"))
# print(dict.get('sex',"No Sex"))
# dict["age"]=69
# del dict["age"]

# print(dict)

# a=dict.items()
# print(type(a))

#SHALLOW COPY 

# dict1=dict.copy()
# dict1["age"]=69
# print(dict)
# print(dict1)


# for key,value in dict.items():
#     print(f"{key} = {value}")








# a={
#     "dict1":{"age":32,"Name":"namit"},
#     "dict2":{"age":31,"Name":"Naman"}
# }
# print(a["dict1"]["age"])

dict={
    "name":"namit",
    "age":32,
    "grade":'A'
}

a={ key:value for key,value in  dict     }
print(a)





