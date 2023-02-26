# BrandoSandoGPT

Based on [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT) this is a GPT model that generates text in the style of the author Brandon Sanderson.

Texts available to train from:
- TWoK
- WoR
- Edgedancer
- Oathbringer
- Dawnshard
- RoW
 
with more on the way!

### Training Guide

Prepare the tokenized dataset by running
```
$ python3 Brandon_Sanderson/Stormlight/prepare.py {name of book here}
```
If no book name is provided it defaults to using all Stormlight books as text to train on, otherwise the following options lets you select which book to train on:
- `'twok'`
- `'wor'`
- `'o'`
- `'row'`
- `'dawn'`
- `'edge'`

Next train the model by running 
```
$ python train.py config/train_shakespeare_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```


TODO:
- train on gpu
- add better transition between cpu and gpu
-
