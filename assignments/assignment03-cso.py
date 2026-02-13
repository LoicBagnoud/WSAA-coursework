# The following program will retrieve the dataset for the 
# "exchequer account (historical series)" from the CSO, and store it into a file called "cso.json

# Author: Loic Bagnoud

# We import our packages
import requests
import json

# Get the Get URL from the CSO
url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D"

# We write our function that gets the URL (printing the status code for info) 
# We transform that response into Json format and write into a file.
def get_data():
    response = requests.get(url)
    print("Status code:", response.status_code)
    data = response.json()

    with open("cso.json", "w") as outfile:
        json.dump(data, outfile)

print(get_data())