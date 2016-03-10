#coding: utf-8

class TestParam(object):
    pass

class Test(object):
    test_param = TestParam()



print "Test", id(Test)
print "TestParam", id(TestParam)
print "Test.TestParam", id(Test.test_param)

z = Test()
print "Test()", id(z)
print "Test().TestParam", id(z.test_param)

print "2Test().TestParam", id(Test().test_param)