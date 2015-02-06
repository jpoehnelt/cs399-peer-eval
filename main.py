import requests
"""
https://github.com/lf237/theatre/graphs/contributors
https://github.com/c1phr/cs399_theatre/graphs/contributors
https://github.com/dukeayers/cs399_theater
"""


repos = ['http://api.github.com/repos/lf237/theatre/collaborators']


for repo in repos:
    request = requests.get(repo)
    print request.json