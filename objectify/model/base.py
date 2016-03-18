# coding: utf-8

#In order of performance
try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

from ..base import ObjectifyObject

class ObjectifyModel(ObjectifyObject):

    __slots__ = (
        '__fetch_attr__',
        '__key_name__',
        '__fetch_attrs__',
        '__fetch_key__',
        '__serializer_ref__',
        '__deserializer_ref__'
    )

    
    __serializer__ = json.dumps
    __deserializer__ = json.loads
    

    def __init__(self,name=None,fetch_key=False,fetch_attrs=[],
            serializer=None,deserializer=None,**kwargs):
        super(ObjectifyModel, self).__init__(
            name=name,
            fetch_key=fetch_key,
            fetch_attrs=fetch_attrs,
            serializer=serializer,
            deserializer=deserializer,**kwargs
        )
        self.__fetch_attr__ = None

        self.__key_name__ = name
        self.__fetch_attrs__ = frozenset(fetch_attrs)
        self.__fetch_key__ = fetch_key

        if serializer is not None:
            self.__serializer_ref__ = serializer
        else:
            self.__serializer_ref__ = self.__serializer__
        
        if deserializer is not None:
            self.__deserializer_ref__ = deserializer
        else:
            self.__deserializer_ref__ = self.__deserializer__


        default = kwargs.get("default",None)
        if default:
            self.from_collection(default)


    def fetch_key_value(self):
        return getattr(self,self.__fetch_attr__)

    def set_fetch_key_value(self,val):
        return setattr(self,self.__fetch_attr__,val)

    @property
    def _serializer(self):
        return self.__serializer_ref__

    @property
    def _deserializer(self):
        return self.__deserializer_ref__

    def serialize(self):
        return self._serializer(self.to_collection())

    def deserialize(self,val):
        return self.from_collection(
            self._deserializer(val)
        )

    def copy_inited(self,keep_name=True):
        kwargs_dict = self._kwargs_to_dict()
        if keep_name:
            kwargs_dict['name'] = self.__key_name__

        return self.__class__(
            *self.__init_args__,
            **kwargs_dict
        )

    def example_value(self):
        raise NotImplementedError()