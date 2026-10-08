

message = "This is a line written by Python.\n"

with open("output/test_writer.txt", "w", encoding="utf-8") as f:
    
    f.write(message)
    f.write("Second line.\n")


#   "w" mode means write:
#   If the file doesn’t exist, it’s created.
#   If it exists, it’s overwritten.
#   f.write(...) writes a string to the file.
#   You must include \n yourself if you want new lines.

#
#


with open("output/test_write.txt", "a", encoding="utf-8") as f:
    f.write("This line is appended.\n")

#   "a" means append: new data is added to the end.