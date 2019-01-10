def ave(nums):
	for num in nums:
		num = float(num)
	n = len(nums)
	fractop = ''
	for num in nums:
		fractop += str(num) + '+'
	fractop = fractop[:-1]
	tex = '\\frac{' + fractop +'}{' + str(n) + '}  = ' + str(sum(nums)/n)[0:8]
	return tex
