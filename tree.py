#!/usr/bin/python

# Sample showing parsing an XML using xmltodict.
# For parsing XML outputs from nmap, nessus, etc.

import xmltodict
from collections import OrderedDict
import os

def output(spacer, field, value):
	# Just print output
	offset = '\n' + spacer + '  ` '
	if type(value) is OrderedDict:
		print '%s- [%s] <dict>' % (spacer, field)
	elif type(value) is list:
		print '%s- [%s] <list>' % (spacer, field)
	else:
		# Showoff, alignment in case of \n\n
		value = os.linesep.join([s for s in str(value).splitlines() if s])
		pval = offset.join(str(value).split('\n'))
		print '%s- %s -> %s' % (spacer, field, pval)

def loadChild(item, spacer):
	# Load child node function based on whether it is dict or list
	if type(item) is OrderedDict:
		dictLoad(item, spacer)
	elif type(item) is list:
		listLoad(item, spacer)

def dictLoad(tree, spacer):
	# Deals with dictionary child
	i = 0
	for item in tree.keys():
		if i<len(tree):
			nspacer = spacer + '  |'
		else:
			nspacer = spacer + '   '
		output(spacer, item, tree[item])
		loadChild(tree[item], nspacer)
		i += 1

def listLoad(mylist, spacer):
	# Deals with list child
	i = 0
	for item in mylist:
		if i<len(mylist):
			nspacer = spacer + '  |'
		else:
			nspacer = spacer + '   '
		output(spacer, '%d' % i, item)
		loadChild(item, nspacer)
		i += 1

f = open('nessus_report.nessus')
xml = f.read()
f.close()

doc = xmltodict.parse(xml)
loadChild(doc, '')
