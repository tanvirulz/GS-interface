#!/usr/bin/env python
# coding: utf-8

# In[90]:


import dateutil 
import dateutil.parser
import datetime


# In[91]:


f = open("easy-fpscript1.txt", "r")


# In[92]:


script = []
for line in f:
    script.append(line.strip())


# In[93]:


#script[0]
f.close()


# In[94]:


line0_tokens = script[0].split(": ")


# In[95]:


#line0_tokens


# In[96]:


fp_name = line0_tokens[1].strip()


# In[97]:


l1_tokens = script[1].split(": ")


# In[98]:


begin_time_input = l1_tokens[1].strip()


# In[99]:


l2_tokens = script[2].split(": ")


# In[100]:


default_delay_seconds = int(l2_tokens[1].strip())


# In[101]:


start_datetime = dateutil.parser.parse(begin_time_input)


# In[102]:


start_datetime.timestamp()


# In[103]:


outscript = []


# In[104]:


execute_at_time = start_datetime.timestamp()


# In[105]:


def create_command(fp_name,line,index,default_delay,execute_at_time):
    if line[:5] == "delay":
        d_raw = line.split()[1].strip()
        d = d_raw.split(":")
        delay_seconds = int(d[0]) * 60*60 +int(d[1])*60+ int(d[2])
        return delay_seconds, ""
    else :
        name = fp_name +"a"+str(index)
        command = line
        timer_state = str(0)
        timer_basis = str(0) #for absolute time which works. relative time does note work
        timer_last_exec = str(3)
        timer_last_exec_ns = str(0)
        timer_activation_time = str(int(execute_at_time))
        timer_activation_time_ns = str(0)
        timer_repeat = str(1)
        compiled_command = name+','+command+',' \
            +timer_state+','+timer_basis+',' \
            +timer_last_exec+','+timer_last_exec_ns \
            +','+timer_activation_time+',' \
            +timer_last_exec_ns+','+timer_repeat+'\n'
        return default_delay,compiled_command
        


# In[106]:


for index, line in enumerate(script[3:]):
    if len(line.strip()) <2: 
        continue
    delay,f_comm = create_command(fp_name,line,index,default_delay_seconds,execute_at_time)
    execute_at_time += delay
    if f_comm == "":
        continue
    else :
        outscript.append(f_comm)
    
    


# In[107]:


#outscript


# In[108]:


of = open(fp_name+".txt","w")

for line in outscript:
    of.write(line)

of.close()


# In[ ]:




