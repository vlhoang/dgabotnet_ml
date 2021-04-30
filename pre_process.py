import string
import pandas
def cut_extend(d):
    i = 0
    while(i<len(d)):
        if d[i] == '.':
            d = d[:i]
            return d
        i = i+1

def find_all_2grams(input_list):
    kq = []
    for i in range(len(input_list)):
        for j in range(len(input_list)):
          kq.append(str(input_list[i]+input_list[j]))
    return kq

def find_all_3grams(input_list):
    kq = []
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            for k in range(len(input_list)):
                kq.append(str(input_list[i]+input_list[j])+input_list[k])
    return kq

def find_ngrams(input_list, n):
    zipped_res = zip(*[input_list[i:] for i in range(n)])
    return ["".join(ngram) for ngram in zipped_res]
# print (cut_extend("example.ta"))

chars = string.ascii_lowercase + string.digits + ".-"

#all bigrams to csv
# bigrams = find_all_2grams(chars)
# df = pandas.DataFrame(columns=['Bigrams'])
# for i in range(len(bigrams)):
#     t = bigrams[i]
#     df.loc[i] = t
# df.to_csv("all_bigrams.csv")

#all trigrams to csv
# trigrams = find_all_3grams(chars)
# df = pandas.DataFrame(columns=['Trigrams'])
# for i in range(len(trigrams)):
#     t = trigrams[i]
#     df.loc[i] = t
# df.to_csv("all_trigrams.csv")

#strip normal domains

# listdomain = pandas.read_csv("top350000_domain.csv")
# df = pandas.DataFrame(columns=['Name'])
# count = 0
# for i in range(len(listdomain)):
#     t = cut_extend(listdomain.at[i, "Name"])
#     if (len(t)>=3 and t.find("_") == -1):
#         if(t.isdigit()):
#             t = "'" + t
#         t = t.lower()
#         df.loc[count] = t
#         print(str(count)+" "+t)
#         count = count+1
# df.to_csv("top350000domain_stripped.csv")

#strip dga domains

# listdomain = pandas.read_csv("top320000_dga.csv")
# df = pandas.DataFrame(columns=['Name'])
# count = 0
# for i in range(len(listdomain)):
#     t = cut_extend(listdomain.at[i, "Name"])
#     if (len(t)>=3):
#         df.loc[count] = t
#         print(str(count)+" "+t)
#         count = count + 1
# df.to_csv("top320000dga_stripped.csv")



#find ds(bigram)
# listdomain = pandas.read_csv("top320000domain_stripped.csv")
# num_appear={}
# bigrams = find_all_2grams(chars)
# for i in range(len(bigrams)):
#     num_appear[bigrams[i]] = 0;
# for i in range(len(listdomain)):
#     t = listdomain.at[i,"Name"]
#     t = str(t)
#     t = t.lower()
#     print(t)
#     for j in range(len(t)-1):
#         bi=t[j:j+2]
#         print(bi)
#         num_appear[bi] = num_appear[bi]+1
# # print(num_appear)
# for i in range(len(bigrams)-2):
#     for j in range(len(bigrams)-1,i,-1):
#         if(num_appear[bigrams[i]]<num_appear[bigrams[j]]):
#             temp = bigrams[i]
#             bigrams[i] = bigrams[j]
#             bigrams[j] = temp
# print(bigrams)
# df = pandas.DataFrame(columns=['Bigrams'])
# for i in range(len(bigrams)):
#     df.loc[i] = bigrams[i]
# df.to_csv("bigrams_sorted.csv")

#find ds(trigram)
listdomain = pandas.read_csv("top320000domain_stripped.csv")
num_appear={}
chars = string.ascii_lowercase + string.digits + ".-"
trigrams = find_all_3grams(chars)
for i in range(len(trigrams)):
    num_appear[trigrams[i]] = 0;
for i in range(len(listdomain)):
    t = listdomain.at[i,"Name"]
    t = str(t)
    t = t.lower()
    print(t)
    for j in range(len(t)-2):
        tri=t[j:j+3]
        print(tri)
        num_appear[tri] = num_appear[tri]+1
print(num_appear)
# for i in range(len(trigrams)-2):
#     for j in range(len(trigrams)-1,i,-1):
#         if(num_appear[trigrams[i]]<num_appear[trigrams[j]]):
#             temp = trigrams[i]
#             trigrams[i] = trigrams[j]
#             trigrams[j] = temp
import operator
sorted = sorted(num_appear.items(), key=operator.itemgetter(1), reverse=True)
print(sorted)
df = pandas.DataFrame(columns=['Trigrams'])
for i in range(len(trigrams)):
    df.loc[i] = sorted[i][0]
df.to_csv("trigrams_sorted.csv")