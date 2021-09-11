import re, sys
import numpy as np
import MySQLdb as mdb



def search(aulkid, cur):
	sstr = "select b.cc from uprtccfx as b join anotinventorylookupclean as c on c.uid = b.uid where c.aulkid = "+aulkid 
	cur.execute(sstr)
	con.commit()
	row = cur.fetchone()
	return row

def parser(aulkid,b):
	ALLERGEN = [] 
	ALTERNATIVE_PRODUCTS = []
	BIOPHYSICOCHEMICAL_PROPERTIES = []
	BIOTECHNOLOGY = []
	CATALYTIC_ACTIVITY = []
	CAUTION = []
	COFACTOR = []
	DEVELOPMENTAL_STAGE = []
	DISEASE = []
	DISRUPTION_PHENOTYPE = []
	DOMAIN = []
	ENZYME_REGULATION = []
	FUNCTION = []
	INDUCTION = []
	INTERACTION = []
	MASS_SPECTROMETRY = []
	MISCELLANEOUS = []
	PATHWAY = []
	PHARMACEUTICAL = []
	POLYMORPHISM = []
	PTM = []
	RNA_EDITING = []
	SEQUENCE_CAUTION = []
	SIMILARITY = []
	SUBCELLULAR_LOCATION = []
	SUBUNIT = []
	TISSUE_SPECIFICITY = []
	WEB_RESOURCE = []

	bbb = ''
	for bb in b:
		bb = re.sub('CC       ', ' ', bb)
		bbb = bbb + bb
		
	bbbb = re.split('CC   -!- ', bbb)
	for l in bbbb:
		if re.match('^ALLERGEN', l):
		   l = re.sub('^ALLERGEN:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   ALLERGEN.append(l)
		if re.match('^ALTERNATIVE PRODUCTS', l):
		   l = re.sub('^ALTERNATIVE PRODUCTS:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   ALTERNATIVE_PRODUCTS.append(l)
		if re.match('^BIOPHYSICOCHEMICAL PROPERTIES', l):
		   l = re.sub('^BIOPHYSICOCHEMICAL PROPERTIES:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   BIOPHYSICOCHEMICAL_PROPERTIES.append(l)
		if re.match('^BIOTECHNOLOGY', l):
		   l = re.sub('^BIOTECHNOLOGY:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   BIOTECHNOLOGY.append(l)
		if re.match('^CATALYTIC ACTIVITY', l):
		   l = re.sub('^CATALYTIC ACTIVITY:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   CATALYTIC_ACTIVITY.append(l)
		if re.match('^CAUTION', l):
		   l = re.sub('^CAUTION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   CAUTION.append(l)
		if re.match('^COFACTOR', l):
		   l = re.sub('^COFACTOR:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   COFACTOR.append(l)
		if re.match('^DEVELOPMENTAL STAGE', l):
		   l = re.sub('^DEVELOPMENTAL STAGE:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   DEVELOPMENTAL_STAGE.append(l)
		if re.match('^DISEASE', l):
		   l = re.sub('^DISEASE:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   DISEASE.append(l)
		if re.match('^DISRUPTION PHENOTYPE', l):
		   l = re.sub('^DISRUPTION PHENOTYPE:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   DISRUPTION_PHENOTYPE.append(l)
		if re.match('^DOMAIN', l):
		   l = re.sub('^DOMAIN:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   DOMAIN.append(l)
		if re.match('^ENZYME REGULATION', l):
		   l = re.sub('^ENZYME REGULATION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   ENZYME_REGULATION.append(l)
		if re.match('^FUNCTION', l):
		   l = re.sub('^FUNCTION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   FUNCTION.append(l)
		if re.match('^INDUCTION', l):
		   l = re.sub('^INDUCTION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   INDUCTION.append(l)
		if re.match('^INTERACTION', l):
		   l = re.sub('^INTERACTION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   INTERACTION.append(l)
		if re.match('^MASS SPECTROMETRY', l):
		   l = re.sub('^MASS SPECTROMETRY:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   MASS_SPECTROMETRY.append(l)
		if re.match('^MISCELLANEOUS', l):
		   l = re.sub('^MISCELLANEOUS:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   MISCELLANEOUS.append(l)
		if re.match('^PATHWAY', l):
		   l = re.sub('^PATHWAY:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   PATHWAY.append(l)
		if re.match('^PHARMACEUTICAL', l):
		   l = re.sub('^PHARMACEUTICAL:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   PHARMACEUTICAL.append(l)
		if re.match('^POLYMORPHISM', l):
		   l = re.sub('^POLYMORPHISM:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   POLYMORPHISM.append(l)
		if re.match('^PTM', l):
		   l = re.sub('^PTM:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   PTM.append(l)
		if re.match('^RNA EDITING', l):
		   l = re.sub('^RNA EDITING:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   RNA_EDITING.append(l)
		if re.match('^SEQUENCE CAUTION', l):
		   l = re.sub('^SEQUENCE CAUTION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   SEQUENCE_CAUTION.append(l)
		if re.match('^SIMILARITY', l):
		   l = re.sub('^SIMILARITY:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   SIMILARITY.append(l)
		if re.match('^SUBCELLULAR LOCATION', l):
		   l = re.sub('^SUBCELLULAR LOCATION:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   SUBCELLULAR_LOCATION.append(l)
		if re.match('^SUBUNIT', l):
		   l = re.sub('^SUBUNIT:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   SUBUNIT.append(l)
		if re.match('^TISSUE SPECIFICITY', l):
		   l = re.sub('^TISSUE SPECIFICITY:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   TISSUE_SPECIFICITY.append(l)
		if re.match('^WEB RESOURCE', l):
		   l = re.sub('^WEB RESOURCE:', '', l)
		   l = re.sub('CC   --------------------------------.*', '', l)
		   l = re.sub('CC   Copyrighted by the UniProt Consortium.*', '', l)
		   WEB_RESOURCE.append(l)

	ccdict = {'aulkid':aulkid, 'ALLERGEN':ALLERGEN,'ALTERNATIVE PRODUCTS':ALTERNATIVE_PRODUCTS,'BIOPHYSICOCHEMICAL PROPERTIES':BIOPHYSICOCHEMICAL_PROPERTIES,'BIOTECHNOLOGY':BIOTECHNOLOGY,'CATALYTIC ACTIVITY':CATALYTIC_ACTIVITY,'CAUTION':CAUTION,'COFACTOR':COFACTOR,'DEVELOPMENTAL STAGE':DEVELOPMENTAL_STAGE,'DISEASE':DISEASE,'DISRUPTION PHENOTYPE':DISRUPTION_PHENOTYPE,'DOMAIN':DOMAIN,'ENZYME REGULATION':ENZYME_REGULATION,'FUNCTION':FUNCTION,'INDUCTION':INDUCTION,'INTERACTION':INTERACTION,'MASS SPECTROMETRY':MASS_SPECTROMETRY,'MISCELLANEOUS':MISCELLANEOUS,'PATHWAY':PATHWAY,'PHARMACEUTICAL':PHARMACEUTICAL,'POLYMORPHISM':POLYMORPHISM,'PTM':PTM,'RNA EDITING':RNA_EDITING,'SEQUENCE CAUTION':SEQUENCE_CAUTION,'SIMILARITY':SIMILARITY,'SUBCELLULAR LOCATION':SUBCELLULAR_LOCATION,'SUBUNIT':SUBUNIT,'TISSUE SPECIFICITY':TISSUE_SPECIFICITY,'WEB RESOURCE':WEB_RESOURCE}
	return ccdict


def empties(ccdict):
	if len(ccdict['ALLERGEN']) < 1:
		ccdict['ALLERGEN'].append('')
	if len(ccdict['ALTERNATIVE PRODUCTS']) < 1:
		ccdict['ALTERNATIVE PRODUCTS'].append('')
	if len(ccdict['BIOPHYSICOCHEMICAL PROPERTIES']) < 1:
		ccdict['BIOPHYSICOCHEMICAL PROPERTIES'].append('')
	if len(ccdict['BIOTECHNOLOGY']) < 1:
		ccdict['BIOTECHNOLOGY'].append('') 
	if len(ccdict['CATALYTIC ACTIVITY']) < 1:
		ccdict['CATALYTIC ACTIVITY'].append('') 
	if len(ccdict['CAUTION']) < 1:
		ccdict['CAUTION'].append('') 
	if len(ccdict['COFACTOR']) < 1:
		ccdict['COFACTOR'].append('') 
	if len(ccdict['DEVELOPMENTAL STAGE']) < 1:
		ccdict['DEVELOPMENTAL STAGE'].append('') 
	if len(ccdict['DISEASE']) < 1:
		ccdict['DISEASE'].append('') 
	if len(ccdict['DISRUPTION PHENOTYPE']) < 1:
		ccdict['DISRUPTION PHENOTYPE'].append('') 
	if len(ccdict['DOMAIN']) < 1:
		ccdict['DOMAIN'].append('') 
	if len(ccdict['ENZYME REGULATION']) < 1:
		ccdict['ENZYME REGULATION'].append('') 
	if len(ccdict['FUNCTION']) < 1:
		ccdict['FUNCTION'].append('') 
	if len(ccdict['INDUCTION']) < 1:
		ccdict['INDUCTION'].append('') 
	if len(ccdict['INTERACTION']) < 1:
		ccdict['INTERACTION'].append('') 
	if len(ccdict['MASS SPECTROMETRY']) < 1:
		ccdict['MASS SPECTROMETRY'].append('') 
	if len(ccdict['MISCELLANEOUS']) < 1:
		ccdict['MISCELLANEOUS'].append('') 
	if len(ccdict['PATHWAY']) < 1:
		ccdict['PATHWAY'].append('') 
	if len(ccdict['PHARMACEUTICAL']) < 1:
		ccdict['PHARMACEUTICAL'].append('') 
	if len(ccdict['POLYMORPHISM']) < 1:
		ccdict['POLYMORPHISM'].append('') 
	if len(ccdict['PTM']) < 1:
		ccdict['PTM'].append('') 
	if len(ccdict['RNA EDITING']) < 1:
		ccdict['RNA EDITING'].append('') 
	if len(ccdict['SEQUENCE CAUTION']) < 1:
		ccdict['SEQUENCE CAUTION'].append('') 
	if len(ccdict['SIMILARITY']) < 1:
		ccdict['SIMILARITY'].append('') 
	if len(ccdict['SUBCELLULAR LOCATION']) < 1:
		ccdict['SUBCELLULAR LOCATION'].append('') 
	if len(ccdict['SUBUNIT']) < 1:
		ccdict['SUBUNIT'].append('') 
	if len(ccdict['TISSUE SPECIFICITY']) < 1:
		ccdict['TISSUE SPECIFICITY'].append('') 
	if len(ccdict['WEB RESOURCE']) < 1:
		ccdict['WEB RESOURCE'].append('') 
	return ccdict

def sqlinsert(ccdict, aulkid):
	cur.execute("insert into cctab (aulkid, ALLERGEN, ALTERNATIVE_PRODUCTS, BIOPHYSICOCHEMICAL_PROPERTIES, BIOTECHNOLOGY, CATALYTIC_ACTIVITY, CAUTION, COFACTOR, DEVELOPMENTAL_STAGE, DISEASE, DISRUPTION_PHENOTYPE, DOMAIN, ENZYME_REGULATION, FUNCTION, INDUCTION, INTERACTION, MASS_SPECTROMETRY, MISCELLANEOUS, PATHWAY, PHARMACEUTICAL, POLYMORPHISM, PTM, RNA_EDITING, SEQUENCE_CAUTION, SIMILARITY, SUBCELLULAR_LOCATION, SUBUNIT, TISSUE_SPECIFICITY, WEB_RESOURCE) values (%s,  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s')" % (int(aulkid),mdb.escape_string(ccdict['ALLERGEN'][0]), mdb.escape_string(ccdict['ALTERNATIVE PRODUCTS'][0]), mdb.escape_string(ccdict['BIOPHYSICOCHEMICAL PROPERTIES'][0]), mdb.escape_string(ccdict['BIOTECHNOLOGY'][0]), mdb.escape_string(ccdict['CATALYTIC ACTIVITY'][0]), mdb.escape_string(ccdict['CAUTION'][0]), mdb.escape_string(ccdict['COFACTOR'][0]), mdb.escape_string(ccdict['DEVELOPMENTAL STAGE'][0]), mdb.escape_string(ccdict['DISEASE'][0]), mdb.escape_string(ccdict['DISRUPTION PHENOTYPE'][0]), mdb.escape_string(ccdict['DOMAIN'][0]), mdb.escape_string(ccdict['ENZYME REGULATION'][0]), mdb.escape_string(ccdict['FUNCTION'][0]), mdb.escape_string(ccdict['INDUCTION'][0]), mdb.escape_string(ccdict['INTERACTION'][0]), mdb.escape_string(ccdict['MASS SPECTROMETRY'][0]), mdb.escape_string(ccdict['MISCELLANEOUS'][0]), mdb.escape_string(ccdict['PATHWAY'][0]), mdb.escape_string(ccdict['PHARMACEUTICAL'][0]), mdb.escape_string(ccdict['POLYMORPHISM'][0]), mdb.escape_string(ccdict['PTM'][0]), mdb.escape_string(ccdict['RNA EDITING'][0]), mdb.escape_string(ccdict['SEQUENCE CAUTION'][0]), mdb.escape_string(ccdict['SIMILARITY'][0]), mdb.escape_string(ccdict['SUBCELLULAR LOCATION'][0]), mdb.escape_string(ccdict['SUBUNIT'][0]), mdb.escape_string(ccdict['TISSUE SPECIFICITY'][0]), mdb.escape_string(ccdict['WEB RESOURCE'][0])))
	con.commit()
	
	


### MAIN CODE ###

try:
        con = mdb.connect('localhost', 'username', 'password', 'database')
        cur = con.cursor()
except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])

a = open(sys.argv[1])

for l in a:
	l = re.sub('\n', '', l)
	l = re.sub('\r', '', l)
	b = search(l,cur)
	c = re.split('--htsr--', b[0])
	ccdict = parser(l,c)
	ccdict = empties(ccdict)
	sqlinsert(ccdict, l)
