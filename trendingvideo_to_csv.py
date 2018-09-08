'to check what are the trending videos of youtube'
from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver") #address for the webdriver
url = 'https://www.youtube.com/feed/trending'

driver.get(url)

# find all titles
titles = driver.find_elements_by_id('video-title')

names = []
for title in titles:
    k = title.text
    names.append(k)

# find respective viewcount
viewcounts = driver.find_elements_by_xpath('//*[@id="metadata-line"]/span[1]')

views = []
for viewcount in viewcounts:
    l = viewcount.text
    views.append(l)

# video out in how many days/hours
videoouts = driver.find_elements_by_xpath('//*[@id="metadata-line"]/span[2]')
time = []

for videoout in videoouts:
    m = videoout.text
    time.append(m)

#scrape all publish houses they are from

channels = driver.find_elements_by_xpath('//*[@id="byline"]/a')
channel = []

for i in channels:
    n =i.text
    channel.append(n)
########################################################################
    
'storing all data in a csv for processing'
import pandas as pd

'after searching for half an hour i concluded that its easy for dictionaries to save in csv format'

columns = ['Title','View_count','Channel_Name','uploaded_on']
dict1 = {'Title':names,'View_count':views,'Channel_Name':channel,'uploaded_on':time}
df = pd.DataFrame(dict1, columns=columns)
df.to_excel('C:\\Users\\visha\\Desktop\\treding.xlsx',header=True, index=False, encoding='utf-8') #address for the downloaded csv file
