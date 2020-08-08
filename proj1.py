from __future__ import print_function
# read file
example1 = "D:/boku no projecto/python/dts/Sesi3_file_tools/example1.txt"
file1 = open(example1, "r")
print("-------------")

# print name(path)
print(file1.name)
print("-------------\n")

# print mode
print(file1.mode)
print("-------------\n")

# print isi file
FileContent = file1.read()
print(FileContent)
print("-------------\n")

# print type
print(type(FileContent))
print("-------------\n")


# close file : gak bisa melakukan operasional lagi
file1.close()
# print(file1.read())

# cara terbaik : close otomatis
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
print("-------------\n")

# cek jika sudah close
print(file1.closed)
print("-------------\n")

# read only 4 first character
# and then next 7 char and next 15 char
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
print("-------------\n")

# print per line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())
    print("first line: " + file1.readline())
print("-------------\n")

# print per line semua
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;
print("-------------\n")

# print per line
with open(example1, "r") as file1:
    FileasList = file1.readlines()
    print(FileasList[0])
    print(FileasList[1])
print("-------------\n")
