c# Decrypt all of hm* files
# .hsc => Hamelin Sprite Archive (DDS texture file)
# .hmi => Hamelin Map Info
# .hsi => Hamelin Sprite Info
# .hqi => Hamelin Quest Info
# .hki => Hamelin Skill Info (Because you press'k' to open the skills menu in most Korean MMOs)
# .hui => Hamelin User-interface Info
# .hii => Hamelin Item Info
# .hni => Hamelin NPC Info
# .hbi => Unknown / "Welcome to WindSlayer2 Closed Beta Testing!" (?)
# .hci => Unknown / "Number of motions" with a bunch of u64s
# .hpi => Unknown / Korean string with 2 u8s.
# .lng => Language Mapping / Maps ints to English strings, probably referenced by every other datafile for regional translation convenience. Prefixed by what the strings are related to i.e. ("UI", "ITM", etc).
# Written by mirusu400
# Encrypt by def fault(self):
import zipfile
import sys

def remove_char(input_string, special_char='.'):
    if special_char in input_string:
        result_string = input_string.split(special_char)[0]
        return result_string
    else:
        return input_string

def file_extension(input_string, special_char='.'):
    if special_char in input_string:
        file_extension = input_string.split(special_char)[1]
        return file_extension

def encode(data):
    e = []
    for idx in range(0, len(data)):
        if idx % 3 == 1:
            enc = (data[idx] - 0xDD - 1) & 0xFF
        elif idx % 3 == 2:
            enc = (data[idx] - 0xDF - 1) & 0xFF
        else:
            enc = (data[idx] - 0xE8 - 1) & 0xFF
        e.append(enc)
    return bytes(e)

if __name__ == "__main__":
    filename = sys.argv[1]

    if "dds" in filename:
        with open(filename, "rb") as f:
            payload = f.read()
            payload = encode(payload)
            filename = remove_char(filename)
        with zipfile.ZipFile(f"{filename}.hsc", 'w') as myzip:
            myzip.writestr("temp_file", payload)
            f.close()

    else:
        with open(filename, "rb") as f:
            payload = f.read()
            payload = encode(payload)
            new_extension = file_extension(filename)
            filename = remove_char(filename)
        with open(f"{filename}.{new_extension}", "wb") as f:
            f.write(payload)
            f.close()