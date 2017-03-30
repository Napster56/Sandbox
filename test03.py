books = []

in_file = open("books.csv", "r")
for record in in_file:
    new_line = record.strip("\n").split(",")
    books.append(new_line)
in_file.close()
print(books)



out_file = open("books.csv", "w")
for record in books:
    for str_record in record:
        str_record = " ".join(record)
        str_record += "\n"
    out_file.write(str_record)
    print(str_record)
out_file.close()
