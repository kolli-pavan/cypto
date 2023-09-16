from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import requests

def home(req):
    
   
    data={
        "rates":{
            "A":500,
            "B":1000,
            "C":1500,
            "D":2000,
            "E":500,
            "F":1000,
            "G":1500,
            "H":2000,
            "I":500,
            "J":1000,
            "K":1500,
            "L":2000,
            "M":500,
            "N":1000,
            "O":1500,
            "P":2000,
            "Q":500,
            "R":1000,
            "S":1500,
            "T":2000,
            "U":500,
            "V":1000,
            "W":1500,
            "X":2000,
            "Y":500,
            "Z":1000,
            "a":1500,
            "b":2000,
            "c":500,
            "d":1000,
            "e":1500,
            "f":2000,
            "g":500,
            "h":1000,
            "i":1500,
            "j":2000,
            "k":500,
            "l":1000,
            "n":1500,
            "o":2000,
            "p":500,
            "q":1000,
            "r":1500,
            "s":2000,
            "AB":500,
            "DE":1000,
            "gh":1500,
            "jk":2000
        }
    }
    # url="http://api.coinlayer.com/live?access_key=5cacfe54c30271b5182606c4fd5895cb"
    # data=requests.get(url).json()
    # print(data["rates"])
    

    return render(req,'project/index.html',{'data':data["rates"]})

    return HttpResponse("Om Sri Jai")

# Create your views here.
