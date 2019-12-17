#!/usr/bin/env python3.8

import requests

IPINFO_URL = "http://ipinfo.io/{ip}/json"


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""

    with requests.Session() as s:
        resp = s.get(IPINFO_URL.format(ip=ip_address))

        if resp.status_code == 200:
            resp_json = resp.json()

            return resp_json["country"]


if __name__ == "__main__":
    country = get_ip_country("187.190.38.36")
    print(country)

"""
Bite 111. Use the ipinfo API to lookup IP country ☆
In this Bite you will use the requests library to make a GET request to the ipinfo service.

Use IPINFO_URL and parse the (2 char) country code from the obtained json response.

Note how we mocked out the requests.get call in the tests, you can see another example of this in our Parsing Twitter Geo Data and Mocking API Calls by Example article.

Querying APIs is a common need so this should become second nature :) - enjoy!

Example return:

{
    ip: "187.190.38.36",
    hostname: "fixed-187-190-38-36.totalplay.net",
    city: "Mexico City",
    region: "Mexico City",
    country: "MX",
    loc: "19.4285,-99.1277",
    org: "AS17072 TOTAL PLAY TELECOMUNICACIONES SA DE CV",
    postal: "03020",
    timezone: "America/Mexico_City",
    readme: "https://ipinfo.io/missingauth"
}
"""
