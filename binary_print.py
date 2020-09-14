def bin_print(num=0):
	if num < 0:
		return None
	octet = ""
	ans = ""
	print(str(num), end='\t')
	while num or ans == "":
		octet = ("1" if num & 1 else "0") + octet
		num = num >> 1
		if num == 0:
			octet = ((8 - len(octet)) * "0") + octet
		if len(octet) == 8:
			ans = octet + " " + ans
			octet = ""
	print(ans)



# Tests

# Bad
bin_print(0)
bin_print(-10)

# Good
bin_print(1)
bin_print(2)
bin_print(4)
bin_print(11)
bin_print(1024 * 256 + 53426)
bin_print(1024 * 256 + 53427)
bin_print(1024 * 256)
bin_print(1024 * 256 * 2)
for i in range(64):
	bin_print(2 ** i)
