import requests
import os
import time


baseurl = 'https://api.accredible.com/v1/credential/generate_certificate_pdf?mode=pdf&credential_id='
dirname = os.path.dirname(__file__)

for x in range(500):
    id = 34255600 + x 
    url = baseurl + str(id)

    try:
        r = requests.get(url, allow_redirects=True, timeout=6)
        filename = str(id) + '.pdf'
        completeName = os.path.join (dirname,'PDFS','20202021Sem2',filename)
        if(len(r.content) > 50000):
            print(f"{id} downloaded")
            open(completeName, 'wb').write(r.content)
        else:
            print(f"{id} empty")
    except:
            print(f"{id} timeout")

    time.sleep(0.5)


