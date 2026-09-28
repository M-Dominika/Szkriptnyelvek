s="""Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""
for i in s:
    if 'a' <= i <= 'z':
        if chr(ord(i)+2)>'z':
            print(chr(ord(i) + 2-26), end="")
        else:
            print(chr(ord(i)+2), end="")
    elif 'A'<=i<='Z':
        if chr(ord(i) + 2) > 'Z':
            print(chr(ord(i)+2-26), end="")
        else:
            print(chr(ord(i)+2), end="")
    else:
        print(i, end="")
