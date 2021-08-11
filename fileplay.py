def count_string_length(string):
  return len(string)

def reverse_string(string):
  return string[::-1]

def change_file(filename, to_changed):
  working_file = open(filename, "r")
  all_lines = working_file.readlines()

  for index in range(len(all_lines)):
    if all_lines[index] == to_changed:
      all_lines[index] = "CHANGED!\n"

  
  working_file = open(filename, "w")
  working_file.writelines(all_lines)
  working_file.close()


if __name__ == "__main__":
  print(count_string_length("Ekrem"))
  print(reverse_string("Ekrem"))
  change_file("testfile.txt", "CHANGE THIS LINE\n")