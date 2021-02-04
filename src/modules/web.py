import requests
import io

def get_url_as_binary(url):
    r = requests.get(url)
    if r.status_code == 200:
        return io.BytesIO(r.content)
    else:
        return None


def get_url_as_text(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        return None
