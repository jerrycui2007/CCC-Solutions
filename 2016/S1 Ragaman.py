# https://dmoj.ca/problem/ccc16s1
original_string = input()
anagram_string = input()

original_letter_count = {}
anagram_letter_count = {}

is_wild_card = True

# Count the appearances of each letter, and it is a wild-card anagram if the original has equal or greater appearances
# each letter
for character in original_string:
    if character in original_letter_count:
        original_letter_count[character] += 1
        anagram_letter_count[character] = 0  # initialize the second dictionary at the same time
    else:
        original_letter_count[character] = 1
        anagram_letter_count[character] = 0  # initialize the second dictionary at the same time

for character in anagram_string:
    if character != "*":
        try:
            anagram_letter_count[character] += 1
        except KeyError:
            is_wild_card = False  # there is a letter in anagram that doesn't appear in original

for character in original_letter_count:
    if original_letter_count[character] < anagram_letter_count[character]:
        is_wild_card = False

if is_wild_card:
    print("A")
else:
    print("N")
