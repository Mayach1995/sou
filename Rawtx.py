import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "01000000019df22115690f22895c07a91d36af0f513c4f6f96fca7612cb5ed32bd023e7844000000006b4830450221009317bbb84f3c38695cae7e71bb853377f0f659078a354e3c7ea4c9771c2ea39902206b3960fadf846fdfb6856ae5f74d6f2c108fb752c1860a4e2ff33b868050cd69012102679a681d9b5bf5c672e0413997762664a17009038674b806bf27dd6b368d9b67feffffff0350c30000000000001976a9141ae9ae0209314a01c8541936f7f4875c1851c55c88ac60670100000000001976a914b169705d617c39ca0fe29469fb2f068a6041ef5a88acd8bcf105000000001976a914e8cea30989bd15530f819b766684b00dc7ba7cfa88ac00000000"

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

