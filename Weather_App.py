#importing request module to work with API.
#it is use to send all kinds of HTTP requests. 
import requests

#Defining a Function.
def GetWeather():
    #getting Input city name from User.
    CityName=input("Enter the City Name: ")
    
    #Create Acount On  https://home.openweathermap.org/users/sign_in and Enter your API KEY here.
    

    API="https://api.openweathermap.org/data/2.5/weather?q={}&appid=Your-API_Key".format(CityName)
    
    Weatherdata=requests.get(API).json()

    #Getting Main Weather_data.
    MainWeather_Data=Weatherdata["weather"][0]["main"]
    Description_data=Weatherdata["weather"][0]["description"]
    City_Temprature=Weatherdata["main"]["temp"]
    City_humidity=Weatherdata["main"]["humidity"]

    #Printing the weather Detail.
    
    print(f"\nMain Weather Condition =>> {MainWeather_Data}")
    #getting City Temp in Kelvin.
    print(f"The Temprature in Kelvin ==> {City_Temprature}")   
    print(f"The Humidity in air is ==> {City_humidity}")
    print(f"Description =>> {Description_data}")
# Calling the Function.
GetWeather()
