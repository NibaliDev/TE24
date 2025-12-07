# Escape-sekvenser och råsträngar i Python

I Python används **escape-sekvenser** för att representera specialtecken i strängar, t.ex. ny rad `\n` eller backslash `\\`. Om du vill skriva en sträng **bokstavligt utan att Python tolkar backslash** kan du använda en **råsträng** (prefix `r`).

---

## 1. Exempel med backslash


stig = "C:\\Users\\Melissa\\Dokument"
print(stig)

"\\ " används för att representera ett faktiskt backslash-tecken.

Utan dubbla backslash skulle Python tolka \U eller \D som escape-sekvens, vilket ger fel.

Output:

C:\Users\Melissa\Dokument

# 2. Råsträng med prefix r

rå = r"C:\Users\Melissa\Dokument"
print(rå)

Prefixet r betyder rå sträng → Python tolkar inga escape-sekvenser.

Backslash används bokstavligt.

Output:

C:\Users\Melissa\Dokument

Fördelen: du behöver inte dubbla backslash, vilket är smidigare för filvägar och regex.

# 3. Escape-sekvenser för specialtecken

print("Rad1\nRad2")

\n betyder ny rad.

Output:

Rad1
Rad2

# Kort sagt:

Använd \\ i vanliga strängar för backslash

Använd r"..." för råsträngar

Escape-sekvenser som \n, \t, \r fungerar i vanliga strängar
