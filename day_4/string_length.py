def string_length(string):
	list_ = list()
	count = 0
	for items in string:
		if isinstance(items,str):
			
			return [len(str(items))]
		else:
			while count < len(string):
				list_.append(len(string[count]))
				count += 1
			
			

print string_length(['Adam','mwass'])