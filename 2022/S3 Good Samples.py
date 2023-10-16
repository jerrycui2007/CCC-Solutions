# https://dmoj.ca/problem/ccc22s3
notes, maximum_pitch, number_of_good_samples = list(map(int, input().split()))

song = []
for i in range(notes):
    remainder = notes - i - 1

    samples_created = min(number_of_good_samples - remainder, maximum_pitch)
    if samples_created <=0:
        break

    if samples_created > i:
        new_note = min(maximum_pitch, i + 1)
        samples_created = new_note
    else:
        new_note = song[i - samples_created]

    song.append(new_note)
    number_of_good_samples -= samples_created  # decreases until we have created enough samples

if number_of_good_samples == 0 and len(song) == notes:
    final_song = ""
    for note in song:
        final_song += str(note) + " "
    print(final_song[:-1])
else:
    print(-1)