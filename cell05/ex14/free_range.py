import sys

def free_range(args):
    if len(args) != 2:
        return "none"
    try:
        start = int(args[0])
        end = int(args[1])
    except ValueError:
        return "none"
    return list(range(start, end+1))

def main():
    result = free_range(sys.argv[1:])
    print(result)

if __name__ == "__main__":
    main()
