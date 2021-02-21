def steak_format(content_to_be_formated,**kwargs):
    for key in kwargs:
        content_to_be_formated=content_to_be_formated.replace(f"<steak>{str(key)}</steak>",str(kwargs[key]))
    return content_to_be_formated