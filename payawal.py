##!/usr/bin/python
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

###################
# 1. NUM TO WORDS #
###################
def numToWords(num):											#for recursive purposes
	return numToWordsFxn(str(num), "")

def numToWordsFxn(num, word):
	if len(num) == 1:											#gets the word form of the ones digit of the number			
		word += search(int(num), ones)
		return word

	if len(num) == 2:											
		if num[0] == '1':
			word += search(int(num)-10, teens)					#subtract ten to properly traverse the teens array
			return word
		else:
			word += search(int(num[0]), tens) + " "				#gets the word form of the tens digit of the number	
			return numToWordsFxn(num[1:], word)						#pass the remaining substring of num

	if len(num) == 3 or len(num) == 6:							#for hundred and hundred thousand input
		word += search(int(num[0]), ones) + " hundred " 		#gets the word form of the digit and append the word hundred
		return numToWordsFxn(num[1:], word)							#pass the remaining substring of num

	if len(num) == 4:											#for thousand input
		word += search(int(num[0]), ones) + "thousand "			#gets the word form of the digit and append the word thousand
		if int(num[1:]) != 0:									#if the remaining numbers are not yet 0, recursive call
			return numToWordsFxn(num[1:], word)						
		else:		
			return word											#else return word to main	

	if len(num) == 5:											#for ten thousand input
		if num[0] == '1':										
			word += search(int(num[1]), teens) + "thousand "	#gets the word form of the digit and append the word thousand
			if int(num[2:]) != 0:								
				return numToWordsFxn(num[2:], word)				#if the remaining numbers are not yet 0, recursive call
			else:
				return word 		 							#else return word to main	
		else:
			word += search(int(num[0]), tens) + " "
			return numToWordsFxn(num[1:], word)	 

	if len(num) == 7:											#for million input
		word += search(int(num[0]), ones) + "million "			#gets the word form of the digit and append the word million
		if int(num[1:]) != 0:									#if the remaining numbers are not yet 0, recursive call
			return numToWordsFxn(num[1:], word)
		else:
			return word											#else return word to main											

def search(num, arr):											#auxiliary function for searching
	i = 0
	for word in arr:
		if i == num:
			return word
		i += 1

###################
# 2. WORDS TO NUM #
###################
def wordsToNum(num):
	result = 0
	temp = 0

	num = num.split(" ")										#split num to array of strings
	for word in num:
		if word in ones:										#checks array of ones
			temp += (ones.index(word))							#accumulates to temp before multiplying
		if word in tens:
			temp += (tens.index(word) * 10)
		if word in teens:
			temp += (teens.index(word) + 10)
		if word == 'hundred':
			temp *= 100
		if word == 'thousand':
			temp *= 1000
			result += temp
			temp  = 0
		if word == 'million':
			temp *= 1000000
			result += temp
			temp = 0

	result += temp												#accumulates to result 
	return result												#returns result to main
	

########################
# 3. WORDS TO CURRENCY #
########################
def wordsToCurrency(num, currency):
	return currency + " " + str(wordsToNum(num))				#prepends currency to result of function call wordsToNum

########################
# 4. NUMBER DELIMITED  #
########################
def numberDelimited(num, delimiter, index):						
	index = len(str(num)) - int(index)							#computes how many jumps from right to left needed
	count = 0													#check number of digit is equal to required jump
	result = ""													#holds the result
	for char in str(num):							
		if count == index:										#if count is equal to required jump, appends the delimiter first before adding the digit
			result += delimiter
		result += char
		count += 1
	if count == index:
		result += delimiter										#if jump == len(str), prepend the delimiter to result
	return result