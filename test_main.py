import main

def test_add():
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_add()
