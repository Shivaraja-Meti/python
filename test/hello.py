# hello.py
import sys
sys.path.append("../test2")   # add test2 folder to Python path

import hello1

print("Hello from hello.py!")
hello1.greet()
