# This lab is to write a module to interact with the API Andrew created

import requests
import json 

url = "https://andrewbeatty1.pythonanywhere.com/books"


def read_books():
    response = requests.get(url)
    print("Status code:", response.status_code)
    return response.json()

def read_books_by_id(id):
    get_url = url + "/" + str(id)
    response = requests.get(get_url)
    print("Status code:", response.status_code)
    return response.json()

def create_book(book):
    response = requests.post(url, json=book)
    print("Status code:", response.status_code)
    return response.json()

def update_book(id, book):
    get_url = url + "/" + str(id)
    response = requests.put(get_url, json=book)
    print("Status code:", response.status_code)
    return response.json()

def delete_book(id):
    get_url = url + "/" + str(id)
    response = requests.delete(get_url)
    print("Status code:", response.status_code)  
    return response.json()



if __name__ == "__main__":
    print(delete_book(1624))