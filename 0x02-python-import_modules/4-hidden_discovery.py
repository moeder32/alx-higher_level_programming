#!/usr/bin/python3

if __name__ == "__main__":
    """Program that prints all of  names defined by a compiled module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print("{}".format(name))
