from math import sqrt

def std(nums,accurancy=5):
	'''
	nums: array of data
	
	accurancy: 精度, 默认五位有效数字
	'''
	for num in nums:
		num = float(num)
	n = len(nums)
	a = sum(nums)/n
	s = 0
	for num in nums:
		s += (num - a)**2
	dev = sqrt(s/(n*(n-1)))		
	a = str(a)
	a = a[0:accurancy]
	undersqrt = ''
	for num in nums:
		undersqrt += '(' + str(num)[0:accurancy] + '-' + a + ')^2 +'
	undersqrt = undersqrt[:-1]
	tex = '\\frac{1}{\\sqrt{' + str(n) + '}} \\sqrt{\\frac{1}{' + str(n) + '-1}[' + undersqrt +']}'
	tex += (' = ' + str(dev)[0:4])
	return tex

