import base64
def base64encode(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def base64decode(s):
    return base64.b64decode(s.encode('utf-8')).decode('utf-8')
