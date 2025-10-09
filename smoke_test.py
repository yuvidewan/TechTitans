import requests

print('Checking health...')
try:
    r = requests.get('http://127.0.0.1:5000/', timeout=5)
    print('Health status', r.status_code)
    print(r.text)
except Exception as e:
    print('Health check failed:', e)

print('\nUploading sample file...')
try:
    with open('sample_upload.txt','rb') as f:
        r = requests.post('http://127.0.0.1:5000/api/upload', files={'files': f}, timeout=10)
        print('Upload status', r.status_code)
        print(r.text)
except Exception as e:
    print('Upload failed:', e)
