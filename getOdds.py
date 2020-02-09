#!/usr/bin/env python
# coding: utf-8

# In[16]:


import urllib.request
import urllib.parse
import time
import json
import pandas as pd
import seaborn as sns


# In[25]:


url = 'https://oldrace.netkeiba.com/?pid=show_ninkioddsgraph_js&raceid=201905050811&type={0}&offset=0&limit=5000'
ngscore = 0
base_score = 100000000000000


# In[18]:


def santan(url):

    url = url.format('8')

    try:

        with urllib.request.urlopen(url) as f:
            res =json.loads( f.read().decode('utf-8') )

        score = base_score
        score_arr = [0] * len(umalist)

        for odd in res['showArray']:
            kumi = odd['Kumi'].split('-')
            score_arr[int(kumi[0]) - 1]+=score
            score -= 1
            score_arr[int(kumi[1]) - 1]+=score
            score -= 1
            score_arr[int(kumi[2]) - 1]+=score
            score -= 1
        
        score_arr = [ngscore if i == 0 else i for i in score_arr]
        df = pd.DataFrame(data={'3tan':score_arr}, columns=['3tan'])
        return df.rank(ascending=False).astype(int)


    except Exception as e:
        print(e)
        return []

    


# In[19]:


def sanhuku(url):
 
    url = url.format('7')
    try:

        with urllib.request.urlopen(url) as f:
            res =json.loads( f.read().decode('utf-8') )

        score = base_score
        score_arr = [0] * len(umalist)

        for odd in res['showArray']:
            kumi = odd['Kumi'].split('-')
            score_arr[int(kumi[0]) - 1]+=score
            score_arr[int(kumi[1]) - 1]+=score
            score_arr[int(kumi[2]) - 1]+=score
            score -= 1
        
        score_arr = [ngscore if i == 0 else i for i in score_arr]
        df = pd.DataFrame(data={'3huku':score_arr}, columns=['3huku'])
        return df.rank(ascending=False).astype(int)

    except Exception as e:
        print(e)
        return []


# In[20]:


def umatan(url):
 
    url = url.format('6')

    try:

        with urllib.request.urlopen(url) as f:
            res =json.loads( f.read().decode('utf-8') )
        
        score = base_score
        score_arr = [0] * len(umalist)
        
        for odd in res['showArray']:
            kumi = odd['Kumi'].split('-')
            score_arr[int(kumi[0]) - 1]+=score
            score -= 1
            score_arr[int(kumi[1]) - 1]+=score
            score -= 1

        score_arr = [ngscore if i == 0 else i for i in score_arr]
        df = pd.DataFrame(data={'umatan':score_arr}, columns=['umatan'])
        return df.rank(ascending=False).astype(int)

    except Exception as e:
        print(e)
        return []


# In[21]:


def wide(url):
 
    url = url.format('5')

    try:

        with urllib.request.urlopen(url) as f:
            res =json.loads( f.read().decode('utf-8') )
            
        score = base_score
        score_arr = [0] * len(umalist)

        for odd in res['showArray']:
            kumi = odd['Kumi'].split('-')
            score_arr[int(kumi[0]) - 1]+=score
            score_arr[int(kumi[1]) - 1]+=score
            score -= 1
        
        score_arr = [ngscore if i == 0 else i for i in score_arr]
        df = pd.DataFrame(data={'wide':score_arr}, columns=['wide'])
        return df.rank(ascending=False).astype(int)

    except Exception as e:
        print(e)
        return []


# In[22]:


def umaren(url):
  
    url = url.format('4')

    try:

        with urllib.request.urlopen(url) as f:
            res =json.loads( f.read().decode('utf-8') )

        score = base_score
        score_arr = [0] * len(umalist)
        
        for odd in res['showArray']:
            kumi = odd['Kumi'].split('-')
            score_arr[int(kumi[0]) - 1]+=score
            score_arr[int(kumi[1]) - 1]+=score
            score -= 1
        
        score_arr = [ngscore if i == 0 else i for i in score_arr]
        
        df = pd.DataFrame(data={'umaren':score_arr}, columns=['umaren'])
        return df.rank(ascending=False).astype(int)

    except Exception as e:
        print(e)
        return []


# In[23]:


def tanhuku(url):
 
    url = url.format('1')
    try:

        with urllib.request.urlopen(url) as f:
            res =json.loads( f.read().decode('utf-8') )

        o1 = []
        for odd in res['showArray']:
            o1.append(odd['Kumi'])

        umalist = sorted(o1)

        score = 1
        score_arr = [0] * len(umalist)
        for o in o1:
            score_arr[o - 1] = score
            score = score + 1

        return umalist, score_arr


    except Exception as e:
        print(e)
        return [],[]


# In[26]:


(umalist, tan) = tanhuku(url)
df = pd.DataFrame(data={
    'umaban':umalist, 
    'tanhuku':tan, 
}, columns=[
    'umaban',
    'tanhuku',
])
df2 = df.join(umaren(url)).join(wide(url)).join(umatan(url)).join(sanhuku(url)).join(santan(url))

cm = sns.light_palette("#2ecc71", as_cmap=True)
df2.style.background_gradient(cmap=cm)


# In[ ]:


print(df2.to_html())


# In[ ]:




