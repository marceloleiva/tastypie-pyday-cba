import json
import requests


def post_tweet(user, tweet):
    url = "http://127.0.0.1:8000/api/v1/tweet/"
    data = {'user': user, 'tweet': tweet * 100}
    headers = {'content-type': 'application/json'}
    return requests.post(url, data=json.dumps(data), headers=headers)

if __name__ == '__main__':
    r = post_tweet('/api/v1/user/1/', 'Chau mundo')
    print r.status_code
    print r.content
