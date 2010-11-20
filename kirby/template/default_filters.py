from time import strftime

filters = {}

def register(fn):
    filters[fn.__name__] = fn
    return fn


@register
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    try:
        return value.strftime(format)
    except:
        return value