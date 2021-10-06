import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0200000002bf54d7c23575d4c63f192df6fa6abcc08d47036785bc88505d5029f1abc8689d000000006b483045022100db0c51cc634a4096374b0b895584a3ca2fb3bea4fd0ee2361f8db63a650fcee6022059a23e4521da413a2c7d0f9a668eedc2e5eac88347c67c48dcca0128fda1cad7012102ac75a5bd9640d55b8300fad347740ac447e4604fbc59260c2dce39f356a0558fffffffff024663893f3a96159be87c402b9ea8b09b8589e2d77fd38376295d99fc0fa429000000006b483045022100db0c51cc634a4096374b0b895584a3ca2fb3bea4fd0ee2361f8db63a650fcee6022039d5e056231a5823dc0957e3d0fa3923ce71f781ad67140a6433fe6829bdf811012102ac75a5bd9640d55b8300fad347740ac447e4604fbc59260c2dce39f356a0558fffffffff0120bf02000000000017a9140d3262f59566a01d4d3b780eea0d278dbdb403c48700000000"

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


