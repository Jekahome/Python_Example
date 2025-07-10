#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from base import add,input_exam
from base_types.types import types_add

def main():
    result = add(2, 3);
    print("Result: ", result);
    print("Result: ", types_add(2,3));    

if __name__ == "__main__":
    # Production:
    main()

    # Run Unit Tests:
    testsuite = unittest.TestLoader().discover(".")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
