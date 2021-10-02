import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0100000006b21b20ccab126d56fb2660cd1b41218b8281878bab39d4330060612e674d0e37010000006a473044022015fff82156fc733100889f0754c6fe8c2b0b1cd07778e0af4cb870a47bc21c40022020e8cca4502d854c3c9c8b9ff7f61dfd0e3a6f9c586dc671d6c98553f722d3d801210385379f0253df67e7520ac4f43506b0ea7d47f00a196bb3ba69a8cf1941251dc0ffffffff9ca41f0ec53d618ca782a6fdfdc95fbe36df23afc7e6292309a293b9094669fb010000006c493046022100defda56e0e7bde2a007e1dd145d47af8770ce60e728b862dd2a2da42a6b4bab2022100af4ec255089059079552279ae0a17e72c5dcab5dcbbf6cbdcf7011104ecec173012102b5e528a94f81fb9cc1b671418acdbecd0096f0de4bc3179438753dcd71fb13e3ffffffff62f1b3755bbcc522a1ab792c805ec85f0b61de19cbbe1085f470dc03e2ea470a010000006b48304502203f3deb4ca8c57fa411fdeb9cd0be22161cc8fce617ce775a3dc505425fb43472022100cfd7ed5d0cef209e880762794ffced9a4ff74f3df844860e7bb4f6e518d864fc012102928b4effb34b97e8538c11b4ed75818c2929b2f64d37d84c790c24f902c47529ffffffffa808453ea3cc2e2ca25179f34a7f007a732273a0ba598ea208d9dcf9571aa645000000006b483045022052f2cdc476546b7fcd8cf5c0ad3e46c60ae3a8f0ccf275838904d4a354d7d34802210091564e2efff0d234818dbb57e3a2dcb1764a85268be38804726bf754cda4e82f012102194ca34338327facc790467870c54607b81e4649888e76d806cc0c13b1da1913ffffffff64ed7bbcf626b3fde88142c83df66627cbb78dc405e583757dc985ee5a334b73010000006b4830450220377d66958d711e5840d518e05552fcf02289b315dc5bfe34915b080410a908c8022100df28f32b5c8717dfb7ea3103433144815d2886642a3919b3607bdae9628ec49d0121026c7492b138334cd70e611179bfc6252c0172105a455cefca13fda243600a55c6ffffffff70962381e96ab3eb53dc165a051bfe2436017b79e0b3bc1aaa538e251ddafdcc010000006c49304602210082c1748504e03c764d1502faba559fc37b874d329cbb3c2a4699cb5ab4446cb70221008546f41b15d934d8d1ee963f3da8e2967082636764bd3dbcf495179d3ea536560121031de8328ee71e38abd219ac481c505b45a608e58ed387c6cb6b7d0e39ca185906ffffffff02b0622a59000000001976a91480ee341d9235e8bb20c4a6abc7433f843fedf64088ac66264c08000000001976a91442c332827e91780ca34b59af7eecc175c0a33f6988ac00000000"

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


