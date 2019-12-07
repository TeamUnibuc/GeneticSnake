import subscripts.GenerateText as GenerateText

_accepted = GenerateText._accepted
_encode = { _accepted[i] : i for i in range(len(_accepted)) }
_decode = { i : _accepted[i] for i in range(len(_accepted)) }

def Encode(s : str):
    return [_encode[i] for i in s]

def Decode(s : list):
    return "".join([_decode[i] for i in s]) 