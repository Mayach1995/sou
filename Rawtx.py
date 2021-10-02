import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0200000001f8bc40f365b47ec2d18b1cbcde905364aad03c2e1835bdddd0ee5326c670dcf9010000006a473044022019a835bacbb99402ddbfb8acb1d7f14b491feb4256608fb36300823a3d0a59a002204285450e6425c5225a471020c544d60e46c5e45b2d9a0f65ad51add976283ee301210302570c945dc0ae3bd39c09a98dd702be11f45187517d5c023a640a4264241b00feffffff0280d54302000000001976a914674b87c22854d1c67c06fef355c03992380243fb88ac4dd4aa01000000001976a914f61f364311a0e696358db520079551b4c5d82f6088ac4c020700"

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

