import requests

# Define the URL you want to request data from
url = 'https://mc-api-j0rn.onrender.com/api/news'  # Example URL

try:
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response content
        print('Response Content:')
        print(response.text)
    else:
        print(f'Error: Received status code {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
