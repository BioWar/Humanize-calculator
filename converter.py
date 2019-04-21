import inflect
import pandas as pd
import sys
import pytest

def convert(string):	
	p = inflect.engine()
	sign = pd.read_csv('sign.csv', index_col=0)
	string = string.strip()
	string = string.split()
	string = ''.join(string)
	sep = []
	value = ''
	for i in string:
		if i.isdigit():
			value += i
		else:
			sep.append(value)
			sep.append(i)
			value = ''
	sep.append(value)
	sep = [i for i in sep if len(i) != 0]
	result = []
	for i in sep :
		if i.isdigit():
			result.append(p.number_to_words(i))
		elif i in sign.index:
			result.append(sign.loc[i, '1'])
		else:
			return 'Invalid input.'
	result = ' '.join(result)
	return result

def test_1():
	string =  '33+11 = 4 4'
	answer = 'thirty-three plus eleven equals forty-four'
	assert convert(string)==answer, "test failed"

def test_2():
	string =  '33+11  - 13 * 4 =  - 8'
	answer = 'thirty-three plus eleven minus thirteen multiplied by four equals minus eight'
	assert convert(string)==answer, "test failed"
	
def test_3():
	string = '1234/2+0=            7'
	answer = 'one thousand, two hundred and thirty-four divided by two plus zero equals seven'
	assert convert(string)==answer, "test failed"
	
def test_4():
	string = '1*1+1/1-2=0'
	answer = 'one multiplied by one plus one divided by one minus two equals zero'
	assert convert(string)==answer, "test failed"
	
def test_5():
	string = '1*1+1/1-2=0 dddddd'
	answer = 'Invalid input.'
	assert convert(string)==answer, "test failed"

if __name__=='__main__':
	if len(sys.argv) > 1:
		args = sys.argv
		print(convert(args[1]))
	else:
		string = 'YOUR STRING HERE.'
		print(convert(string))
