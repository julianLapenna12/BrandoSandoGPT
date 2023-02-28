# BrandoSandoGPT

Based on [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT) this is a GPT model that generates text in the style of the author Brandon Sanderson.

Texts available to train from:
- The Way of Kings
- Words of Radiance
- Edgedancer
- Oathbringer
- Dawnshard
- Rhythm of War
 
with more on the way!

## Training Guide

### 1. Prepare the tokenized dataset by running
```
$ python3 Brandon_Sanderson/Stormlight/prepare.py {name of book here}
```
If no book name is provided it defaults to using all Stormlight books as text to train on, otherwise the following options lets you select which book to train on:
- `twok`
- `wor`
- `o`
- `row`
- `dawn`
- `edge`

Note: If you want to train the model on a specific subset of the books, call 
```
python3 Brandon_Sanderson/Stormlight/append_file.py --output_file.txt --book1.txt --book2.txt --book3.txt
```


### 2. Train the model 

On lighter machines (i.e. laptops, macbooks) the model can only be trained on smaller paramaters
```
$ python train.py config/train_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```
or on heavier machines, we can use the full set
```
$ python train.py config/train_char.py
```

### 3. Finally, sample from the model
```
$ python3 sample.py --out_dir=out-sanderson-char
```
and sample paragraphs will be generated to the command line.

TODO:
- train on gpu
- add better transition between cpu and gpu
-
