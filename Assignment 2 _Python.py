#!/usr/bin/env python
# coding: utf-8
1.  The two values are true and false. Boolean operator return returns the output as true if one of the conditions or input is true or successfully fulfills the condition, otherwise it turns the output as false.

2. Three different type of boolean operators are AND, OR and NOT. AND = both are true, OR - if any is true , and NOT - if the solution is not true then it will return output as false and vice versa.

3. There are various type of boolean operators sucha as logical operators and comparison operators. Logical operators are AND, OR and NOT. 
AND - 
X (True) and Y (False) = False
X (False) and Y (False) = False
X (False) and Y (True) = False
X (True) and Y (True) = True

OR - 
X (True) and Y (False) = True
X (False) and Y (False) = False
X (False) and Y (True) = True
X (True) and Y (True) = True

NOT - 
X (True) and not X (False)
X (False) and not X (True) 

Comparison operators :

== The resultant is True if both operands are equal else false.
!= The resultant is True if both operands are not equal else false.
< It results in a True if the first operand is smaller than the second, else a False.
> It results in a True if the first operand is greater than the second, else a False.
<= It results in a True if the first operand is lesser than or equal to the second, else a False.
>= It results in a True if the first operand is greater than or equal to the second, else a False.

4. 




# In[3]:


(5 > 4) and (3 == 5)
not(5>4)


# In[4]:


(5 > 4) and (3 == 5)
not ((5> 4) or (3 == 5))


# In[5]:


(True and True) and (True == True)
(not False) or (not True )


# In[ ]:


5. Comparison operators has already been explained in question no.3
6. The “=” is an assignment operator is used to assign the value on the right to the variable on the left. The '==' operator checks whether the two given operands are equal or not. If so, it returns true. Otherwise it returns false.


# In[6]:


spam = 0
if spam == 10:
    print('eggs')
if spam >5 :
    print('bacon')
else :
    print('spam')
    print('spam')
    print('spam')


# In[ ]:


9. Restart the kernel if it gets stuck in the endless loop.
10. In case of break the loop will disconntinue if it doesn't specifies the condition and in case of continue it will go the next loop or condition and process the solution accordingly.
11. The difference between ranges are range (10) will show resultant before range 10 i,e from 0 to 9 horizontally and when range is (0,10) it will show resultant from 0 to 9 without skipping and range. While range is (0,10,1) it will show resultant from range 0 to 9 skipping one digit everytime.


# In[7]:


for i in range(1, 11):
    print(i)


# In[8]:


i = 1
while(i<=10):
    print(i)
    i += 1


# In[24]:


import Spam as sp
sp.bacon()


# In[12]:


if (spam ==1) :
    
    print("Hello")
elif (spam == 2) :
    print("Howdy")
else :
    print('Greetings')


# In[18]:


spam = 1


# In[21]:


spam = 1
if (spam ==1) :
   print("Hello")
elif (spam == 2) :
   print("Howdy")
else :
   print('Greetings')
   


# In[22]:


spam = 2
if (spam ==1) :
    print("Hello")
elif (spam == 2) :
    print("Howdy")
else :
    print('Greetings')


# In[1]:


spam.bacon()


# In[2]:


from spam import bacon
bacon()


# In[ ]:




