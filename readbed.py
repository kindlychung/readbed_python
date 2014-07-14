#!/usr/bin/python3

def bitsToNum(x):
    if x == "00":
        return 2
    elif x == "01":
        return -9
    elif x == "10":
        return 1
    elif x == "11":
        return 0
    else:
        raise Exception("Unknown bits code!")

def byteToNum(xbyte):
    x = "{:08b}".format(xbyte)
    xstring = [x[i:i+2] for i in range(0, len(x), 2)]
    xgen = [str(bitsToNum(i)) for i in xstring]
    xgen.reverse()
    xgenstring = """std::vector<int> """ + "{" + ", ".join(xgen) + "}"
    return xgenstring


# print out c++ code for inclusion in a header file
print("""const std::vector< std::vector<int> > gencodes {""")
for i in range(256):
    # print("{0:08b}".format(i))
    print("    ", end="")
    print(byteToNum(i), end="")
    if i != 255:
        print(",")
    else:
        print("")

print("};")
