import re, sys
import MySQLdb as mdb



def uld(anot, cur):
 	#anot = {'definition':definition,'accession':accession,'version':version,'gi':gi,'dbsource':dbsource,'source':source, 'rct':ct}
	cur.execute("insert into refseqdb (definition,accession, version, gi, dbsource, source, rct) values ('%s', '%s', '%s', '%s', '%s', '%s', %d)" %   (mdb.escape_string(anot['definition']), mdb.escape_string(anot['accession']), mdb.escape_string(anot['version']), mdb.escape_string(anot['gi']), mdb.escape_string(anot['dbsource']), mdb.escape_string(anot['source']), anot['rct']))
	con.commit()

	
con = None


try:
	con = mdb.connect('localhost', 'username', 'password', 'database')
	cur = con.cursor()

except mdb.Error, e:
	print "Error %d: %s" % (e.args[0],e.args[1])



con.commit()



f = open(sys.argv[1])

rec = []
reclist = []
locusarray = []
ldr = ''
for l in f:
  l = re.sub('\n', '', l)
  if re.match('^LOCUS', l):
	ldr = re.match('^.*(..-...-....)',l)
	locusdatestr =  ldr.group(1)
	locusarray.append(locusdatestr)
	#anot = recparse(rec,locusdatestr,uidct)
	#uld(uidct,anot, cur)
	reclist.append(rec)
	rec = []	
  else:
	rec.append(l)


ct = 0
recstry = []
for a in reclist:
	locusdate = locusarray[ct]
	ct = ct + 1
	arstr = ''
	for aa in a:
		arstr = arstr + aa
	recstry.append(arstr)

ct = 0
definition = ''
accession = ''
version = ''
gi = ''
dbsource = ''
source = ''
for a in range(1, len(recstry)):
	ct = ct + 1
	#ma = re.match('^DEFINITION  (.*)ACCESSION   (.*)VERSION     (.*)  GI:(.*)DBSOURCE    (.*)KEYWORDS    (.*)SOURCE      (.*)ORGANISM.*$',a)

	if re.match('^DEFINITION ',recstry[a]):
		ma = re.match('^DEFINITION (.*)ACCESSION  .*REFERENCE',recstry[a])
		definition = ma.group(1)
	'''
	if re.match('^DEFINITION .*ACCESSION .*REFERENCE',recstry[a]):
		ma = re.match('^DEFINITION  .*ACCESSION   (.*)VERSION     ',recstry[a])
		accession = ma.group(1)
	if re.match('^DEFINITION .*ACCESSION .*VERSION   .*REFERENCE',recstry[a]):
		ma = re.match('^DEFINITION  .*ACCESSION   .*VERSION     (.*)  GI:.*REFERENCE',recstry[a])
		version = ma.group(1)
	if re.match('^DEFINITION .*ACCESSION .*VERSION   .*GI:.*REFERENCE',recstry[a]):
		ma = re.match('^DEFINITION  .*ACCESSION   .*VERSION     .*  GI:(.*)DBSOURCE    .*KEYWORDS    .*SOURCE      .*ORGANISM  .*REFERENCE',recstry[a])
		gi = ma.group(1)
	if re.match('^DEFINITION .*ACCESSION .*VERSION   .*GI:.*DBSOURCE.*REFERENCE',recstry[a]):
		ma = re.match('^DEFINITION  .*ACCESSION   .*VERSION     .*  GI:.*DBSOURCE    (.*)KEYWORDS    .*SOURCE      .*ORGANISM  .*REFERENCE',recstry[a])
		dbsource = ma.group(1)
	if re.match('^DEFINITION .*ACCESSION .*VERSION   .*GI:.*DBSOURCE.*SOURCE.*REFERENCE',recstry[a]):
		ma = re.match('^DEFINITION  .*ACCESSION   .*VERSION     .*  GI:.*DBSOURCE    .*KEYWORDS    (.*)SOURCE      .*ORGANISM  .*REFERENCE',recstry[a])
		source = ma.group(1)
 	anot = {'definition':definition,'accession':accession,'version':version,'gi':gi,'dbsource':dbsource,'source':source, 'rct':ct}
	'''
 	anot = {'definition':definition}
	print anot
	#uld(anot, cur)



if con:
	con.close()



