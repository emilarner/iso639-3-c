import os
import sys

def printnl(text: str):
    sys.stdout.write(text)


line_count = 0
with open("iso639-3.txt", "r") as fp:
    line_count = len(fp.readlines()) - 1


already_seen = set()

printnl(f"const char *iso639_3_ents[{line_count}] = " + "{")

with open("iso639-3.txt", "r") as fp:
    for line in enumerate(fp.readlines()):
        if (line[0] == 0):
            continue

        tokens = line[1].split("\t")

        if (tokens[0] not in already_seen):
            printnl(f"\"{tokens[0]}\",")
        
        already_seen.add(tokens[0])

printnl("\n };")

printnl(f"const char *iso639_3_fullnames[{line_count}] = " + " {")

already_seen.clear()
with open("iso639-3.txt", "r") as fp:
    for line in enumerate(fp.readlines()):
        if (line[0] == 0):
            continue

        tokens = line[1].split("\t")
        
        if (tokens[0] not in already_seen):
            printnl(f"\"{tokens[1]}\",")

        already_seen.add(tokens[0])

printnl("\n };")

printnl(f"\n\nconst int iso639_3_len = {line_count};")

printnl("enum iso639_3_enum {\n")
already_seen.clear()
with open("iso639-3.txt", "r") as fp:
    for line in enumerate(fp.readlines()):
        if (line[0] == 0):
            continue

        tokens = line[1].split("\t")
        if (tokens[0] not in already_seen):
            printnl(f"ISO639_3_E_{tokens[0].upper()},")

        already_seen.add(tokens[0])

printnl("\n};")
