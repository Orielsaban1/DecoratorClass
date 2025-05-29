from types import FunctionType

import mock
from functools import update_wrapper
def mock_os_isdir(path):
    print("oriel_bla_bla")
    if path == "oriel/oriel":
        return False
    return True

class OrielClassDecorator:
    def __init__(self, func: FunctionType):
        self.func = func
        update_wrapper(self, func)
        #oriel
    @mock.patch("os.isdir",mock_os_isdir)
    def __call__(self, *args, **kwargs) -> FunctionType:
        return self.func(*args, **kwargs)