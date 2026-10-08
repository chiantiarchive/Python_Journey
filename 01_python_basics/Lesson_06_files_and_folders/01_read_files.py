

#   Does not work because it has no path from this folder
f = open("sample.txt", "r", encoding="utf-8")
content = f.read()
f.close

print(content)


#
#
#


#     What’s different and why?
#     with open(...) as f: creates a context manager.
#     Python automatically closes the file when the block ends, even if an error occurs.
#     This is safer and is the standard professional style.

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.close

print(content)


#
#
#


#   Reading file line by line
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        #   Each line includes the newest character "\n"
        print(line.strip()) #   srtip() removes leading/trailing whitespaces