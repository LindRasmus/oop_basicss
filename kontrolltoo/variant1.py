def inimeste_arv():
    naiskondade_arv = 0
    tugiisikute_arv = 0
    for tugiisikute_arv in ok:
        if tugiisikute_arv < 15:
            tugiisikute_arv = 10
        else:
            tugiisikute_arv = 8
        return tugiisikute_arv

failinimi = str(input("Sisestage failinimi(see on naiskonnad.txt): "))
fail = open(failinimi, encoding="UTF-8")
sisu = fail.readlines()
naiskondade_arv = [int(x) for x in sisu]
osalenud = [int(x) for x in sisu]
if int(osalenud[0]) < 15:
    tugiisikute_arv = 10
else:
    tugiisikute_arv = 8
if int(osalenud[1]) < 15:
    tugiisikute_arv1 = 10
else:
    tugiisikute_arv1 = 8
if int(osalenud[2]) < 15:
    tugiisikute_arv2 = 10
else:
    tugiisikute_arv2 = 8
if int(osalenud[3]) < 15:
    tugiisikute_arv3 = 10
else:
    tugiisikute_arv3 = 8
if int(osalenud[4]) < 15:
    tugiisikute_arv4 = 10
else:
    tugiisikute_arv4 = 8
if int(osalenud[5]) < 15:
    tugiisikute_arv5 = 10
else:
    tugiisikute_arv5 = 8
if int(osalenud[6]) < 15:
    tugiisikute_arv6 = 10
else:
    tugiisikute_arv6 = 8
fail.close()

inimeste_arv = naiskondade_arv[0] * (22 + tugiisikute_arv)
inimeste_arv1 = naiskondade_arv[1] * (22 + tugiisikute_arv1)
inimeste_arv2 = naiskondade_arv[2] * (22 + tugiisikute_arv2)
inimeste_arv3 = naiskondade_arv[3] * (22 + tugiisikute_arv3)
inimeste_arv4 = naiskondade_arv[4] * (22 + tugiisikute_arv4)
inimeste_arv5 = naiskondade_arv[5] * (22 + tugiisikute_arv5)
inimeste_arv6 = naiskondade_arv[6] * (22 + tugiisikute_arv6)
kokku = inimeste_arv + inimeste_arv1 + inimeste_arv2 + inimeste_arv3 + inimeste_arv4 + inimeste_arv5 + inimeste_arv6


print("Turniiril oli inimesi: " + str(inimeste_arv))
print("Turniiril oli inimesi: " + str(inimeste_arv1))
print("Turniiril oli inimesi: " + str(inimeste_arv2))
print("Turniiril oli inimesi: " + str(inimeste_arv3))
print("Turniiril oli inimesi: " + str(inimeste_arv4))
print("Turniiril oli inimesi: " + str(inimeste_arv5))
print("Turniiril oli inimesi: " + str(inimeste_arv6))
print("Kokku oli kõigil turniiridel inimesi: " + str(kokku))
input()
