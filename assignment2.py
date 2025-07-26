#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[15]:



l1 = ["apple",["Banana", "Orange", "Grapes"],"mango"]
print(l1)
slice1 = l1[1:2]
print(slice1)


# In[24]:


dict1 = {"name1": 20,
        "name2": 22,
        "name3": 24,
        "name4": 30,
        "name5": 27}
print(dict1)
print(dict1["name1"])
dict1["name6"]= 32
print(dict1)


# In[25]:


def find_dupli(l1):
    for i in l1:
        for j in range(1,l1.length()):
            if(l1[i]==l1[j]):
                print("duplicate found")
                
l1 = [1,2,3,4,1,5,6,7,8,10]
find_dupli(l1)


# In[ ]:




