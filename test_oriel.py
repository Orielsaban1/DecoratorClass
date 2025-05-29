from oriel_decorator import OrielClassDecorator
import os

@OrielClassDecorator
def test_oriel():
    assert os.path.isdir("oriel") == True
    assert os.path.isdir("oriel/oriel") == False
#oriel