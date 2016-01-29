def reverse_string(string):
  if string:
    strs=''
    length = len(string)
    while length > 0:
        strs+=string[length-1]
        length -= 1
    return strs
    
  else:
    return None

print(reverse_string("sillywewe"))