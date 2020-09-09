import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'symboling': "3",
                            'normalized-losses': "1",
                            'make': "ford",
                            'fuel-type': "gas",
                            'aspiration': "std",
                            'num-of-doors': "two",
                            'body-style': "convertible",
                            'drive-wheels': "rwd",
                            'engine-location': "front",
                            'wheel-base': "88.6",
                            'length': "168.8",
                            'width': "64.1",
                            'height': "48.8",
                            'curb-weight': "2548",
                            'engine-type': "dohc",
                            'num-of-cylinders': "four",
                            'engine-size': "130",
                            'fuel-system': "mpfi",
                            'bore': "3.47",
                            'stroke': "2.68",
                            'compression-ratio': "9",
                            'horsepower': "111",
                            'peak-rpm': "5000",
                            'city-mpg': "21",
                            'highway-mpg': "27",
                            'price': "13495",
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/38165fb830604bc798537417027af26f/services/05887d6169ee4391b4357492447d5cf8/execute?api-version=2.0&format=swagger'
api_key = "2FQE8WLSRhiFj6b/ENsdE2UquFy9Put0R6YT50EiscNoY3Xva0L6AENWf3nZ58t8wrqztgaCMFydJ5Q1yb9wXQ==" # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))