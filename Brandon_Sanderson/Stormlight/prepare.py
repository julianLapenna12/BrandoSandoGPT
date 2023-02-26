import os
import requests
import tiktoken
import numpy as np

# download twok dataset
input_file_path = os.path.join(os.path.dirname(__file__), 'The_Way_of_Kings.txt') # scoop from file
if not os.path.exists(input_file_path): # or from url
    data_url = 'https://raw.githubusercontent.com/julianLapenna12/BrandoSandoGPT/master/Brandon_Sanderson/Stormlight/The_Way_of_Kings.txt'
    with open(input_file_path, 'w') as f:
        f.write(requests.get(data_url).text)

# text stored in data var
with open(input_file_path, 'r') as f:
    data = f.read()

# train and val split
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
