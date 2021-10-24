import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "010000000001019b406f0f1b7c0fa5a8826e37aa951e5715caf555b99adc292942e4cd66a6c1eb0100000017160014be86245a4cc90f0f7b24194a38cc82fbc53ab13c0000000002102700000000000017a91489f56e1525625b724b84452442738388be057a0787302301000000000017a91455ca9a4501a7b340d8d97b89e5807f9d2ce9e40d8702483045022100f578f8e00594438e317fa1a2947005144b3ded3490514dbfefe85a58f181772302206d2efbbc795395a9db18421acd61f586c508d199bba57f7fb82e7ff06653dafe012103afb37ed12717a31b5bd872870dc70c3a6a8f0faac8d23c4657b3b6d4d271b92f00000000"

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


