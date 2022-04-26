import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "010000000706b0efadaca4766a7d2e5427f9a803b151cbc4486205d5248806870ce7de8e8e000000008b48304502205706a053d30e90def1e863b2c8ec0f0c462e565cc19090c4926f105664d1bdf0022100c264b37bdf4ffb6174c13c6cd9f22ed3f8b66fc15ae37408a22902fb07175acc014104d6597d465408e6e11264c116dd98b539740e802dc756d7eb88741696e20dfe7d3588695d2e7ad23cbf0aa056d42afada63036d66a1d9b97070dd6bc0c87ceb0dffffffff8d48030e9030168697d03541206be1368365693ce8077ecaf18c0d717776fac1000000004847304402204b9e098bcc5deb14ec868f53bf6ed38d2a45b4f13a13bb10e9b3b67a633b47b60220468e7fd9c901c6201eced5abfc4a52522f6e0e7dd60bbfc7c71a213b5ace171201ffffffff978697cf864708dc8e1690b1dd0cf3f7c8d660de46ec4b65cd2c8d22240a04aa0000000049483045022100d55c0ec773f417e37b4958c6e4564f19e7ce562cebef555ff80e7ca78e4d04aa02201ce8ef31dc40cdd6b46986db9d5267292b9fdc150e03603cbd7499aee0c0f81401ffffffffa7739658a9b0c3b35a46fa0062db7a0077d012ce57ce68c3fa366694e3314fa40000000049483045022100ab57dd743e0fdea93389f7a3ba65855d47000a789cdea3245f9e7834faadd6d4022016998895ab0d73cb88f1ac900c80aba2ebe2e852c0a53159d937b73f4ad42b7601ffffffffe978ce3d437cd840fb272037b34022285a12a3ec4ebc61ff1e1bbf232887d4de0000000048473044022012523db1c172ca4b63208d4289a70b1e17b23e082ad06086ed5fb24b4e1162520220484b1a52abe13f1b47c447d6003bca0c0c786a5fe978c45d3c59eccc8cf9474b01fffffffff87adde1214e4d1dc2b167eb7961294beecf0c11a02fb1712ba875c2ba9d2e7f000000004a493046022100d423dd7705b1881d7398109fdc1119681cc2f91ee4baa38d7a78f96d43884f110221009d0cb81043bf95f47fb3e508e2ee9fec999cfbdc03f3ffdbe320058f8676de6101fffffffffaef25ac1a490387b13148a713df92fb170180d1980a20233812d75716351fcc000000004948304502206a58f73b4964d70897f434440dc39b5bce7838d6dcdeff2c64d628b48cb28d430221009b1808a574626953f907170eeaf8de2c03c4b4df46e64377a5fd699709a4a2c201ffffffff0100e87648170000001976a9140366041c1c1e5dfe19bbfdef94fe25a9340ab24588ac00000000"

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


