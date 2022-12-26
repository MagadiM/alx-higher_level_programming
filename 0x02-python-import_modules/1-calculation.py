#usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a, b = 10, 5
    /*addition*/
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    /*subtraction*/
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    /*mul*/
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    /*div*/
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
