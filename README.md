# bulkresolver.py

Bulk Resolver
Author: blak3irwin


A utility to resolve in bulk IP Addresses and Hostnames.  There is also a
switch for single resolution, but you may be better served with another
DNS utility such as nslookup or dig.

# Usage: 
```
./bulkresolver.py [--ips list_of_ips.txt OR --names list_of_names.txt OR --single <DNS Record Type> <IP or Hostname>]
```
## Examples: 
```
./bulkresolver.py --ips ips.txt
./bulkresolver.py --names names.txt
#--single feature is a little buggy.  nslookup or dig may better server you for single lookups.
./bulkresolver.py --single PTR 8.8.8.8
./bulkresolver.py --single <A,MX,NS,TXT,PTR,ALL> google.com
```
