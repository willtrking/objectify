# coding: utf-8

from bisect import bisect_left

class ObjectifyObject(object):

    __slots__ = (
        '__init_args__',
        '__init_kwargs_keys__',
        '__init_kwargs_key_orig_idx__',
        '__init_kwargs_values__'
        #'__init_kwargs__'
    )

    #__init_args__ = []
    #clear__init_kwargs__ = {}

    def __init__(self,*args,**kwargs):
        self.__init_args__ = args
        
        #Tuples as we'll prefer memory reduction
        #to lookup performance


        key_places = []
        for idx,key in enumerate(kwargs.iterkeys()):
            key_places.append((idx,key))

        key_places = sorted(key_places,key=lambda t: t[1])
        key_places = zip(*key_places)


        self.__init_kwargs_keys__ = key_places[1]
        self.__init_kwargs_key_orig_idx__ = key_places[0]

        self.__init_kwargs_values__ = tuple(
            kwargs.values()
        )


        #self.__init_kwargs__ = kwargs

    def __repr__(self):
        return '<%sclear.%s object at %s>' % (
            self.__class__.__module__,
            self.__class__.__name__,
            hex(id(self))
        )
    
    def fetch(self):
        raise NotImplementedError()

    def fetch_from(self,frm,**kwargs):
        raise NotImplementedError()

    def transform_fetch(self,fetched):
        raise NotImplementedError()
        
    def to_collection(self):
        raise NotImplementedError()

    def from_collection(self,frm):
        raise NotImplementedError()

    #def _kwargs_contains_keys(self,key):
    #    return (key <= lst[-1]) and (lst[bisect_left(lst, item)] == item)

    def _kwargs_key_index(self,key):
        #Get the ORIGINAL index of the key

        i = bisect_left(self.__init_kwargs_keys__, key)
        if (i != len(self.__init_kwargs_keys__) and 
                self.__init_kwargs_keys__[i] == key):
            return self.__init_kwargs_key_orig_idx__[i]

        raise ValueError


    def _kwargs_value(self,key,*args,**kwargs):
        args_len = len(args)

        if args_len > 1:
            raise TypeError

        if args_len > 0 and kwargs:
            raise TypeError

        if len(kwargs.keys()) > 1:
            raise TypeError

        if kwargs and 'default' not in kwargs:
            raise TypeError

        _do_def = False
        if args_len == 1:
            _def = args[0]
            _do_def = True

        if 'default' in kwargs:
            _def = kwargs['default']
            _do_def = True

        try:
            return self.__init_kwargs_values__[
                self._kwargs_key_index(key)
            ]
        except ValueError as e:
            if _do_def:
                return _def
            else:
                raise e

    def _kwargs_to_dict(self):
        r = {}

        for k in self.__init_kwargs_keys__:
            r[k] = self._kwargs_value(k)

        return r



    #Return a duplicate object with the init args/kwargs used
    def copy_inited(self):
        return self.__class__(
            *self.__init_args__,
            **self._kwargs_to_dict()
        )

    #Lets us specify an example for this object
    #Designed for docs
    def example_value(self):
        raise NotImplementedError()