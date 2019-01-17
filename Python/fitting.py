from math import sqrt

import matplotlib.pyplot as plt
from average import ave

def linear_parameters(xs,ys):
	'''return the parameters [a,b,sigma_a,sigma_b,r],
	 where b is the slope of a linear fitting'''
	n = len(xs)
	xys = [xs[k]*ys[k] for k in range(n)]
	xsqs = [xs[k]**2 for k in range(n)]
	ysqs = [ys[k]**2 for k in range(n)]
	#calculate average values
	xbar = sum(xs)/n
	ybar = sum(ys)/n
	xybar = sum(xys)/n
	xsqbar = sum(xsqs)/n
	ysqbar = sum(ysqs)/n
	
	b = (xbar*ybar - xybar)/(xbar**2 - xsqbar)
	a = ybar - b*xbar
	#calculate errors of a b
	es = [(ys[k] - (b*xs[k] + a)) for k in range(n)]
	esqs = [es[k]**2 for k in range(n)]
	sigma_y = sqrt(sum(esqs)/(n-2))
	sigma_b = sigma_y/(sqrt(n*(xsqbar - xbar**2)))
	sigma_a = sigma_b*sqrt(xsqbar)
	
	r = (xybar - xbar*ybar)/(sqrt(xsqbar - xbar**2)*sqrt(ysqbar - ybar**2))
	
	return [a,b,sigma_a,sigma_b,r]


def linear_eq(xs,ys):
	'''return the LaTeX eqs. of calculate parameters'''
	n = len(xs)
	xbar = sum(xs)/n
	ybar = sum(ys)/n
	xbar = str(xbar)
	ybar = str(ybar)
	b_up = ''
	for k in range(n):
		b_up += '(' + str(xs[k]) + '-' + xbar + ')(' + str(ys[k]) + '-' + ybar + ')'
	for k in range(n):
		b_down += '(' + str(xs[k]) + '-' + xbar + ')^2'
	#eqs for a and b	
	b_eq = '\\frac{' + b_up + '}{' + b_down + '}'
	a_eq = ybar + '-' + str(linear_parameters[1]) +'\\times' + xbar
	
	sigma_y_under = '('
	for k in range(n):
		sigma_y_under += '[' + str(ys[k]) + '-(' + str(linear_parameters[1]) + '+' + str(linear_parameters[0]) +')]^2 +'
	sigma_y_under = sigma_y_under[:-1]
	sigma_y_under += ']'
	#eq for sigma_y
	sigma_y_eq = '\\sqrt{\\frac{1}{' + str(n) + '-2}' + sigma_y_under + '}'
	
		
		
	
	
	
	
	
	
