import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "010000000188c396d1472f99d8120f6880365ab3be8cdb3a809fd1e53888afb05b1886b4d4040000006b483045022100d1e4a6924937ca46095aec78e349f515e249293abd4c2393bbdf2860f2bdc8ea02205953cd8f55521722702084ebe5b923dd1e137786807c9dce261338113ede60560121031de8328ee71e38abd219ac481c505b45a608e58ed387c6cb6b7d0e39ca185906ffffffff02b082c223000000001976a914ebad630482c849874dfa3ff7b55a5a296c5f139988ac2ac53288000000001976a9148e8010af55f579cabdd56f476d53c2009907bcd588ac00000000"

m = txnUtils.parseTxn(tx)
e = txnUtils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')
s = keyUtils.derSigToHexSig(m[1][:-2])
pub =  m[2]
sigR = s[:64]
sigS = s[-64:]
sigZ = z
print ('Signed TX is :', tx)
print ('Signature (r, s pair) is :', s)
print ('Public Key is :', pub)
print ("")
print ("#################################################################################################")
print ("")
print ('Unsigned TX is :', e)
print ('hash of message (sigZ) is USE This ONE :', z)
print ('reversed z :', z1)
print ("")
print ("#################################################################################################")
print ("##################################VALUES NEEDED ARE BELOW #######################################")
print ("#################################################################################################")
print ("")
print ('THE R VALUE is  :', sigR)
print ('THE S VALUE is  :', sigS)
print ('THE Z VALUE is  :', sigZ)
print ('THE PUBKEY is :', pub)

