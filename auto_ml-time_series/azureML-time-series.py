import requests
import json
from datetime import timedelta, date, datetime

# Periode van voorspelling
start_date = date(2019, 12, 5)
end_date = date.today()

length = 13
needed_length = 10

epoch_time = 1576195200
datetime_time = datetime.fromtimestamp(epoch_time)
print(datetime_time)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))

    # URL for the web service
    scoring_uri = 'http://ed91ac85-301c-48fc-8cd9-9d648055e4df.westeurope.azurecontainer.io/score'
    # If the service is authenticated, set the key or token
    # key = '<your key or token>'

    # example payload for bike share forecast future (next day)
    data = {"data":
        [
            {
                "Order_Date": str(single_date),
            }
        ]
    }

    # Convert to JSON string
    input_data = json.dumps(data)

    # Set the content type
    headers = {'Content-Type': 'application/json'}
    # If authentication is enabled, set the authorization header
    # headers['Authorization'] = f'Bearer {key}'

    # Make the request and display the response
    resp = requests.post(scoring_uri, input_data, headers=headers)
    print(resp.text)