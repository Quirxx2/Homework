class Sun(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call inst() instead')

    @classmethod
    def inst(cls):
        if cls._instance is None:
            #print('Creating new instance')
            cls._instance = cls.__new__(cls)
            #Put any initialization here
        return cls._instance


p = Sun.inst()
f = Sun.inst()
print(p is f)
#True