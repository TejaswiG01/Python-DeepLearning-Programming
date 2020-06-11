# opening the file in read mode
file = open("pyfile.txt", "r")
count = dict()

# counting the word frequency and storing in count
for line in file:
    line = line.strip()
    words = line.split(" ")
    # iterate over each word in line
    for i in words:
        if i in count:
            # increment the count
            count[i] = count[i] + 1
        else:
            # add the word to count
            count[i] = 1

# print contents of dictionary
for key in list(count.keys()):
    print(key, ":", count[key])
