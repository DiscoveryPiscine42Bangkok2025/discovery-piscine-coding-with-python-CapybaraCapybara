import sys

a = sys.argv

if len(a) >= 2:
    for i in a[1:]:
        if not i.endswith("ism"):
            print(i+"ism")
else:
    print("None")