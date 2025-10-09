import requests
url='http://127.0.0.1:5000/api/upload'
with open(r'd:\Satwik\AMITY\CYBERCUP 5.0\TechTitans\sample_upload.txt','rb') as f:
    files={'files': f}
    try:
        r = requests.post(url, files=files, timeout=10)
        print('status', r.status_code)
        print(r.text)
    except Exception as e:
        print('ERROR', e)
