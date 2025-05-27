# to create and write into file
with open("sample.txt", "w") as f:
    f.write("This is Vineela \n")

#to append
with open("sample.txt", "a") as f:
    f.write("From ECE Branch.\n")

# read content from starting
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

#append and read together
with open("sample.txt", "a+") as f:
    f.write("My hobby is drawing.\n")
    f.seek(0) 
    print("\nReading content after appending and reading together:")
    print(f.read())