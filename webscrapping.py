# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:05:00 2020

@author: 20304834
"""

from bs4 import BeautifulSoup as bs
from tkinter.ttk import Combobox
from tkinter import Button, Labels
from tkinter import *
import webbrowser
import pandas as pd
import requests
global url
url=' '
def openinsta():
    #print('inside openinsta')
    url="https://www.instagram.com/"+dictionary[cb.get()]+'/'
    chromedir="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
    webbrowser.open(url)
def opentwit():
    #print('inside opentwit')
    url="https://twitter.com/"+dictionary1[cb.get()]+'/'
    chromedir="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
    webbrowser.open(url)
    
root=Tk()
root.title('Welcome to the Web')
root.geometry('{}x{}'.format(700,500))
lblinsta=Label(root, text='Explore the Web',width=40, font=('arial',30,'bold'),fg='#922821')
lblinsta.pack()
lblname=Label(root, text='Select Name',width=15, font=('arial',12,'bold'),fg='#922821')
lblname.place(x=25,y=90)
binsta=Button(root, text='OPEN INSTAGRAM PROFILE',width=25, font=('arial',10,'bold'),fg='#922821',command=openinsta)
binsta.place(x=220,y=450)
binsta=Button(root, text='OPEN TWITTER PROFILE',width=25, font=('arial',10,'bold'),fg='#922821',command=opentwit)
binsta.place(x=450,y=450)
lblopen=Label(root, text='To visit profile, Click here==>',width=30, font=('arial',10,'bold'),fg='#922821')
lblopen.place(x=-20,y=450)


def parse_data(s):
    data={}
    s=s.split('-')[0]
    s=s.split(' ')
    data['followers']=s[0]
    data['following']=s[2]    
    data['posts']=s[4]
    lblfollowers=Label(root, width=30, font=('arial',12,'bold'),fg='#922821')
    lblfollowers.configure(text='Number of Followers= ' + s[0])
    lblfollowers.place(x=25,y=200)
    lblfollowing=Label(root, width=30, font=('arial',12,'bold'),fg='#922821')
    lblfollowing.configure(text='Number of Following= ' + s[2])
    lblfollowing.place(x=25,y=230)
    lblposts=Label(root, width=30, font=('arial',12,'bold'),fg='#922821')
    lblposts.configure(text='Number of posts= ' + s[4])
    lblposts.place(x=25,y=260)
    
'''
def scrape_data(self):
    print('inside scrape_data1')
    global url
    url="https://twitter.com/"+dictionary[cb.get()]+'/'
    print(url)
    r=requests.get(url)
    s=bs(r.text,'html.parser')
    meta=s.find('meta', property='og:description')
    #print(s)
    return parse_data1(meta.attrs['content'])    
'''
def scrape_data(self):
    global url
    url="https://www.instagram.com/"+dictionary[cb.get()]+'/'
    #print(url)
    r=requests.get(url)
    s=bs(r.text,'html.parser')
    meta=s.find('meta', property='og:description')
    #print(s)
    return parse_data(meta.attrs['content'])

   
df=pd.DataFrame()
for f in [r'C:\Users\20052020\1234pyol\social_handles.xlsx']:
    data=pd.read_excel(f,'Sheet1')
    df=df.append(data)
    
df_name=df[['person_name']]
df_name=df_name.values.tolist()
#print(df_name)

df_handle=df[['insta_handle']]
df_handle=df_handle.values.tolist()
#print(df_handle)

df_handle1=df[['twitter_handle']]
df_handle1=df_handle1.values.tolist()
#print(df_handle1)

final_names=[]
for i in df_name:
    final_names.append(repr(i)[2:-2])
final_handles=[]
for i in df_handle:
    final_handles.append(repr(i)[2:-2])
final_handles1=[]
for i in df_handle1:
    final_handles1.append(repr(i)[2:-2])

dictionary={}
for i in range(len(final_names)):
    dictionary.update({final_names[i]:final_handles[i]})
#print (dictionary)
dictionary1={}
for i in range(len(final_names)):
    dictionary1.update({final_names[i]:final_handles1[i]})
#print (dictionary1)
cb=Combobox(root,width=18, values=final_names,font=('Times New Roman',12,'bold'))
cb.current(0)
cb.bind('<<ComboboxSelected>>', scrape_data)
cb.place(x=50,y=130)

root.mainloop()