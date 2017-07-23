def factorial(n):
  '''returns n!'''
  return 1 if n<2 else n*factorial(n-1)

help(factorial) # returns text written between '''text'''

print(list(map(factorial,range(11))))

text = ['aa','dasdas','d','sadasdaggdf']
print(sorted(text,key=len)) #len function returns size and sorted sorts from lower to higher
