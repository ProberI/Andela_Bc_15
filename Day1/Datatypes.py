# Author Paul Upendo


def data_type(v):
    if type(v) == int:
        if v > 100:
            return 'more than 100'
        elif v < 100:
            return 'less than 100'
        elif v == 100:
            return 'equal to 100'

    elif type(v) == str:
        return len(v)

    elif type(v) == bool:
        return (v)

    elif type(v) == list:
        if len(v) < 3:
            return None
        else:
            return v[2]

    elif v is None:
        return 'no value'

