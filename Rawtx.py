import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "01000000012fddaafdc4e06e67ccf01eccf1d76c6b2747f543835191e13b3f28600b65973f000000006a473044022040dcdb89c361dc0ef8d0fdc2764f9bc1888fe8b183a1e2cfb568c8e92d27771402204b0adf970bd576262b1036406b901ddfd1cb280e0337dd29b6f30e1a9d3d1c0201210245fc9bb6ee1a1a3467088c83d0003d43468b8df9d502dbc1a9fb7fbda78c1bc9ffffffff0200e220a2040000001976a914f72009a230d15eaf0ca431e890793f4c3a1e36d288ac00943577000000001976a914aba7e554c3f7faf1edc392c5130cbe147dc8e0d988ac00000000"

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

