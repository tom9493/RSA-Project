import getRandomPrime

def modPower(g, a, p):
    result = 1  # Initialize result

    g = g % p

    if g == 0:
        return 0

    while a > 0:
        if (a & 1) == 1:
            result = (result * g) % p

        a = a >> 1  # a/2
        g = (g * g) % p

    return result


def gcd(p, q):
    while q:
        p, q = q, p % q

    return p


def extendedEA(x, y):
    if x % y == 0:
        return y, 0, 1
    else:
        gcd, s, t = extendedEA(y, x % y)
        s = s - ((x//y) * t)
        return gcd, t, s

def MI(e, t):
    gcd, a, b = extendedEA(e, t)
    if (gcd != 1):
        return None
    else:
        return a % t


if __name__ == '__main__':
    p = 10204253583040238527889904793013801980353796675507703578274264640536545763673475633904096835292125625627577997858550788351510423095334165389619077246921627
    q = 12054486474968531792422173227014291607191989795894392477720365099737215227349313093787564524262350826774241774061019464321157887376407978047957960538052619
    e = 65537
    t = (q - 1) * (p - 1)
    n = p * q
    print("n: ", n)
    d = MI(e, t)
    print("d: ", d)

    encryptM = 87745973471415865965480967078324613816029912872778799661173940080877570187878110464999342494200131053657577225714039885848430264245561051654278372334969790031032235417365845050659210029123605590035928264494673305484728916338364927717618941589767488047220684032751028555620999273804658535876073959575202975973
    decryptM = 79073459319943932885687118887863027818388815450461870393868919464528082488939145999518836463581818536659610676586011911113664339818697656948076932773057604226483976158804777545752430863578392045217671993142343214846938100165816304870710770974093313813779150933277217907946386334139855813820631631423018622255
    me = modPower(encryptM, e, n)
    print("me: ", me)
    md = modPower(decryptM, d, n)
    print("md: ", md)

    # This function to get p and q
    # while True:
    #     n = 512
    #     prime1 = getRandomPrime.getPrime(n)
    #     prime2 = getRandomPrime.getPrime(n)
    #     if not getRandomPrime.MRTest(prime1) and getRandomPrime.MRTest(prime2):
    #         continue
    #     else:
    #         print(n, "bit prime1 is: \n", prime1)
    #         print(prime1.__sizeof__())
    #         print(n, "bit prime2 is: \n", prime2)
    #         print(prime2.__sizeof__())
    #         break
    #
    # # Checks for p and q highest order bit set
    # print(bin(p))
    # print(bin(q))

    # Checks if (p-1)(q-1) is relatively prime to 65537 or e
    # gcd1 = gcd(t, e)
    # print(gcd1)
