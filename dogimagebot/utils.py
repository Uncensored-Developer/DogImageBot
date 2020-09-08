import requests


def get_image_url():
    req = requests.get('https://random.dog/woof.json')
    res = req.json()
    return res.get('url', None)
