import xml.etree.ElementTree as ET


def xml_malumot_olish():
    import xml.etree.ElementTree as ET
    malumot = '''
    <odam>
        <ismi>Ulug'bek</ismi>
        <yili>1997</yili>
        <tel_nomer type="intl">
            +998930751753
        </tel_nomer>
    </odam>'''

    daraxt = ET.fromstring(malumot)
    print('Ismi:', daraxt.find('ismi').text)
    print('Tel nomeri:', daraxt.find('tel_nomer').text.strip())

def xml_loop_oila():
    import xml.etree.ElementTree as ET
    input = '''
    <oila>
        <bolalar>
            <bola>
                <nomer>1</nomer>
                <ism>Ali</ism>
            </bola>
            <bola>
                <nomer>2</nomer>
                <ism>Vali</ism>
            </bola>
        </bolalar>
    </oila>
    '''
    bolalar = ET.fromstring(input)
    lst = bolalar.findall('bolalar/bola')
    print('Bolalar soni:', len(lst))
    print('-----------------------')
    for element in lst:
        print('Ism', element.find('ism').text)
        print('Nomer', element.find('nomer').text)


def json_malumot_olish():
    import json

    malumot = '''
    [
        {   
            "nomer": "1",
            "ism": "Ali"    
        },
        {   
            "nomer": "2",
            "ism": "Vali"    
        }
    ]
    '''
    olingan_data = json.loads(malumot)
    print('Soni:', len(olingan_data))
    print('------------------------')
    for element in olingan_data:
        print('Ism: ', element['ism'])
        print('Nomeri: ', element['nomer'])

json_malumot_olish()

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




