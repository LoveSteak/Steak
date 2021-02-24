from .Exceptions import FuncArgumentTypeError
import inspect

def Validator(objectin:object,expectedtype:object)->None:
    '''
    This function should be called inside another function to check if an object matches the expected type
    If not, it raise an FuncArgumentTypeError exception
    '''
    if isinstance(objectin,expectedtype):
        return
    else:
        funcname=inspect.stack()[1][3]
        expectedtype=expectedtype
        receivedtype=type(objectin)
        raise FuncArgumentTypeError(funcname,expectedtype,receivedtype)