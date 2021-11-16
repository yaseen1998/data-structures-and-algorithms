from stack_queue_brackets import __version__
from stack_queue_brackets.stack_queue_brackets import prack

def test_version():
    assert __version__ == '0.1.0'
def test_Square_Brackets():
    actual = True
    exceptValue= prack('()')
    assert actual ==exceptValue

def test_Compine_Brackets():
    actual = True
    exceptValue= prack('{}(){}')
    assert actual ==exceptValue

def test_Compine_BracketsandWord():
    actual = True
    exceptValue= prack('()[[Extra Characters]]')
    assert actual ==exceptValue

def test_Compine_BracketsandWord2():
    actual = True
    exceptValue= prack('{}{Code}[Fellows](())')
    assert actual ==exceptValue

def test_Compine_Brackets2():
    actual = True
    exceptValue= prack('(){}[[]]')
    assert actual ==exceptValue

def test_Compine_Brackets3():
    actual = False
    exceptValue= prack('[({}]')
    assert actual ==exceptValue

def test_Compine_Brackets4():
    actual = False
    exceptValue= prack('(](')
    assert actual ==exceptValue

def test_Compine_Brackets5():
    actual = False
    exceptValue= prack('{(})')
    assert actual ==exceptValue

