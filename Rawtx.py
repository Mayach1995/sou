import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "01000000012a483f50ddbeaecf1b1586d6349500517b2d9304ce5725169d25657e0830c755000000008b48304502205ca7c70821d2e309d1eff2aba8ab1362eac870a535a534a482500d3eba9eef18022100a7a4dd346dfd30d2803abe9aa17744f02e02964b98738b15a381a6fc30acdef5014104d6597d465408e6e11264c116dd98b539740e802dc756d7eb88741696e20dfe7d3588695d2e7ad23cbf0aa056d42afada63036d66a1d9b97070dd6bc0c87ceb0dffffffff0200a0db215d0000001976a914666a5bcac99eb29e521abcf864bd08617c8cc2c288ac0088526a740000001976a9142cbcceff99a7a3a34e230b9ba6f1020e6de8714488ac00000000"

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

