import os
import requests
import tiktoken
import numpy as np
import sys

data_url = 'https://raw.githubusercontent.com/julianLapenna12/BrandoSandoGPT/master/Brandon_Sanderson/Stormlight/'

match sys.argv[1].lower():
    case 'twok':
        file_name = 'The_Way_of_Kings.txt'
    case 'wor':
        file_name = 'Words_of_Radiance.txt'
    case 'o':
        file_name = 'Oathbringer.txt'
    case 'row':
        file_name = 'Rhythm_of_War.txt'
    case 'dawn':
        file_name = 'Dawnshard.txt'
    case 'edge':
        file_name = 'Edgedancer.txt'
    case _:
        file_name = 'all.txt'


data_url += file_name

# download twok dataset
input_file_path = os.path.join(os.path.dirname(__file__), file_name) # scoop from file
if not os.path.exists(input_file_path): # or from url
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

print(__file__)
# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data/train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data/val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
