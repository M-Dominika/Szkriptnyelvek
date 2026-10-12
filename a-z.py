import sys

def main():
    """Ha a fájl neve a-z.py, visszaadja az abc betűit a-tól z-ig, ha viszont z-a.py akkor z-től a-ig adja vissza"""
    fajl_neve=sys.argv[0]
    if fajl_neve.endswith("a-z.py"):
        for i in range(ord('a'), ord('z')+1):
            print(chr(i), end="")
    elif fajl_neve.endswith("z-a.py"):
        for i in range(ord('z'), ord('a')-1, -1):
            print(chr(i), end="")


if __name__ == "__main__":
    main()
