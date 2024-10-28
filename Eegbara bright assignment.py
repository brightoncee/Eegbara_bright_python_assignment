#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Creating a to-do list for days in the week using a list
todo_list = [
   ["Monday", "Check emails", "Attend meeting", "Write report"],
   ["Tuesday", "Work on project", "Call client", "Read book"],
   ["Wednesday", "Go jogging", "Grocery shopping", "Study Python"],
   ["Thursday", "Clean the house", "Pay bills", "Watch a movie"],
   ["Friday", "Finish project", "Go to the gym", "Dinner with friends"]]
def print_todo_list(todo_list): 
   for task in todo_list:
       print(task)
# Defining the day to perform tasks
day_index =todo_list[3]  # thursday
print(day_index)
  


# In[58]:


#CREATING A DICTIONARY
my_bio_info={
    "name":"Eegbara_bright",
    "age": 27,
    "state": "rivers_state",
    "skills":["excel","SQL","powerbi","python","R"],
}
print(my_bio_info)


# In[69]:


#loop through the bio dictionary and print key and values
for key, value in my_bio_info.items():
    if key =="skills":
        print("my skills are:")
        for skill in value:
            print(skill)
    else:
            print(f"my {key.capitalize()} is {value}")


# In[71]:


doubled_values =[(lambda x: x*2)(x)
for x in range(1,51)]

print("doubled values from 1 to 50:")
print(doubled_values)

