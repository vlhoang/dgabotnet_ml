import pandas
import math
from nltk import everygrams
import enchant

def cut_extend(d):
    i = 0
    while(i<len(d)):
        if d[i] == '.':
            d = d[:i]
            return d
        i = i+1
def ffeatures(domain):
    domain = cut_extend(domain)
    ts_bigrams = pandas.read_csv("all_bigrams.csv", converters={i: str for i in range(54872)})
    ts_trigrams = pandas.read_csv("all_trigrams.csv", converters={i: str for i in range(54872)})
    ds_bigrams = pandas.read_csv("bigrams_sorted.csv", converters={i: str for i in range(54872)})
    ds_trigrams = pandas.read_csv("trigrams_sorted.csv", converters={i: str for i in range(54872)})
    N = 1444
    M = 54872
    hexchars = "0123456789abcdefABCDEF"
    frequent = {"a": 9.35, "b": 2.27, "c": 3.87, "d": 3.26, "e": 9.69, "f": 1.67, "g": 2.4, "h": 2.56, "i": 7.4,
                "j": 0.55, "k": 1.9,
                "l": 4.65, "m": 3.37, "n": 6.12, "o": 7.28, "p": 2.91, "q": 0.21, "r": 6.44, "s": 6.48, "t": 6.13,
                "u": 3.23, "v": 1.37,
                "w": 1.2, "x": 0.67, "y": 1.67, "z": 0.68, "0": 0.18, "1": 0.24, "2": 0.23, "3": 0.15, "4": 0.16,
                "5": 0.1, "6": 0.09,
                "7": 0.09, "8": 0.1, "9": 0.08, ".": 0, "-": 1.26}
    domain = str(domain)
    domain = domain.lower()
    found_bi = []
    num_found_bi = []
    found_tri = []
    num_found_tri = []



    # find f1
    for j in range(len(domain) - 1):
        bi = domain[j:j + 2]
        if (bi not in found_bi):
            res = ds_bigrams[ds_bigrams["Bigrams"] == bi]
            if (res.empty == False):
                found_bi.append(bi)
                num_found_bi.append(1)
        else:
            pos = found_bi.index(bi)
            num_found_bi[pos] = num_found_bi[pos] + 1
    f1 = len(found_bi)

    # find f9
    for j in range(len(domain) - 2):
        tri = domain[j:j + 3]

        if (tri not in found_tri):
            res = ds_trigrams[ds_trigrams["Trigrams"] == tri]
            if (res.empty == False):
                found_tri.append(tri)
                num_found_tri.append(1)
        else:
            pos = found_tri.index(tri)
            num_found_tri[pos] = num_found_tri[pos] + 1
    f9 = len(found_tri)

    # find f2
    f2 = 0
    for i in range(f1):
        index = ts_bigrams.index[ts_bigrams["Bigrams"] == found_bi[i]][0] + 1
        f2 = f2 + (num_found_bi[i]*index)

    # find f10
    f10 = 0
    for i in range(f9):
        index = ts_trigrams.index[ts_trigrams["Trigrams"] == found_tri[i]][0] + 1
        f10 = f10 + (num_found_tri[i]*index)

    #find f3
    f3 = 0
    for i in range(f1):
        vt = ds_bigrams.index[ds_bigrams["Bigrams"] == found_bi[i]][0] + 1
        f3 = f3 + (num_found_bi[i]*vt)
    f3 = f3/f1

    #find f11
    f11 = 0
    for i in range(f9):
        vt = ds_trigrams.index[ds_trigrams["Trigrams"] == found_tri[i]][0] + 1
        f11 = f11 + (num_found_tri[i]*vt)
    f11 = f11/f9

    #find f4
    f4 = f2/len(domain)

    #find f12
    f12 = f10/len(domain)

    #find f5
    f5 = f3/len(domain)

    #find f13
    f13 = f11/len(domain)

    #find f6
    f6 = f1/len(domain)

    #find f14
    f14 = f9/len(domain)

    #find f7
    f7 = 0
    for i in range(f1):
        f7 = f7 + num_found_bi[i]
    f7 = f7/len(domain)

    #find f15
    f15 = 0
    for i in range(f9):
        f15 = f15 + num_found_tri[i]
    f15 = f15/len(domain)

    #find f8
    f8 = 0
    for i in range(f1):
        vt = ds_bigrams.index[ds_bigrams["Bigrams"] == found_bi[i]][0] + 1
        f8 = f8 + ((vt/N)*math.log10(vt/N))
    f8 = -f8

    #find f16
    f16 = 0
    for i in range(f9):
        vt = ds_trigrams.index[ds_trigrams["Trigrams"] == found_tri[i]][0] + 1
        f16 = f16 + ((vt/M)*math.log10(vt/M))
    f16 = -f16

    #find f17
    f17 = 0
    vowels = ['a','e','i','o','u']
    for i in range(len(domain)):
        if (domain[i] in vowels):
            f17=f17+1

    #find f18
    f18 = f17/len(domain)

    #find f19
    f19 = 0
    if (len(domain) == 1):
        f19 = 1
    else:
        for i in range(len(domain)):
            if (domain[i] not in hexchars):
                if (i != 0):
                    f19 = 1
                    break

    #find f20
    unq_chars = ''.join(set(domain))
    f20 = 0
    for char in unq_chars:
        f20 = f20 + (domain.count(char) * frequent[char])
    f20 = f20 / len(domain)

    #find f21
    # d = enchant.Dict("en_US")
    d = enchant.request_pwl_dict("wordlist.txt")
    kq = [''.join(_ngram) for _ngram in everygrams(domain) if d.check(''.join(_ngram)) and len(_ngram) > 1]
    f21 = len(kq)

    #find f22
    if (len(domain)<5): f22 = 1
    else: f22 = 0

    dfObj = pandas.DataFrame(
        columns=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13',
                 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22'])
    dfObj.loc[0] = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22]
    return dfObj
