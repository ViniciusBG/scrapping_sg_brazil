#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# In[50]:

option = webdriver.ChromeOptions()
option.add_argument(' — incognito')

driver = webdriver.Chrome(executable_path='/Applications/chromedriver', chrome_options=option)

# In[51]:
empresas = {}
for i in range(1,10):
    time.sleep(5)
    driver.get('https://www.jornaldacidadeonline.com.br/')
    time.sleep(5)
    try:
        x =driver.find_element_by_id('onesignal-popover-cancel-button')
        x.click()
        time.sleep(5)
        link=driver.find_element_by_class_name('ads__content')
        link.click()
        time.sleep(5)
        #driver.switch_to.window(driver.window_handles[1])
        #time.sleep(5)
        title = driver.title
        #driver.switch_to.window(driver.window_handles[0])
        time.sleep(7)
        empresa = driver.title
        link1=driver.current_url
        empresas['Empresa{}'.format(i)]={}
        empresas['Empresa{}'.format(i)]['Nome']=empresa
        empresas['Empresa{}'.format(i)]['Link']=link1

    except:
        time.sleep(5)
        link=driver.find_element_by_class_name('ads__content')
        link.click()
        time.sleep(5)
        #driver.switch_to.window(driver.window_handles[1])
        #time.sleep(5)3
        title = driver.title
        link1=driver.current_url
        #driver.switch_to.window(driver.window_handles[0])
        empresas['Empresa{}'.format(i)]={}
        empresas['Empresa{}'.format(i)]['Nome']=title
        empresas['Empresa{}'.format(i)]['Link']=link1

# In[52]:
    
ads = pd.DataFrame.from_dict(empresas)
ads = ads.transpose()
ads = ads.drop_duplicates(subset='Nome',keep='first')


