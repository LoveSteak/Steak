import inspect
class FuncArgumentTypeError(Exception):
    def __init__(self, funcname,expectedtype,receivedtype):
        message=f'{funcname} expects a {expectedtype} but a {receivedtype} was given.'
        super().__init__(message)