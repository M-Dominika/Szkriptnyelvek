#!/usr/bin/env python3

def main(szo):
    if  szo==szo[::-1]:
        return "palindróm"
    else:
        return "nem palindróm"

if __name__=="__main__":
    szo=input()
    print(main(szo))
