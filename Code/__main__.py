

machineLookUp = dict()

file = open("./hubs-case.input", "r")
output = open("./hubs-case.output2", "w")
amountOfLinks = int(file.readline().replace("\n", ""))
m = int(file.readline().replace("\n", ""))



def linkDifference(srcLink):
    l = list()
    for i in range(0, amountOfLinks):
        if i != srcLink:
            l.append(i)
    return l

# Adds a new link to a machine or updates the old one
def updateLink(address, src_link):
    port = machineLookUp.get(address)
    machineLookUp.update({address : src_link})

# Returns an array representation of the links
def get_des_Link(address, src_link):
    port = machineLookUp.get(address)
    if port is None:
        return linkDifference(src_link)
    elif port == src_link:
        return None
    else:
        l = list()
        l.append(port)
        return l

counter = 0
for line in file:
    counter += 1
    if counter > m:
        break

    line = line.split(" ")
    port = int(line[0])
    frame = line[1].replace("\n", "")
    destination = ''.join(frame[0:4])
    src = ''.join(frame[4:8])
    length = int(frame[8], 16) + int(frame[9], 16) + int(frame[10], 16) + int(frame[11], 16)
    payload = ''.join(frame[12:(12+2*length)])
    checksum_given = int(frame[-1:],16)

    updateLink(destination, port)
    links = get_des_Link(src, port)
    if links is not None:
        output_string = frame
        for e in links:
            output_string += " " + str(e)
        output.write(output_string + '\n')
#         write message and append the links

