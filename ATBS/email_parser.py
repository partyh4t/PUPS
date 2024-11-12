

# email web parser - WIP

import re
import requests

domain_name = 'https://owasp.org'

# performs a get request to a given domain
def webRequest(domain):
    content = requests.get(domain).content
    return content
    
# parsers emails from http response with regex
def emailParser(content):
    regex = re.compile(r'([\w\.-]+)@([a-zA-Z0-9]+)\.?(com|org|net|gov)?')
    for i in content:
        match = regex.search(i)
        if match:
            print(match.group())

http_content = webRequest(domain_name)
emailParser(http_content)