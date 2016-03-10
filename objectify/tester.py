import inspect, _ast


"""
    In future this may let us copy ONLY the params
    that are actually initialized in a classes constructor
    when copying a class via copy_inited

    This would save memory as we wouldnt need the 4 tuple
    solution currently used

    HOWEVER cpu performance here is really unknown, so more
    time is needed to evaluate if this is necessary


    Other considerations exist to. At time of writing, elimiting 
    the tuples only saves 36mb, cutting 10000 blankly initialized
    objects to 30mb from 66mb

    BUT that 66mb is almost enitely tuples (70%)

    Right now with objects being filled out, we see something like this (for 10000 objects)

    Partition of a set of 680102 objects. Total size = 104982648 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0 420034  62 43203416  41  43203416  41 tuple
         1  10001   1 10480280  10  53683696  51 dict of 0x7fed01717cf0
         2  10000   1 10480000  10  64163696  61 dict of 0x7fed0174ed80
         3  40003   6  9600720   9  73764416  70 objectify.prop.string.TrimmedUnicode
         4  30001   4  7200240   7  80964656  77 objectify.dynamic.DynamicProperty
         5  40000   6  3840000   4  84804656  81 unicode
         6  10010   1  2805872   3  87610528  83 dict (no owner)
         7  10001   1  2720272   3  90330800  86 objectify.prop.timestamp.SmartTimestamp
         8  10001   1  2560256   2  92891056  88 __main__.DecimalLatitude
         9  10001   1  2400240   2  95291296  91 objectify.prop.boolean.Boolean
    <23 more rows. Type e.g. '_.more' to view.>


"""

def _class_assignments(statement,assigments=[]):

class Autoslots_meta(type):
    """
    Looks for assignments in __init__
    and creates a __slot__ variable for all the
    instance attributes in the assignment.
    Assumes that all assignments in __init__ are of
    the form:
        self.attr = <value>
    """

    def _test(cls):
        
        if '__init__' in cls.__dict__:
            init = cls.__dict__['__init__']
            
            initproc_source = inspect.getsource(cls)
            
            ast = compile(initproc_source, "dont_care", 'exec', _ast.PyCF_ONLY_AST)
            classdef = ast.body[0]
            stmts = classdef.body
            for declaration in stmts:
                if isinstance(declaration, _ast.FunctionDef):
                    if declaration.name == '__init__':
                        initbody = declaration.body
                        print initbody
                        for statement in initbody:
                            if isinstance(statement, _ast.Assign):
                                for target in statement.targets:
                                    if isinstance(target,_ast.Attribute):
                                        print target.__dict__
                            if isinstance(statement, _ast.If):
                                print statement.__dict__
                                    #name1 = target.attr
                                    #if name1 not in orig_slots:
                                    #    slots.append(name1)
                #if slots:
                #    dct['__slots__'] = slots
                #print slots
        #return type.__new__(cls, name, bases, dct)
        #return super(Autoslots_meta, cls).__new__(cls, name, bases, dct)