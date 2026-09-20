#!/usr/bin/env python3

def main(szam):
    n=str(szam)
    return(int(n[::-1]))

if __name__=="__main__":
    szam=int(input())
    print(main(szam))
