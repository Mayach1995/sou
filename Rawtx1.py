import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0100000001675e134847456cbf88ee9c32fdd22ed75df056b77374651462ba4aefe25b2256000000006b483045022100a1695e0f8277903c23f59e7e580aa232b1d5f29a2072a343af71416cc966f9ff022043779d3b014c1bc0100d31fdba6d591b8c8fe0fa81b907245b5c083619162ff901210245fc9bb6ee1a1a3467088c83d0003d43468b8df9d502dbc1a9fb7fbda78c1bc9ffffffff0200e40b54020000001976a914256af90c52bda88cf1d3cf67c635b726c048efa288ac5e4bd5dc010000001976a914b047258b638f00ed5df5b34c20049a9a3ad3ba4088ac00000000"

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


