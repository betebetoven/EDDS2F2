import hashlib
from sha256 import shasha
from nodoLL import nodito

# Hash pairs of items recursively until a single value is obtained
pedro = shasha()
general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = hexagon]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"+"        rankdir=BT;\n"
def merkle(hashList):
    global general
    if len(hashList) == 1:
        pedro = nodito(hashList[0])
        return  pedro
    newHashList = []
    # Process pairs. For odd length, the last is skipped
    for i in range(0, len(hashList)-1, 2):
        print(i)
        print(i+1)
        print("__")
        newHashList.append(hash2(hashList[i], hashList[i+1]))
        general+=f'\n\"{str(hashList[i])}\" -> \"{str(newHashList[-1])}\"'
        general+=f'\n\"{str(hashList[i+1])}\" -> \"{str(newHashList[-1])}\"'
    if len(hashList) % 2 == 1: # odd, hash last item twice
        newHashList.append(hash2(hashList[-1], hashList[-1]))
        general+=f'\n\"{str(hashList[-1])}\" -> \"{str(newHashList[-1])}\"'
    return merkle(newHashList)

def hash2(a, b):
    # Reverse inputs before and after hashing
    # due to big-endian / little-endian nonsense
    a1 = a
    b1 = b
    h = pedro.generate_hash(str(a1)+str(b1)).hex()
    return h

# https://blockexplorer.com/rawblock/0000000000000000e067a478024addfecdc93628978aa52d91fabd4292982a50
txHashes = [
  "00baf6626abc2df808da36a518c69f09b0d2ed0a79421ccfde4f559d2e42128b",
  "91c5e9f288437262f218c60f986e8bc10fb35ab3b9f6de477ff0eb554da89dea",
  "46685c94b82b84fa05b6a0f36de6ff46475520113d5cb8c6fb060e043a0dbc5c",
  "ba7ed2544c78ad793ef5bb0ebe0b1c62e8eb9404691165ffcb08662d1733d7a8",
  "b8dc1b7b7ed847c3595e7b02dbd7372aa221756b718c5f2943c75654faf48589",
  "25074ef168a061fcc8663b4554a31b617683abc33b72d2e2834f9329c93f8214",
  "0fb8e311bffffadc6dc4928d7da9e142951d3ba726c8bde2cf1489b62fb9ebc5",
  "c67c79204e681c8bb453195db8ca7d61d4692f0098514ca198ccfd1b59dbcee3",
  "bd27570a6cbd8ad026bfdb8909fdae9321788f0643dea195f39cd84a60a1901b",
  "41a06e53ffc5108358ddcec05b029763d714ae9f33c5403735e8dee78027fe74",
  "cc2696b44cb07612c316f24c07092956f7d8b6e0d48f758572e0d611d1da6fb9",
  "8fc508772c60ace7bfeb3f5f3a507659285ea6f351ac0474a0a9710c7673d4fd",
  "62fed508c095446d971580099f976428fc069f32e966a40a991953b798b28684",
  "928eadbc39196b95147416eedf6f635dcff818916da65419904df8fde977d5db",

]		
t = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]


nodo = merkle(txHashes)
general+=f'\n\"{merkle(txHashes).value}\"[fillcolor="pink"] \n{"}"}'
print(general)