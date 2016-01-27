def output(name,**kwargs):
	print 'name: ',name
	for i in kwargs.keys():
		print i, ": ",kwargs[i]


output('Angela',age=19,gender='F',loc='NRB')

def my_sum(*args):
	total = 0
	for i in args:
		total += i

	return total

print "My Sum: ",my_sum(10,20)
print "My Sum: ",my_sum(10,30,40,50,67,80)