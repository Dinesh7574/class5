#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loop
#if
#while
#for


# In[4]:


name = "kiran"

if name == "kiran":
    print ("yes")
else:
        print("no")
        


# In[5]:


police = "no"
signal = "red"

if police == "yes" or signal == "red":  #if the first and 2nd condition is satisfied then the first only execute it wont jump into 2nd
    print ("stop")
elif police == "no" and signal == "red":
    print("go")
else :
    if signal == "green":
        print("green")


# In[8]:


#while
a = 1
while a<5:       #only if the given condition is true it will execute 
    print(a)
    a = a+1


# In[9]:


#for
range (5)


# In[12]:


for i in range (5):
    print(i)


# In[18]:


a = ["hello","welcome","today"]
for i in a:
    print(i)
    


# In[19]:


[0,2,4,6,8]         #to print a even number in the list?


# In[20]:


l =[]
for i in range(10):
    if i%2==0:
        l.append(i)
print(l)        
        


# In[21]:


l = []
for i in range (0,10,2):
    l.append(i)
print (l)


# In[22]:


#input = ["dinesh@gmail.com","kumar@gmail.com","kiran@yahoo.com"]
#out = ["dinesh","kumar","kiran"]
#out = ["gmail","yahoo"]


# In[46]:


a = ["dinesh@gmail.com","kumar@gmail.com","kiran@yahoo.com"]
for i in a:
    if a = dinesh@gmail.com :
        print ("dinesh")
           l.append(i)
print(l)  


# In[43]:


a = ["dinesh@gmail.com","kumar@gmail.com","kiran@yahoo.com"]
while a=username@gmail.com:
    print username


# In[47]:


def extract_username_and_domain(emails):
    usernames = [email.split('@')[0] for email in emails]
    domains = [email.split('@')[1].split('.')[0] for email in emails if email.startswith("gmail") or email.startswith("yahoo")]
    return usernames, domains

emails = ["dinesh@gmail.com","kumar@gmail.com","kiran@yahoo.com"]
usernames, domains = extract_username_and_domain(emails)
print("Usernames:", usernames)
print("Domains:", domains)


# In[13]:


a=["dinesh@gmail.com","kumar@gmail.com","kiran@yahoo.com"]
l = []

for email in a:
    username= email.split('@')[0]
    l.append(username)

        

print(l)


# In[53]:


a=["dinesh@gmail.com","kumar@gmail.com","kiran@yahoo.com"]
for mail in a:
    mail = username.split('@')[0]
   
print (l)


# In[ ]:






# In[49]:


#input a = ["apple","apple","mango","mango","orange","orange","lemon","apple"]
#out ={'apple':3, 'orange':1, 'lemon':1, 'mango':2}
#out = ["apple","mango"]
#out =['apple', 'orange', 'lemon', 'mango']


# In[70]:


a = ["apple","apple","mango","mango","orange","orange","lemon","apple"]

print(a[1:3])
a = list(set(a))
print (a)


# In[ ]:





# In[ ]:




