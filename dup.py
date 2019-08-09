a=[12,24,35,24,88,120,155,88,120,155]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
print(uniq_items) 
