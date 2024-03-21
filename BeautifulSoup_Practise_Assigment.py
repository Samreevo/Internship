#!/usr/bin/env python
# coding: utf-8

# In[32]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[33]:


from bs4 import BeautifulSoup
import requests


# 1. Write a python program to display all the header tags from wikipedia.org.

# In[34]:


url ='https://www.wikipedia.org/'

page =requests.get(url)

page


# In[35]:


soup = BeautifulSoup(page.content)

soup


# In[36]:


first_title =soup.find('div',class_="central-featured-lang lang1") 
first_title                      


# In[37]:


first_title.text.strip()



# In[38]:


all_title =soup.find_all('div',class_="central-featured-lang") 
all_title


# In[39]:


new_all_title= []

for i in all_title:
    new_all_title.append(i.text.strip())

print(new_all_title)


# 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[40]:


url ='https://www.imdb.com/chart/top/'

movies =requests.get(url)

movies


# In[41]:


#403 Forbidden
#Unauthorized request. The client does not have access rights to the content. 
#Unlike 401, the client’s identity is known to the server.


# 3.0 Write a python program to scrape mentioned details from dineout.co.in : i) Restaurant name ii) Cuisine iii) Location iv) Ratings v) Image URL.

# In[42]:


##Food not found!Looks like you are not in our service area but don't worry, 
##we take uniting foodies with food very seriously and will come to your region soon!
##Are you in our service area?


# 4.0 Write s python program to display list of respected former finance minister of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[43]:


url ='https://presidentofindia.nic.in/former-presidents'

prime_m =requests.get(url)

prime_m


# In[44]:


res_prime_m =BeautifulSoup(prime_m.content)

res_prime_m


# In[45]:


name_prime_m = res_prime_m.find('div',class_="president-listing") 

name_prime_m.text.strip()


# In[ ]:





# In[46]:


name=[]
for prime in res_prime_m.find_all('h3'):
    name.append(prime.text.strip())
name


# In[47]:


term=[]
for prime in res_prime_m.find_all('h5'):
    term.append(prime.text.strip())
term


# In[48]:


import pandas as pd

df = pd.DataFrame({'Name':name,'Term of Office':term})

df

