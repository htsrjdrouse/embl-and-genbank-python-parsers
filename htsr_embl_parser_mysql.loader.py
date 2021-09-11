import re, sys
import MySQLdb as mdb



def uld(uidct,anot, cur):
	cur.execute("insert into nuprtcc_just_genbank (uidct,id, acc, ra, rx, dt, de, gn, os, oc, ox, oh, rp, rt, rl, dr, pe, kw, ft, sq, seq,cc) values (%d,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %   (uidct,mdb.escape_string(anot['id']), mdb.escape_string(anot['acc']), mdb.escape_string(anot['ra']), mdb.escape_string(anot['rx']), mdb.escape_string(anot['dt']), mdb.escape_string(anot['de']), mdb.escape_string(anot['gn']), mdb.escape_string(anot['os']), mdb.escape_string(anot['oc']), mdb.escape_string(anot['ox']), mdb.escape_string(anot['oh']), mdb.escape_string(anot['rp']), mdb.escape_string(anot['rt']), mdb.escape_string(anot['rl']), mdb.escape_string(anot['dr']), mdb.escape_string(anot['pe']), mdb.escape_string(anot['kw']), mdb.escape_string(anot['ft']), mdb.escape_string(anot['sq']), mdb.escape_string(anot['seq']), mdb.escape_string(anot['cc'])))
	con.commit()




def iddt(l):
	#ID   001R_FRG3G              Reviewed;         256 AA.
	a = re.match('^ID   (.*)     .*', l)
	id  = a.group(1) 
	id = re.sub(' .*', '', id)
	return id
	
def accdt(l):
	#AC   Q6GZX2;
	a = re.match('^AC   (.*)', l)
	id  = a.group(1) 
	return id



def recparse(rec):
	rastr = ''
	rxstr = ''
	dtstr = ''
	destr = ''
	gnstr = ''
	osstr = ''
	ocstr = ''
	oxstr = ''
	ohstr = ''
	rpstr = ''
	rtstr = ''
	rlstr = ''
	drstr = ''
	pestr = ''
	kwstr = ''
	ftstr = ''
	sqstr = ''
	seq = ''
	ccstr = ''
	for j in rec:
		j = re.sub('\n','',j)
		j = re.sub('\r','',j)
		if re.match('^ID', j):
			idstr =  re.sub(' ','',iddt(j))
		if re.match('^AC', j):
			accstr= accdt(j)
		if re.match('^DT', j):
			j = re.sub('^DT   ', '', j)
			dtstr = dtstr + j + '--htsr--'
		if re.match('^DE', j):
			j = re.sub('^DE   ', '', j)
			destr = destr + j + '--htsr--'
		#GN   ORFNames=FV3-001R;
		if re.match('^GN', j):
			j = re.sub('^GN   ', '', j)
			gnstr = gnstr + j + '--htsr--'
		#OS   Frog virus 3 (isolate Goorha) (FV-3).
		if re.match('^OS', j):
			j = re.sub('^OS   ', '', j)
			osstr = osstr + j + '--htsr--'
		#OC   Viruses; dsDNA viruses, no RNA stage; Iridoviridae; Ranavirus.
		if re.match('^OC', j):
			j = re.sub('^OC   ', '', j)
			ocstr = ocstr + j + '--htsr--'
		#OX   NCBI_TaxID=654924;
		if re.match('^OX', j):
			j = re.sub('^OX   ', '', j)
			oxstr = oxstr + j + '--htsr--'
		#OH   NCBI_TaxID=8295; Ambystoma (mole salamanders).
		if re.match('^OH', j):
			j = re.sub('^OH   ', '', j)
			ohstr = ohstr + j + '--htsr--'
		#RP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA].
		if re.match('^RP', j):
			j = re.sub('^RP   ', '', j)
			rpstr = rpstr + j + '--htsr--'
		#RX   PubMed=16912294; DOI=10.1128/JVI.00464-06;
		if re.match('^RX', j):
			j = re.sub('^RX   ', '', j)
			rxstr = rxstr + j + '--htsr--'
		#RA   Delhon G., Tulman E.R., Afonso C.L., Lu Z., Becnel J.J., Moser B.A.,
		if re.match('^RA', j):
			j = re.sub('^RA   ', '', j)
			rastr = rastr + j + '--htsr--'
		#RT   "Comparative genomic analyses of frog virus 3, type species of the
		if re.match('^RT', j):
			j = re.sub('^RT   ', '', j)
			rtstr = rtstr + j + '--htsr--'
		#RL   Virology 323:70-84(2004).
		if re.match('^RL', j):
			j = re.sub('^RL   ', '', j)
			rlstr = rlstr + j + '--htsr--'
		#DR   EMBL; AY548484; AAT09660.1; -; Genomic_DNA.
		if re.match('^DR', j):
			j = re.sub('^DR   ', '', j)
			drstr = drstr + j + '--htsr--'
		#PE   4: Predicted;
		if re.match('^PE', j):
			j = re.sub('^PE   ', '', j)
			pestr = pestr + j + '--htsr--'
		#KW   Activator; Complete proteome; Reference proteome; Transcription;
		if re.match('^KW', j):
			j = re.sub('^KW   ', '', j)
			kwstr = kwstr + j + '--htsr--'
		#FT   CHAIN         1    256       Putative transcription factor 001R.
		if re.match('^FT', j):
			j = re.sub('^FT   ', '', j)
			ftstr = ftstr + j + '--htsr--'
		#SQ   SEQUENCE   256 AA;  29735 MW;  B4840739BF7D4121 CRC64;
		if re.match('^SQ', j):
			j = re.sub('^SQ   ', '', j)
			sqstr = sqstr + j + '--htsr--'
     		#     MSIIGATRLQ NDKSDTYSAG PCYAGGCSAF TPRGTCGKDW DLGEQTCASG FCTSQPLCAR
		if re.match('^     [A-Z]', j):
			j = re.sub('^     ', '', j)
			j = re.sub(' ','',j)
			seq = seq + j 
		#CC   -!- FUNCTION: Activates ubiquitin by first adenylating its C-terminal
		if re.match('^CC  ', j):
			ccstr = ccstr + j + '--htsr--'


 	anot = {'id':idstr,'acc':accstr,'ra':rastr , 'rx':rxstr , 'dt':dtstr , 'de':destr , 'gn':gnstr , 'os':osstr , 'oc':ocstr , 'ox':oxstr , 'oh':ohstr , 'rp':rpstr , 'rt':rtstr , 'rl':rlstr , 'dr':drstr , 'pe':pestr , 'kw':kwstr , 'ft':ftstr , 'sq':sqstr , 'seq':seq, 'cc':ccstr}
	return anot


con = None


try:
	con = mdb.connect('localhost', 'username', 'password', 'database')
	cur = con.cursor()

except mdb.Error, e:
	print "Error %d: %s" % (e.args[0],e.args[1])



con.commit()



f = open(sys.argv[1])

rec = []
uidct = 0
for l in f:
  l = re.sub('\n', '', l)
  if re.match('^\/\/', l):
	uidct = uidct + 1
	anot = recparse(rec)
	uld(uidct,anot, cur)
	rec = []	
  else:
	rec.append(l)


if con:
	con.close()



