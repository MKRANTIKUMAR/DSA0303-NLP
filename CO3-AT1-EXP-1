def parse_tree(words):
    if len(words) != 5:
        return False

    det1, noun1, verb, det2, noun2 = words

    if det1 not in ["the", "a"]:
        return False

    if noun1 not in ["student", "teacher", "book"]:
        return False

    if verb not in ["reads", "likes"]:
        return False

    if det2 not in ["the", "a"]:
        return False

    if noun2 not in ["student", "teacher", "book"]:
        return False

    print("Valid Sentence")
    print("S")
    print("├── NP")
    print("│   ├── Det →", det1)
    print("│   └── N →", noun1)
    print("└── VP")
    print("    ├── V →", verb)
    print("    └── NP")
    print("        ├── Det →", det2)
    print("        └── N →", noun2)

    return True


sentence = input("Enter a sentence: ")
words = sentence.lower().split()

if not parse_tree(words):
    print("Invalid Sentence")
