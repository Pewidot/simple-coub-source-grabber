#Coub Url generator Script by Moritz Henseleit
#reminder you have to install beautifulsoup4 with "pip install beautifulsoup4"
import webbrowser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'} #defining the used Web User Agent
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = input("Insert Coub Share URL: ") 
uClient = uReq(my_url)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
search = '{"default":"' #defining unique javascript parts to search for the start
search_end = '"}},"audio_versions' #defining unique javascript parts to search for the end
start_index = str(page_soup).find(search) #searching for the javascript part where the akamaihd source starts
end_index = str(page_soup).find(search_end) #searching for the javascript part where the akamaihd source ends
html_to_string = str(page_soup) #converting to string
global_key = html_to_string[start_index+12:end_index] #grabbing the exact akamaihd link to the video and audio source
print("Opening Browser with this URL: "+global_key) #prints out the url to the source
webbrowser.open_new(global_key) #optional opens the url in the standard browser
uClient.close()





