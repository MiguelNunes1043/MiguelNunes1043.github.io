import requests
import json
#a
key = "AIzaSyBHCtB8LDXx7Hgee6Fabrf1Smi_Sk4uAvQ"

def getBookByMostRelevant(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q="+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookByTitle(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=intitle:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookByAuthor(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=inauthor:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookByPublisher(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=inpublisher:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookBySubject(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=subject:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookByISBN(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=isbn:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookByLCCN(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=lccn:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()

def getBookByOCLC(str):
    apiURL="https://www.googleapis.com/books/v1/volumes?q=oclc:"+str+"&key="+key
    response = requests.get(apiURL)
    return response.json()



if __name__=="__main__":
    print(getBookByTitle("name of the wind"))