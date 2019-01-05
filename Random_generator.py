#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
i = random.randint(1,10)
while True:
    j = int(input("Pick Number from 1 to 10: "))
    if j>10:
        print("Number is greater than 10")
    elif i>j:
        print("TOO LOW!!")
    elif j>i:
        print("TOO HIGH!!")
    else:
        print("You Won!!")
        k = input("Wanna play again(y/n): ").lower()
        if k == 'y':
            i = random.randint(1,10)
            continue
        else:
            print("Thanks for playing!!")
            break


# In[ ]:




