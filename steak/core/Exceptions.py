import inspect
from .Logger import Logger
class FuncArgumentTypeError(Exception):
    '''
    Exception class whose objects to be raised when a type of a variable passed to a function does not match our expectation
    '''
    def __init__(self, funcname,expectedtype,receivedtype):
        message=f'{funcname} expects a {expectedtype} but a {receivedtype} was given.'
        logger = Logger(logger="Exceptions.py")
        logger.critical(message)
        super().__init__(message)
