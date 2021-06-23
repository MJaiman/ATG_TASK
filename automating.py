import requests
while(True):
    response = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=00b132eaffa09b62a9ff098a3b86047d&user_id=193283850%40N03&format=json&nojsoncallback=1')
    print(response.json())
    if response.status_code == 200:
        print('Request Succesfull')
    else:
        print('Error')
        break