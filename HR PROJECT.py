#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from datetime import date 


# In[3]:


data=pd.read_csv('HRDataset.csv')
data                


# In[4]:


data.size


# In[5]:


data.shape


# In[6]:


data.info


# In[7]:


data.isnull().sum()


# In[8]:


data.head(10)


# In[9]:


data.tail(10)


# In[10]:


Manager_Data=data.loc[:,['DeptID','ManagerID','ManagerName']]
Manager_Data


# In[11]:


n_value=Manager_Data[Manager_Data['ManagerID'].isnull()]
n_value


# In[12]:


data['DateofTermination']=data['DateofTermination'].replace(to_replace=np.nan,value=0)
data['DateofTermination'].isnull().sum()                                                       


# In[13]:


data['ManagerID']=Manager_Data['ManagerID'].replace(to_replace=np.nan,value=39.0)
data['ManagerID'].isnull().sum()                                                       


# In[14]:


data.isnull().sum()


# In[19]:


#Count of employees in each department
count_emp=data.groupby("Department")["Department"].count()
count_emp


# In[20]:


#Average salary of employess in each depatment
Avg_Salary=data.groupby("Department")["Salary"].mean()
Avg_Salary


# In[21]:


#Calculate the average of salary of employees based on gender.
sex_salary=data.groupby(["Department","Sex"],as_index=False).Salary.mean()
sex_salary


# In[22]:


#Most popular recruitmentSource of the company based on department
Recruitmentsource=data.groupby(["Department","RecruitmentSource"]).size().reset_index(name="counts")
Recruitmentsource


# In[23]:


#Total Number of working days for terminated employee.
Employee_Name=input("Enter name:")


# In[26]:


Start_year=int(input('Enter the start year:'))
Start_month=int(input('Enter the start month:'))
Start_day=int(input('Enter the start day:'))
Start_date=date(Start_year,Start_month,Start_day)
Start_date


# In[27]:


T_year=int(input('Enter the Terminated year:'))
T_month=int(input('Enter the Terminated month:'))
T_day=int(input('Enter the Terminated day:'))
T_date=date(T_year,T_month,T_day)
T_date


# In[28]:


business_days=pd.bdate_range(Start_date,T_date)
business_days


# In[29]:


print('Employee name:',Employee_Name,'Working_days',len(business_days))
      


# In[15]:


#Fetch the manager name of departments.
Manager_Details=data.groupby(['Department','ManagerName','ManagerID']).size().reset_index(name='counts')
Manager_Details.set_index("ManagerName",inplace=True)
Manager_Details


# In[16]:


#Fetch Employee name and number of absences.
Emp_Attendance=data.loc[:,['Department','ManagerName','Employee_Name','Absences']]
Emp_Attendance


# In[ ]:




