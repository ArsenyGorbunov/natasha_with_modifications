from natasha.doc import Doc
from natasha.extractors import AddrExtractor
from natasha.morph.vocab import MorphVocab

morph_vocab = MorphVocab()
addr_extractor = AddrExtractor(morph_vocab)

text = "Россия, Бурятия, Баргузинский р-н, Улан-Удэ, 20 лет октября, д. 7"
out = addr_extractor.find(text)
print(out)
