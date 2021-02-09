import random
import string

def randstring(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def uniquerandstring(stringwealreadyhave,size=6, chars=string.ascii_uppercase + string.digits):
    s=randstring(size,chars)
    if s in stringwealreadyhave:
        return uniquerandstring(stringwealreadyhave,size,chars)
    return s