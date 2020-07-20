# We are writing a program that opens up a text file and deletes all of the odd numbers.

file = open("filename.txt", "r")  # Opens file in read mode.

outfile = ""

for line in range(10):
    if line % 2 == 0:
        file.readline()
    else:
        outfile += file.readline()  # Because python starts counting from 0, we end up deleting all of the even numbers!

file = open("filename.txt", "w")
file.write(outfile)
file.close()