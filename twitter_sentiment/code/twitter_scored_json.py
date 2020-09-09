import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'sentiment_label': "1",
                            'tweet_text': "This is a good test",
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/38165fb830604bc798537417027af26f/services/5a277c295a8e4644b5aa0910d36a7150/execute?api-version=2.0&format=swagger'
api_key = 'hUbZSxannXe8gMcSYCd3x4r0n2N1nRtlMoL1U+cGaLBIESArVP6JmXfloPIz2X8JVIwpH87ZQu77e0/udu2YJQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result[-65:-4])



except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
