import requests
import os
import time

#https://api.accredible.com/v1/credential/generate_certificate_pdf?credential_id=28013155&mode=pdf

baseurl = 'https://api.accredible.com/v1/credential/generate_certificate_pdf?mode=pdf&credential_id='
dirname = os.path.dirname(__file__)

for x in range(500):
    id = 28012850 + x 
    url = baseurl + str(id)
    r = requests.get(url, allow_redirects=True)
    
    filename = str(id) + '.pdf'
    completeName = os.path.join (dirname,'PDFS','20202021Sem1',filename)
    if(len(r.content) > 50000):
        print(f"{id} downloaded")
        open(completeName, 'wb').write(r.content)
    else:
        print(f"{id} empty")
    time.sleep(0.5)


