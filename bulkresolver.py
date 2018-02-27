#!/usr/bin/python
'''
Bulk Resolver
Author: blak3irwin


A utility to resolve in bulk IP Addresses and Hostnames.  There is also a
switch for single resolution, but you may be better served with another
DNS utility such as nslookup or dig.
'''

import os
import sys
import dns.resolver
import dns.reversename

def resolve_to_ip(names):
	file = open(names,'rU')
	name_list = file.read().splitlines()
	resolved=[]
	for line in name_list:
		try:
			answer=dns.resolver.query(line,'a')
		        for rdata in answer:
                	        resolved.append(rdata)
				print line, rdata
		except:
			print line, 'QUERY FAILED'
	print '\n\n'
	print 'PRINTING SORTED LIST OF RESOLVED IPS:'
	for i in sorted(resolved):
		print i
def resolve_to_name(ips):
	file = open(ips,'rU')
	ip_list = file.read().splitlines()
	resolved=[]
	for line in ip_list:
		print line
		try:
			rev= '.'.join(reversed(line.split('.')))+'.in-addr.arpa'
			print rev
                	answer=dns.resolver.query(rev,'PTR')
                        for rdata in answer:
                                resolved.append(rdata)
                                print line, rdata
                except:
                        print line, 'QUERY FAILED'
        print '\n\n'
        print 'PRINTING SORTED LIST OF RESOLVED IPS:'
        for i in sorted(resolved):
                print i

def resolve_single(single,rectype):
	if rectype == 'PTR':
		rev= '.'.join(reversed(single.split('.')))+'.in-addr.arpa'
		answer=dns.resolver.query(rev,rectype)
		for rdata in answer:
			rdata
			print rdata

	elif rectype == 'ALL':
		list = ['A', 'MX', 'NS', 'TXT']
		for i in list:
			try:
				answer=dns.resolver.query(single,i)
				for rdata in answer:
					print rdata
			except:
				print i, 'RECORD QUERY FAILED'


		rev= '.'.join(reversed(single.split('.')))+'.in-addr.arpa'
		try:
			answer=dns.resolver.query(rev,'PTR')
			for rdata in answer:
				print rdata
		except:
			print 'PTR RECORD QUERY FAILED'
	else:
		try:
			answer=dns.resolver.query(single,rectype)
			for rdata in answer:
				print rdata
		except:
			print PTR, 'QUERY FAILED'


#begin main program'''
args = sys.argv[1:]

if not args:
	print 'usage: ./builkresolver.py [--ips list_of_ips.txt OR --names list_of_names.txt OR --single <DNS Record Type> <IP or Hostname>]'
	print 'examples: ./bulkresolver.py --ips ips.txt'
	print './bulkresolver.py --names names.txt'
	print './bulkresolver.py --single PTR 8.8.8.8'
	print './bulkresolver.py --single <A,MX,NS,TXT,PTR,ALL> google.com'
	sys.exit(1)

if args:
	if args[0] == '--ips':
		ips = args[1]
		del args[0:2]
		#print 'ips file =',ips
		resolve_to_name(ips)

	elif args[0] == '--names':
		names = args[1]
		del args[0:2]
		#print 'names file=',names
		resolve_to_ip(names)
	elif args[0] == '--single':
		rectype = args[1]
		single = args[2]
		resolve_single(single,rectype)
	else:
		print 'usage: [--ips list_of_ips.txt OR --names list_of_names.txt]'
        sys.exit(1)
