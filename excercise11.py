from sys import argv
script, file_name = argv

txt = open(file_name)

print(f"Here's your file {file_name}.")
print(txt.read())

print("type the filename again")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

