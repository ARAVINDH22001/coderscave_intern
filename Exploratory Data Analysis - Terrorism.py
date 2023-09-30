#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[67]:


data = pd.read_csv("globalterrorismdb_0718dist.csv", encoding="latin1")
df = pd.DataFrame(data)
print("Data has been successfully imported")
df.head()


# In[68]:


df.info()


# In[69]:


df.shape


# In[70]:


df.columns


# In[71]:


for i in df.columns:
    print(i, end=", ")


# In[72]:


df = df[["iyear", "country_txt", "attacktype1_txt", "weaptype1_txt", "nkill", "nwound"]]
df.head()


# In[73]:


df.rename(columns={"iyear": "Year", "country_txt": "Country",
                   "attacktype1_txt": "Attack Type", "weaptype1_txt": "Weapon Type",
                   "nkill": "Killed", "nwound": "Wounded"}, inplace=True)


# In[74]:


df.head()


# In[75]:


df.info()


# In[76]:


df.shape


# In[77]:


df.isnull().sum()


# In[78]:


df["Killed"] = df["Killed"].fillna(0)
df["Wounded"] = df["Wounded"].fillna(0)
df["Casualty"] = df["Killed"] + df["Wounded"]

df.describe()


# In[79]:


attacks = df["Year"].value_counts(dropna=False).sort_index().to_frame().reset_index().rename(columns={"index": "Year", "Year": "Attacks"}).set_index("Year")
attacks.head()


# In[80]:


attacks.plot(kind="bar", color="cornflowerblue", figsize=(15, 6), fontsize=13)
plt.title("Timeline of Attacks", fontsize=15)
plt.xlabel("Years", fontsize=15)
plt.ylabel("Number of Attacks", fontsize=15)
plt.show()


# In[81]:


yc = df[["Year", "Casualty"]].groupby("Year").sum()
yc.head()


# In[82]:


yc.plot(kind="bar", color="cornflowerblue", figsize=(15, 6))
plt.title("Year-wise Casualties", fontsize=13)
plt.xlabel("Years", fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Casualties", fontsize=13)
plt.show()


# In[83]:


yk = df[["Year", "Killed"]].groupby("Year").sum()
yk.head()


# In[84]:


yw = df[["Year", "Wounded"]].groupby("Year").sum()
yw.head()


# In[85]:


fig = plt.figure()
ax0 = fig.add_subplot(2, 1, 1)
ax1 = fig.add_subplot(2, 1, 2)

# Killed
yk.plot(kind="bar", color="cornflowerblue", figsize=(15, 15), ax=ax0)
ax0.set_title("People Killed in each Year")
ax0.set_xlabel("Years")
ax0.set_ylabel("Number of People Killed")

# Wounded
yw.plot(kind="bar", color="cornflowerblue", figsize=(15, 15), ax=ax1)
ax1.set_title("People Wounded in each Year")
ax1.set_xlabel("Years")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# In[86]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[87]:


data = pd.read_csv("globalterrorismdb_0718dist.csv", encoding="latin1")
df = pd.DataFrame(data)


# In[88]:


print("Data has been successfully imported")


# In[89]:


df = df[["iyear", "country_txt", "attacktype1_txt", "weaptype1_txt", "nkill", "nwound", "region_txt"]]


# In[90]:


df.rename(columns={"iyear": "Year", "country_txt": "Country",
                   "attacktype1_txt": "Attack Type", "weaptype1_txt": "Weapon Type",
                   "nkill": "Killed", "nwound": "Wounded"}, inplace=True)

# Fill missing values


# In[91]:


df["Killed"] = df["Killed"].fillna(0)
df["Wounded"] = df["Wounded"].fillna(0)


# In[92]:


reg = pd.crosstab(df.Year, df.region_txt)
reg.head()


# In[93]:


reg.plot(kind="area", stacked=False, alpha=0.5,figsize=(20,10))
plt.title("Region wise attacks",fontsize=20)
plt.xlabel("Years",fontsize=20)
plt.ylabel("Number of Attacks",fontsize=20)
plt.show()


# In[94]:


regt=reg.transpose()
regt["Total"]=regt.sum(axis=1)
ra=regt["Total"].sort_values(ascending=False)
ra


# In[95]:


ra.plot(kind="bar",figsize=(15,6))
plt.title("Total Number of Attacks in each Region from 1970-2017")
plt.xlabel("Region")
plt.ylabel("Number of Attacks")
plt.show()


# In[96]:


rw = df[["region_txt", "Wounded"]].groupby("region_txt").sum().sort_values(by="Wounded", ascending=False)


# In[97]:


fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 6))

# Killed
rw.plot(kind="bar", color="cornflowerblue", ax=ax0)
ax0.set_title("People Killed in each Region")
ax0.set_xlabel("Regions")
ax0.set_ylabel("Number of People Killed")

# Wounded
rw.plot(kind="bar", color="cornflowerblue", ax=ax1)
ax1.set_title("People Wounded in each Region")
ax1.set_xlabel("Regions")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# In[ ]:





# In[ ]:




