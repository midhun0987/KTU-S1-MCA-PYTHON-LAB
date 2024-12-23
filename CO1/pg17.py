#17. Sort dictionary in ascending and descending order.
 
d={"apple":1 ,"pineapple":3,"kiwi":4,"banana":2}
print(" original dictionary is",d)
aresult=dict(sorted(d.items()))
print("dictionary in ascending order",aresult)
dresult=dict(sorted(d.items(),reverse=True))
print("dictionary in decending order",dresult)