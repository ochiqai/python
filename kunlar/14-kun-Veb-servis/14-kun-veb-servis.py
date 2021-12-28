import xml.etree.ElementTree as ET


def bir():
    input = '''
    <stuff>
    <users>
    <user x="2">
    <id>001</id>
    <name>Chuck</name>
    </user>
    <user x="7">
    <id>009</id>
    <name>Brent</name>
    </user>
    </users>
    </stuff>'''

    stuff = ET.fromstring(input)

    lst = stuff.findall('users/user')
    print('User count:', len(lst))
    lst2 = stuff.findall('user')
    print('User count:', len(lst2))

def ikki_xml_fayl():
    data = ET.parse("misol_xml.xml")
    lst = data.findall("book")
    print(len(lst))
    for element in lst:
        print(element.attrib['id'])
        print(element.find('author').text)


def uch_json_fayl():
    import json

    data = '''
    [
        { "id" : "001",
        "x" : "2",
        "name" : "Chuck"
        } ,
        { "id" : "009",
        "x" : "7",
        "name" : "Brent"
        }
    ]
    '''

    lst = json.loads(data)

    for element in lst:
        print(element['id'])
        print(element['x'])
        print(element['name'])


def google_geocofing_api():
    import urllib.request, urllib.parse, urllib.error
    import json
    import ssl

    api_key = "AIzaSy___IDByT70"
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else:
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print(json.dumps(js, indent=4))

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)


google_geocofing_api()

