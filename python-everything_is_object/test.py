for i in range(29):
    with open(str(i) + "-answer.txt", "w") as f:
        f.write("This is answer file number " + str(i))
