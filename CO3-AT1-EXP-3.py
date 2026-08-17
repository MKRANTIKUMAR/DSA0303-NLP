def sentence_probability(sentence):
    words = sentence.split()

    if len(words) != 2:
        return 0

    subject, verb = words

    np = {
        "John": 0.6,
        "Mary": 0.4
    }

    vp = {
        "runs": 0.5,
        "walks": 0.5
    }

    if subject in np and verb in vp:
        return 1.0 * np[subject] * vp[verb]

    return 0


sentence = input("Enter sentence: ")
print(sentence_probability(sentence))
