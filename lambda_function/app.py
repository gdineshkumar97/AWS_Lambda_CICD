import json
import requests
import pandas
import numpy
import os

def lambda_handler(event, context):
    
    print("Deployment via CICD")
    print("Event received:", event)
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()

    df = pandas.DataFrame(data)
    print(df.head())

    print("Environment Variables:")
    defined_variables = ["ENV", "API_KEY", "LOG_LEVEL"]
    for var in defined_variables:
        value = os.environ.get(var)
        if value is not None:
            print(f"{var}: {value}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched and printed successfully!')
    }