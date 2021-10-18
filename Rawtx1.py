import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0100000001be755266c907d7980fb8a5a4ae1a835158cc31efbb342b4ccdd170b76ebf65ad010000006a47304402206211b2bf4ee9afec47510a72058b1a05049864205b2897f68b868654074eb918022018bbf7ae733b861f786a19c890e07400e46272ec28d836658644931a6a233fa0012102acfcf19fc2f5fbf9f37403df45fd154270f49bbc567c943358f3d1dbbd6947f1fdffffff01de030000000000001976a914571b6994a7a968be41b6631f8ba44d9dbadb60b088ac00000000"

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


