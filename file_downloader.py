from tqdm import tqdm 
import time
import requests
    
chunk_size = 1024

url = "data:image/jpeg;base64,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"
r = requests.get(url, stream = True)
total_size = int(r.headers['content-length'])

with open("Python.pdf", 'wb') as f:
    for data in tqdm(iterable = r.iter_content(chunk_size= chunk_size, total = total_size/chunk_size, unit="KB")):
        f.write(data)

print("Download Complete")