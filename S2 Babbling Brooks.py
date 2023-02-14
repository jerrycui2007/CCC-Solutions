n = int(input())
streams = []

for _ in range(n):
    streams.append(int(input()))

instruction = 0

while True:
    instruction = int(input())

    if instruction == 77:
        break
    elif instruction == 99:  # split
        stream_to_split = int(input())
        percentage_split = int(input())

        streams.insert(stream_to_split, streams[stream_to_split - 1] * (1 - (percentage_split / 100)))
        streams[stream_to_split - 1] *= percentage_split / 100
    elif instruction == 88:  # join
        stream_to_join = int(input())
        streams[stream_to_join - 1] += streams[stream_to_join]
        streams.pop(stream_to_join)

output = ""
for length in streams:
    output += str(round(length)) + " "

print(output[:-1])
