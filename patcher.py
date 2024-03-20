import sys
if __name__ == '__main__':
    file = ""
    if len(sys.argv) != 2:
        print("Drag and Drop WindSlayer.exe file here.")
        file = input()
    else:
        file = sys.argv[1]

    a = input("Put your ip!")

    with open(file, "rb") as f:
        data = bytearray(f.read())
        data[0xA49b8] = 0x74
        print("doing...0")

        for i in range(0x1C):
            if i > len(a)-1:
                data[0x155340+i] = 0x00
                print("doing...1")
            else:
                data[0x155340+i] = ord(a[i])
                print("doing...2")

        with open("WindSlayer_out.exe", "wb") as f:
            f.write(data)
            f.close()

    input("Done! Take Windslayer_out.exe file.")