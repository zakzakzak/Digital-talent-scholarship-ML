# membuat dan menulis file
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt', 'w') as writefile:
    writefile.write("This is line A")
print("-------------\n")

# to see if it worked
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
print("-------------\n")

# menghapus yg sebelumnya, membuat yg baru
# jika dalam satu with, maka dianggap tambah (append)
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
print("-------------\n")

# Berfungsi sebagai append 'a', sehingga tidak ditulis ulang
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt', 'a') as testwritefile:
    for i in range (4) :
        testwritefile.write("This is line C\n")
print("-------------\n")


# isi dengan array
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
print("-------------\n")

# append line
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")
print("-------------\n")

# COPY FILE
with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example2.txt','r') as readfile:
    with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
print("-------------\n")




# --------------------------BUAT TRANSLATE TXT KE PNG---------------------------------------
# with open('D:/boku no projecto/python/dts/Sesi3_file_tools/Example3.txt','r') as readfile:
#     with open('D:/boku no projecto/python/dts/Sesi3_file_tools/bbb.png','w') as writefile:
#           for line in readfile:
#                 writefile.write(line)
# print("-------------\n")
# --------------------------BUAT TRANSLATE TXT KE PNG---------------------------------------
