# import requests module
import requests
from requests.auth import HTTPBasicAuth

# Making a get request method
def GetJsonAPI(webaddress, username, password):
    
    response = requests.get(str(webaddress),
			auth = HTTPBasicAuth(str(username), str(password)))
    
    return (response.json())

