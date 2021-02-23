import steak.core as Core
import inspect

def Validator(objectin,typein):
    if isinstance(objectin,typein):
        return True
    else:
        funcname=inspect.stack()[1][3]
        expectedtype=typein
        receivedtype=type(objectin)
        raise Core.FuncArgumentTypeError(funcname,expectedtype,receivedtype)