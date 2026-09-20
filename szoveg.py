#!/usr/bin/env python3


def main():
    emberek = [
        ('Anna', 2001, 165, 55),
        ('Béla', 2003, 167, 65),
        ('Szabolcs', 2005, 172, 75),
        ('Kata', 2004, 155, 50),
    ]
    print("="*68)
    print("| {0:<10} | {1:^19} | {2:^15} | {3:^11} |".format("Név", "Születési év", "Magasság", "Súly"))
    print("="*68)
    for ember in emberek:
        print("| {0:10} | {1:^19} | {2:^15} | {3:^11} |".format(ember[0], ember[1], str(ember[2])+" cm", str(ember[3])+" kg"))
    print("="*68)


if __name__=="__main__":
    main()
