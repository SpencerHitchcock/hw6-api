#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import json

from config import api_key

from citipy import citipy

# Output File (CSV)
output_data_file = "out_cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)



# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# In[ ]:



# url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID="

# settings = {"units": "imperial", "appid": api_key}
# # current_weather = owm.get_current(city_names[i], **settings)


# # set up lists to hold reponse info
# lat = []
# temp = []
# humidity = []
# cloudiness = []
# windspeed = []
# name = []


# # Loop through the list of cities and perform a request for data on each
# for city in cities:
#     try:
        
#         weather_response=requests.get(url+ "&appid=" + api_key + "&q=" + city)
#         lat.append(response['coord']['lat'])
#         temp.append(response['main']['temp'])
#         humidity.append(response['main']['humidity'])
#         cloudiness.append(response['clouds']['all'])
#         windspeed.append(response['wind']['speed'])
#         name.append(response["name"])
#         city_list.append({"City": city,
#                           "Lat": lat,
#                           "Lon": lon,
#              "Temp": temp,
#              "Humidity": humidity,
#              "Cloudiness": cloudiness,
#              "Windspeed": windspeed})

#     except:
#         continue


# In[ ]:


url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + api_key

city_list = []

lat = []
lon = []
temp = []
humidity = []
cloudiness = []
windspeed = []
date = []

#Initial set of variables for log file
records=1
sets=1
print("Beginning Data Retrieval")
print("-----------------------------")
for i, city in enumerate(cities): 
    varcity = url + "&q=" + city
    if (i%50==0 and i>=50):
        sets=sets+1
        records = 0
    weather_response=requests.get(varcity).json()
#     if weather_response.ok:

print("Processing Record "+ str(records) + " of set " + str(sets) + " | " + city)
records+=1
try:
 #adding data to lists
    lat.append(response['coord']['lat'])
    lng.append(response['coord']['lon'])
    date.append(response['main']['date'])
    temp.append(response['main']['temp'])
    humidity.append(response['main']['humidity'])
    cloudiness.append(response['clouds']['all'])
    windspeed.append(response['wind']['speed'])
    city_list.append({"City": city,
                          "Lat": lat,
                          "Lon": lon,
             "Temp": temp,
             "Humidity": humidity,
             "Cloudiness": cloudiness,
             "Windspeed": windspeed})
except:
    

        #counter for log file


    print("City not found, skipping!")
pass
print("-----------------------------")
print("Data Retrieval Complete")
print("-----------------------------")


# In[ ]:





# In[ ]:


# all_df = pd.DataFrame({"Lat": lat,
#              "Temp": temp,
#              "Humidity": humidity,
#              "Cloudiness": cloudiness,
#              "Windspeed": windspeed})
# all_df

# # all_df = {"Lat": lat,
# #              "Temp": temp,
# #              "Humidity": humidity,
# #              "Cloudiness": cloudiness,
# #              "Windspeed": windspeed}
# # all_df = pd.DataFrame(all_df)


# # df = pd.read_csv("weather_data.csv", names=['lat', 'temp', 'humidity', 'cloudiness', 'windspeed'])
# # df = pd.DataFrame({"Lat": lat,
# #              "Temp": temp,
# #              "Humidity": humidity,
# #              "Cloudiness": cloudiness,
# #              "Windspeed": windspeed})

# all_df.to_csv('city_weather_data.csv')

# all_df.head()


# In[ ]:


#This Should be all Atributes vs latitude but i dont have any data...
plt.scatter(lat, temp,c ='r', label='Temp F')
plt.scatter(lat, humidity, c ='b', label='Humidity')
plt.scatter(lat, windspeed, c ='g', label='Wind Speed')
plt.scatter(lat, cloudiness, c = 'purple', label = 'Cloudiness')
plt.legend(loc='lower right')
plt.title('Weather attributes VS Latitude')
plt.xlabel('Latitude')
plt.ylabel('Weather Value')
plt.show()


# #### Latitude vs. Temperature Plot

# In[ ]:


plt.scatter(lat,temp,c ='r', label='Temp F')
plt.legend(loc='lower left')
plt.title('Temperatur VS Latitude')
plt.xlabel('Latitude')
plt.ylabel('Temp in F')
plt.savefig('Graph_Images/temp.png')
plt.show()


# #### Latitude vs. Humidity Plot

# In[ ]:


plt.scatter(lat,humidity,c ='b', label='Humidity')
plt.legend(loc='lower left')
plt.title('Humidity VS Latitude')
plt.xlabel('Latitude')
plt.ylabel('% Humidity')
plt.savefig('Graph_Images/humidity.png')
plt.show()


# #### Latitude vs. Cloudiness Plot

# In[ ]:


#Compare by Cloudiness
plt.scatter(lat,cloudiness,c ='purple', label='Cloudiness')
plt.legend(loc='lower left')
plt.title('Cloudiness VS Latitude')
plt.xlabel('Latitude')
plt.ylabel('% Cloudiness')
plt.savefig('Graph_Images/cloudiness.png')
plt.show()


# #### Latitude vs. Wind Speed Plot

# In[ ]:


#Compare by Windspeed
plt.scatter(lat,windspeed,c ='g', label='Wind Speed')
plt.legend(loc='lower left')
plt.title('Windspeed VS Latitude')
plt.xlabel('Latitude')
plt.ylabel('Windspeed MPS')
plt.savefig('Graph_Images/windspeed.png')
plt.show()


# In[ ]:




