# from nltk import everygrams
# # import enchant
# # domain_cut = 'shopwithus'
# # #d = enchant.Dict("en_US")
# # d = enchant.request_pwl_dict("wordlist.txt")
# # # Exclude single char words.
# # kq = [''.join(_ngram) for _ngram in everygrams(domain_cut) if d.check(''.join(_ngram)) and len(_ngram) > 1]
# # # print(len(kq))
# # print(kq)
# import pandas
# import numpy as np
# ds_trigrams = pandas.read_csv("trigrams_sorted.csv",converters={i: str for i in range(54872)})
# tri = "021"
# res = ds_trigrams[ds_trigrams["Trigrams"] == tri]
# print (res)
from features import ffeatures
domain = "google.com"
print (ffeatures(domain).head())