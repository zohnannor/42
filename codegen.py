import re
import tokenize

with open("template.txt", "r") as f:
    template = f.read()

with open("prog.c", "r") as f:
    tokens = tokenize.generate_tokens(f.readline)

    source = []
    for token in tokens:
        source.append(token.string)


def repl(m):
    res = []

    while len("".join(res)) < len(m.group()):
        token = source.pop(0)
        res.append(token)

    if len("".join(res)) > len(m.group()):
        last_token = res.pop()
        source.insert(0, last_token)
        res.insert(-1, " ")

    return "".join(res)


code = re.sub("#+", repl, template).replace(".", " ")
#                                  This is because in the "prog.c",
#                                  spaces replaced with dots.

with open("42.c", "w") as f:
    f.write(code)
