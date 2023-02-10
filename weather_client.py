import requests                                                                                                                                                                           
from typing import Dict                                                                                                                                                                   
                                                                                                                                                                                          
# connect to a "real" API                                                                                                                                                                 
                                                                                                                                                                                          
## Example: OpenWeatherMap                                                                                                                                                                
URL = "https://api.openweathermap.org/data/2.5/weather"                                                                                                                                   
                                                                                                                                                                                          
# TODO: get an API key from openweathermap.org and fill it in here!                                                                                                                       
API_KEY = "f0c1934825c1e5ee81482e3932a2c081"                                                                                                                                              
                                                                                                                                                                                          
def get_weather(city) -> Dict:                                                                                                                                                            
   res = requests.get(URL, params={"q": city, "appid": API_KEY})                                                                                                                          
   return res.json()                                                                                                                                                                      
                                                                                                                                                                                          
# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)                                                                                                    
                                                                                                                                                                                          
URL2 = "https://official-joke-api.appspot.com/jokes/random"                                                                                                                                            
                                                                                                                                                                                          
def get_joke() -> Dict:                                                                                                                                                             
   """                                                                                                                                                                                                                                                                                                                   
  gets a joke from the url """                                                                                                                                                                                    
   res = requests.get(URL2)                                                                                                                       
   return res.json()                                                                                                                                                                      
                                                                                                                                                                                          
def main():                                                                                                                                                                               
   temp = get_weather("London")                                                                                                                                                           
   print(temp)                                                                                                                                                                            
                                                                                         
   joke = get_joke()                                                                                                                                                        
   print(joke)                                                                                                                                                                            
                                                                                                                                                                                          
if __name__ == "__main__":                                                                                                                                                                
   main()      

