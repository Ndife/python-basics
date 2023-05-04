
set1 = { "uche", "king", "make"}
set2 = {"uche", 'make'}

intersect = set1 & set2     # intersection
mod = set1 | set2       # union
dif =  set1 - set2      # difference
sup = set1 > set2       # super set
setLength = len(set1)   # set length 

print(list(set1))       # convert set to list | Arrau
print(set1)