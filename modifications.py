from natasha.doc import Doc
from natasha.extractors import AddrExtractor
from natasha.morph.vocab import MorphVocab

# MKR,
morph_vocab = MorphVocab()
addr_extractor = AddrExtractor(morph_vocab)

text = "Россия, Бурятия, мкр Баргузинский , Улан-Удэ, 20 лет октября, д. 7"
out = addr_extractor.find(text)
print(out)

# \n
text = "г. Москва-Захарова, \n\nИстринский район, сельское поселение Павло-Cл"
print(text)
out = addr_extractor.find(text)
print(out)

