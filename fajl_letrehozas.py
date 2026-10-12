def main():
    print("---------------------------\nCreate an empty source file\n---------------------------\n1) Python [py]\n2) Java   [java]\nq) quit")
    v=input("> ")
    if v=="1":
        try:
            with open("alap.py", "x") as f:
                f.write("#!/usr/bin/env python3\n\ndef main():\n\tprint('Py3')\n\n##############################################################################\n\nif __name__ == \"__main__\":\n\tmain()")
        except(FileExistsError):
            print("File már létezik")
    elif v=="2":
        try:
            with open("alap.java", "x") as f:
                f.write("public class alap {\n\tstatic void main() {\n\t\tSystem.out.println(\"Hello world\");\n\t}\n}")
        except(FileExistsError):
            print("File már létezik")
    else:
        return 0

if __name__ == "__main__":
    main()
