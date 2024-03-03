import requests

# Replace this URL with the actual endpoint URL for your deployed function
url = 'https://your-region-your-project.cloudfunctions.net/addmessage'

# Send a POST request
params = {'text': 'Your sample message'}

# Print the response text
print(response.text)
