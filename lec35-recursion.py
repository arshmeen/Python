# recursion is function calling itself
# knowing how many times a recursion can be called
import sys

print(sys.getrecursionlimit())

# we can also increase the recursion limit
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())