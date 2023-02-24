import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# path = r'/home/julian/Documents/Projects/BrandoSandoGPT/Brandon Sanderson/Stormlight/The_Way_of_Kings'
# path = r'/home/julian/Documents/Projects/BrandoSandoGPT/Brandon Sanderson/Stormlight/Words_of_Radiance'
# path = r'/home/julian/Documents/Projects/BrandoSandoGPT/Brandon Sanderson/Stormlight/Oathbringer'
path = r'/home/julian/Documents/Projects/BrandoSandoGPT/Brandon Sanderson/Stormlight/Rhythm_of_War'
# https://colab.research.google.com/github/ZA3karia/PDF2TEXT/blob/master/ebook_to_text.ipynb#scrollTo=655qYKDx2UYU

def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
]
def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output
def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output
def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext

out = epub2text(path + '.epub')

# out = out[5:106] # TWoK
# out = out[9:140] # WoR
# out = out[9:172] # O
out = out[10:169] # RoW

txtout = []

for _ in out:
    _ = _.replace("\n ", '')
    _ = _.replace("*\xa0", '')
    _ = _.replace("\xa0*", '')
    _ = _.replace("'\xa0", '')
    txtout.append(' '.join(_.split()))

with open(path+".txt", "a") as myfile:
    for _ in txtout:
        myfile.write(_)