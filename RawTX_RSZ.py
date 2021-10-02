import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0100000001d399e443104d753569f861d31f66887fb86368dcd728d824bf2648ee22b16bba010000006b483045022100c281c1bf11c6ad6afeff992907b33993eabd78cab8e130c2894302fa9761bf0902206719d3e9feb142bc9f982359b57620fa2169b5daa5ea53e50173ced743834aaf01210245fc9bb6ee1a1a3467088c83d0003d43468b8df9d502dbc1a9fb7fbda78c1bc9ffffffff02b169eb05000000001976a914d66b6f29ef254c5dac230c6902a98d149e6e078f88acbf2f0a00000000001976a91455b352b6f4c3ff32d85e54e8db32d8ade7e6465488ac00000000"

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


