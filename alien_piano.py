#!/usr/bin/env python
# coding: utf-8

# In[1]:


T = int(input())
for test_cases in range(1,T+1):
    N = int(input())
    violations = 0
    notes = list(map(int, input().split()))
    
    upcount = 0
    downcount = 0
    
    for i in range(1, len(notes)):
        if(notes[i] > notes[i-1]):
            upcount += 1
            downcount = 0
        if(notes[i] < notes[i-1]):
            upcount = 0
            downcount += 1
        if(upcount > 3 or downcount > 3):
            violations += 1
            upcount = 0
            downcount = 0
    print("Case #{}: {}".format(test_cases, violations))

