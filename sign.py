"""
Q2 (b) RSA digitally sign the file
name : saurabh chopra
student number: 250883097
this program will read the sign.txt which is the actual code and sign the data
it will also verify the signature and hash of data to be equal in the STDOUT it will print True

"""


def sign_data(data):
    '''
    param: data read from the file to be signed
    return: base64 encoded signature
    '''
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5 
    from Crypto.Hash import SHA256
    from Crypto.Util import asn1
    from base64 import b64encode, b64decode 
    #given by the prof n , e, d 
    n = 103923750583675917777452723084902275956322321347251369547198561741725160583083214244873468324950694356892627873520290850868687184677774313738345853731914172873201679734133922293223038318576487055717405740516986030705800665383388489578499651714083347835387576319528274700123545962228546255987411521556243948149
    # added long as it was throwing an exception
    e = long(65537)

    d = 17565091249452647225549595093023216057619090797007849313736034124434893324058360379487364521346397323516481360986683274410980788633530769996790469838235089550522885790106853124306578513977869050393094033637670437634572856174875038057195517551596745993052717984365235149738925687601660611790816608095661093629
    # generate public and private key
    key = RSA.construct((n,e,d))
    privatekey = key.exportKey()
    publickey = key.publickey().exportKey()
    print publickey
    print privatekey
    rsakey = RSA.importKey(privatekey) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new()
    digest.update(data)
    sign = signer.sign(digest) 
    # verify signature and hash of data are equal
    print  signer.verify(digest, sign)
    return b64encode(sign)

fileLocation = r'sign.txt'

inputFile = open(fileLocation, "r").read()

signature = sign_data(inputFile)
print signature     
