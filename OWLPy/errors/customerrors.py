# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class NotFound(Error):
   """Raised when the input value is too small"""
   pass
class PlayerNotFound(NotFound):
   """Raised when the input value is too large"""
   pass