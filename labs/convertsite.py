import requests
import urllib.parse
import config as cfg

target_url = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"

api_key = cfg.config["htmltopdfkey"]

api_url = "https://api.html2pdf.app/v1/generate"

params = {"url":target_url, "apikey":api_key }
parsed_params = urllib.parse.urlencode(params)
request_url = api_url +"?"+ parsed_params

response = requests.get(request_url)
print (response.status_code)