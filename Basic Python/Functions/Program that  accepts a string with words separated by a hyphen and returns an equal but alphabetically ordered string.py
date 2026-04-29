def order_string_alphabetically(string):
	words = string.split("-")     
	words.sort()                  
	result = "-".join(words)      
	return result

print(order_string_alphabetically("python-variable-function-computer-monitor"))