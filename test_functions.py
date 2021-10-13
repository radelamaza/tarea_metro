import functions
import main
muestra = {'lineas': [['A', 'B', 'C'], ['C', 'G', 'H', 'I', 'F'], [
    'C', 'D', 'E', 'F']], 'rojo': ['H'], 'verde': ['G', 'I']}


def test_input():
    data = functions.get_data(["main.py", "test.json", "A", "B", "rojo"])
    assert data == muestra


def test_forward():
    step = functions.forward(1, 0, ['C', 'G', 'H', 'I', 'F'], ['F', 'I', 'G', 'C'], muestra, [['A', 'B', 'C'], [
                             'C', 'G', 'H', 'I', 'F'], ['C', 'D', 'E', 'F']], 'F', 'A', 'verde', 3, 1000000, ['F', 'I', 'G', 'C', 'B', 'A'])
    assert step == ['F', 'I', 'G', 'C', 'B', 'A']


def test_backward():
    step = functions.backward(1, 4, ['C', 'G', 'H', 'I', 'F'], ['F'], muestra, [['A', 'B', 'C'], [
                              'C', 'G', 'H', 'I', 'F'], ['C', 'D', 'E', 'F']], 'F', 'A', 'verde', 0, 1000000, False)
    assert step == ['F', 'I', 'G', 'C', 'B', 'A']


def test_compare_results1():
    compare = functions.compare_results(
        ['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'H', 'F'])
    assert compare == ['A', 'B', 'C', 'H', 'F']


def test_compare_results2():
    compare = functions.compare_results(['A', 'B', 'C', 'H', 'F'], [
                                        'A', 'B', 'C', 'D', 'E', 'F'])
    assert compare == ['A', 'B', 'C', 'H', 'F']


def test_main():
    optimum = main.main(muestra, 'A', 'F', False)
    assert optimum == ['A', 'B', 'C', 'D', 'E', 'F']


def test_main_color():
    optimum = main.main(muestra, 'A', 'F', "rojo")
    assert optimum == ['A', 'B', 'C', 'H', 'F']
