from .keywords import (Messgae,MathOperation)
from robotlibcore import DynamicCore

class ActionLibrary(DynamicCore):
    def __init__(self):
        lib=[
            MathOperation(self),
            Messgae(self)
        ]
        DynamicCore.__init__(self,lib)