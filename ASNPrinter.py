__author__ = 'wblack'

masterList = {}
asnList = open("/Users/wblack/Documents/global_ASN.txt").readlines()
transpacList = open("/Users/wblack/transpac-origin-asn").readlines()

for i in asnList:
    line = i.split("|", 4)
    masterList[line[0]] = line[2]

for j in transpacList:
    key = j.strip('\n')
    if key not in masterList:
        print key, "not present"
    else:
        print 'ASN:', key, '  ORG ID:', masterList[key]