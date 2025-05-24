class Singleton:
    """
    A base class that can be used to implement the Singleton pattern.

    To make a class a Singleton, inherit from this class.
    The first time the class is instantiated, it will create a single instance.
    Subsequent attempts to instantiate the class will return the same instance.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    
    def __init__(self, value):
        if not hasattr(self, 'value'):
            self.value = value