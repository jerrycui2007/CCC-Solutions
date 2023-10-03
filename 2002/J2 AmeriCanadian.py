# https://dmoj.ca/problem/ccc02j2
while True:
    word = input()
    if word == "quit!":
        break
    else:
        if len(word) >= 4:
            if word[-2] + word[-1] == "or":
                if word[-3] not in "aeiouy":  # is a consonant
                    word = word.replace("or", "our")
        print(word)