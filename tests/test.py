import c_cpp_py as cp

def test_main():
    assert cp.__version__ == "0.0.1"
    assert cp.add(1, 2) == 3
    assert cp.subtract(1, 2) == -1