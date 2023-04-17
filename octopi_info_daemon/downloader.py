import requests


def download(url, filepath):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    else:
        raise RuntimeError(f'Could not download {url} (request status {response.status_code})')
