# with open("file_question.txt") as in_file:
#     text = in_file.read()
#     text_test = text.strip()
# print(text_test)

with open("file_question.txt") as in_file:
    for line in in_file:
        # print(line)
        parts = line.strip().split(",")
        # print(parts)
        name = parts[0].strip()
        year = parts[1].strip()
        price = parts[2].strip()
        print(f"{name} {year} {price[0: -2]}")


# FILENAME = "file_question.txt"

# in_file = open(FILENAME)
# for line in in_file:
#     print(line)
# in_file.close()

# text = in_file.read()
# in_file.close()
# print(text)
