# coding: utf-8

from .base import ObjectifyProperty

#### PURE STRING ####
class String(ObjectifyProperty):
    """ An ASCII string """
    
    __slots__ = ()

    to_type=str
    
    def example_value(self):
        return "Serious sample string"

    def _to_type(self,value):
        return intern(self.to_type(value))


class Str(ObjectifyProperty):
    """ An ASCII string """
    
    __slots__ = ()

    to_type=str
    
    def example_value(self):
        return "Serious sample string"

    def _to_type(self,value):
        return intern(self.to_type(value))

class TrimmedString(ObjectifyProperty):
    """ An ASCII string with whitespace padding removed """

    __slots__ = ()

    to_type=str
    
    def example_value(self):
        return "Serious sample string"

    def _to_type(self,value):
        return intern(self.to_type(value).strip())



#### UNICODE ####

class Unicode(ObjectifyProperty):
    """ A Unicode (UTF-8) string """

    __slots__ = ()

    to_type = unicode
    #Charset for unicode encoding
    __unicode_charset__ = 'utf-8'


    def _to_type(self,value):
        if not isinstance(value, unicode):
            return self.to_type(value,self.__unicode_charset__)
        return value

    
    def example_value(self):
        return u"Serious utf8 string"
        

class TrimmedUnicode(ObjectifyProperty):
    """ A Unicode (UTF-8) string with whitespace padding removed """

    __slots__ = ()

    to_type = unicode
    #Charset for unicode encoding
    __unicode_charset__ = 'utf-8'

    def _to_type(self,value):
        if not isinstance(value, unicode):
            return self.to_type(value,self.__unicode_charset__).strip()
        return value.strip()

    
    def example_value(self):
        return u"Serious utf8 string"

