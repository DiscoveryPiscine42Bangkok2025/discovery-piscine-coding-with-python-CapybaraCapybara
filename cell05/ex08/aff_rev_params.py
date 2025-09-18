import sys
a = sys.argv
if len(sys.argv) > 2:
    for i in reversed(a):
        print(i)
else:
    print("None")
    