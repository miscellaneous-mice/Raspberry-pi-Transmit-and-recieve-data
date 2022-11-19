import requests 
from datetime import datetime
import time
import statistics
import json
 
  
string2={"data":"4095,4095,4095"}
for i in [1,3,5]:
  res = requests.post(url="http://jhaabhay10.pythonanywhere.com/todo"+str(i), data=string2)               #posting string2 on website
                                                                                                          #string to be posted should be in format of
                                                                                                          #{"data":"number1,number2,number3"}
                                                                                                          #follow the same pattern if you want to post separate numbers
while(1):
  print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  for i in [1,3,5]:
    temp=str(requests.get("http://jhaabhay10.pythonanywhere.com/todo"+str(i)).json())                         #gets the data from the website
    #print(str(i)+":"+temp)
    vals=temp.split(',')
    arr=[int(i) for i in vals]
    print(arr)                                                                                                #printing extracted from website
    dat=int(statistics.mean(arr)*255/4095)
    print(dat)
    res = requests.post(url="http://jhaabhay10.pythonanywhere.com/todo"+str(i+1), data={"data":dat})          #posts the data on website
  time.sleep(3)
  print()
  print()
  print()
