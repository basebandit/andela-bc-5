def words(string):
    string = string.replace('\t', ' ').split()
    my_dict = {}

    for word in string:
        if not my_dict.get(word):
            try:
                my_dict[int(word)] = string.count(word)
            except:
                my_dict[word] = string.count(word)

    return my_dict

print words("one of each")
