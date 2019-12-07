class ndict(dict):
    
    def __missing__(self,key):
        print('can\'t find')
        # super.__missing__(self,key)

    def __contains__(self,item):
        print('not\'t in the container')

    def __delitem__(self,key):
        print('delete item')

    def __getitem__(self,key):
        # print(key)
        pass

    def __setitem__(self,key,value):
        print('set the {} of {} is {}'.format(key,self,value))
        # object.__setitem__(self,key,value)
       

a = {'a':1,'b':2}
na = ndict(a)
b = 3 in na
print(na)
print(na['c'])
c = na['b']
na.setdefault('c',3) 
na['b']=3
del na['a']

pass
