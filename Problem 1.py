#!/usr/bin/env python
# coding: utf-8

# # String Challenge

# ### What's Your Name?  
# https://www.hackerrank.com/challenges/whats-your-name?isFullScreen=true

# In[2]:


#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print('Hello ' + first + ' ' + last +"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# ### String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

# In[ ]:


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# ### Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# In[8]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split()
    answer = ''
    for string in s:
        answer += string.capitalize()
        answer += " "
    return answer[:-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:





# # Sets
# 

# ### Symmetric Difference
# 
# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

# In[10]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
set_a = set(map(int, input().split()))
N = int(input())
set_b = set(map(int, input().split()))

symmetric_diff = sorted(set_a.symmetric_difference(set_b))

for num in symmetric_diff:
    print(num)


# ### Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
country_stamps = set()

for _ in range(n):
    country = input()
    country_stamps.add(country)

print(len(country_stamps))


# ### Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

# In[13]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))

