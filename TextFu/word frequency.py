#!/usr/bin/python

# Takes a file as input.
# Calculate frequency of each word. Only pure word.
# Top used words are returned via retrieve() function.
# Class noteKeeper keeps record of words.
# Class fileReader feed words to keepNote.
# Function main() feed files to fileReader.

import re

class noteKeeper:
	noteBook = {}
	bookList = []
	def __init__(self):
		pass
	def feedWord(self, word):
		if self.noteBook.has_key(word):
			self.noteBook[word] += 1
		else:
			self.noteBook[word] = 1
	def retrieve(self, length=10):
		self.makeList()
		bookList = self.bookList
		if length > len(bookList):
			length = len(bookList)
		for i in range(length):
			print '%s \t{%d}' % (bookList[i][1], bookList[i][0])
	def makeList(self):
		self.bookList = []
		for items in self.noteBook.items():
			self.bookList.append((items[1], items[0]))
		self.bookList.sort()
		self.bookList.reverse()
	def count(self):
		return len(self.noteBook)
		

class fileReader:
	note = noteKeeper()
	def __init__(self):
		pass
	def feedFile(self, fileName):
		try:
			f = open(fileName, 'r')
		except:
			print 'File not opened'
			return
		for lines in f.readlines():
			for words in re.findall('[a-z]+\\\\', re.escape(lines.lower())):
				self.note.feedWord(words.strip('\\'))
	def retrieve(self, num):
		self.note.retrieve(num)
	def count(self):
		return self.note.count()

if __name__ == "__main__":
	myFile = fileReader()
	myFile.feedFile('clock.sub')
	print 'Wordlist created of %d words' % myFile.count()
	while True:
		print '\nEnter number of range (0 to exit)'
		try:
			i = int(raw_input())
		except:
			break
		if i == 0:
			break
		print 'Displaying top %d' % i
		myFile.retrieve(i)
