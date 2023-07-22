from itertools import combinations

rep = ["AA", "RR", "NN", "DD", "CC", "QQ", "EE", "GG", "HH", "II", "KK", "LL", "MM",
       "FF", "SS", "TT", "WW", "YY", "VV"]
al = "ARNDCQEGHIKLMFSTWYV"
st = list(combinations(al, 2))


# add the combinaitons along with the values, simultaneously reverse the keys and add the color codes,
# Next, add the double repeated ones with their color codes.
# There should be 190 key value pairs.

lis = []
dic = {}
for each in st:
    st = ''
    for a in range(2):
        st = st+each[a]
    lis.append(st)
    dic[st] = ''
#lis = lis+rep

print(len(lis))
# print(dic)
