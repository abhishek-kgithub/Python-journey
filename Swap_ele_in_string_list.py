li=['Gfg','is','best','for','Geeks']
print(str(li))
res=[i.replace('G','-').replace('e','G').replace('-','e')  for i in li]
print(str(res))