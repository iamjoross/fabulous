"""~map <search term> <map service> return the map of the <search term> from <map service>. The default map service is Google Maps"""

try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re
import requests
from random import shuffle


def unescape(url):
    # for unclear reasons, google replaces url escapes with \x escapes
    return url.replace(r"\x", "%")


def map(searchterm, unsafe=False):
    # searchterm = quote(searchterm)

    # safe = "&safe=" if unsafe else "&safe=active"
    # searchurl = "https://www.google.com/search?tbm=isch&q={0}{1}".format(searchterm, safe)

    # # this is an old iphone user agent. Seems to make google return good results.
    # useragent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Versio  n/4.0.5 Mobile/8A293 Safari/6531.22.7"

    # result = requests.get(searchurl, headers={"User-agent": useragent}).text

    # images = list(map(unescape, re.findall(r"var u='(.*?)'", result)))
    # shuffle(images)

    # if images:
    #     return images[0]
    # else:
    #     return ""
    pass


def on_message(msg, server):
    text = msg.get("text", "")
    # match = re.findall(r"~map (.*)", text)
    match = re.findall(r"~map (.*)( -service=youtube)", text)
    print(match)
    if not match:
        return

    searchterm = match[0]
    return map(searchterm.encode("utf8"))

on_bot_message = on_message
