def hangrend(szo):
    mely = False
    magas = False
    for i in szo:
        if i in 'aáoóuú':
            mely = True
        if i in 'eéiíöőüű':
            magas = True
    if mely and magas:
        return "Vegyes"
    if mely:
        return "Mély"
    if magas:
        return "Magas"
    return "Semmilyen"

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for i in words:
        print(i, "-", hangrend(i))

if __name__ == '__main__':
    main()
