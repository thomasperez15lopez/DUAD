def flip_string(text):
	reversed_text = ""
	for letter in text:
		reversed_text = letter + reversed_text
	return reversed_text


result = flip_string("Hello world")
print(result)

print(flip_string("Hello world"))