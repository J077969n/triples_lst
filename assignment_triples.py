from os import lstat


lst = [1,2,3,4,5,6,7]

def triples(lst):
    return lst* 3

triples_lst = list(map(triples,lst))
print(triples_lst)