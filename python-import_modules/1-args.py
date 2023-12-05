from sys import argv

if __name__ == "__main__":
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{}".format("0 arguments."))
    elif arg_len == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{} {}".format(arg_len, "arguments:"))
        for i in range(1, arg_len + 1):
            print("{}: {}".format(i, argv[i]))