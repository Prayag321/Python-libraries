# s1t4p2
# sttttpp
def genereate_alpha(alpha,count):
  string = ""
  count = int(count)
  for i in range(count):
    string +=alpha
    
  return string

def generate_string(string):
  letter=""
  new_string = ""
  for i in string:
    if i.isalpha():
      letter=i
      new_string += genereate_alpha(letter,string[string.find(i)+1])
    
  print(new_string)



string = "s1t4p2"
generate_string(string)
