# coding: utf-8

class Tester(object):
    
    def test(self,a,*args,**kwargs):
        print args
        return a
    

zz = Tester()

#print zz.test('a')
print zz.test('a',b='b')