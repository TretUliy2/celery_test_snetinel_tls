#!/usr/bin/env python3 
from tasks import add
import time 

if __name__ == '__main__':
    result = add.delay(4, 4)
    print(f"{result=} {type(result)=}")
    print(result)
