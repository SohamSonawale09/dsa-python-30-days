# Problem statement:
# Given a dictionary and a key, check whether the key exists or not.

key = "name"
d = {
    "name" : "soham",
    "age" : 22,
    "role" : "Data Science Student"
} 
exists = False
for i in d:
    if i == key:
        exists = True
        break
if exists:
    print("key exists") 
else:
    print("key is not exists") 
    
    
# other method 

if key in d:
    print("key exists")
else:
    print("key not exists")