def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

a="Hi I am superman"
print(reverse(a))
