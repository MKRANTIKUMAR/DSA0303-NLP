def check_agreement(subject, verb):
    subject_features = {
        "he": "singular",
        "she": "singular",
        "it": "singular",
        "they": "plural"
    }

    verb_features = {
        "runs": "singular",
        "writes": "singular",
        "run": "plural",
        "write": "plural"
    }

    if subject in subject_features and verb in verb_features:
        return subject_features[subject] == verb_features[verb]

    return False


subject = input("Enter subject: ")
verb = input("Enter verb: ")

print(check_agreement(subject, verb))
