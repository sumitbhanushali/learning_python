# == compares equality of content of two objects and is compares id of two objects
# tuples contain references of objects like lists so when lists are changed, change in tuple is also reflected
#to shallow copy a list l2 = list(l1)
# or list l2 = l1[:]
#copy module provides copy and deepcopy
#mutable objects like lists are passed as reference to functions
#avoid mutable objects as default parameters in functions because in such case list is shared among instances when instances are not given those optional parameters, to avoid this make copy by list(l1) 
