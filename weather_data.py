import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://rss.weather.gov.hk/rss/CurrentWeather.xml")
soup = BeautifulSoup(page.content, 'html.parser')
soup = str(soup)
front,mid = soup.split('<table border="0" cellspacing="0" cellpadding="0">',1)
mid,back = mid.split('</table>',1)
location_list = mid.split('\n')
d = {}
location_names = []
location_temperatures = []

for i in location_list:
    if len(i) > 10:
        front_a, mid_a = i.split('<font size="-1">',1)
        mid_a, back_a = mid_a.split('</font>',1)
        front_b, mid_b = back_a.split('<font size="-1">',1)
        mid_b, back_b = mid_b.split('</font>',1)
        mid_b = mid_b[:2]
        location_names.append(mid_a)
        location_temperatures.append(int(mid_b))
d = {'Locations':location_names,'Temperatures':location_temperatures}
df = pd.DataFrame.from_dict(d,orient='columns')
print(df)

        
        
        


