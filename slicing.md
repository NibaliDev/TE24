#Slicing – Enkel Mall
sekvens[start:stop:steg]

#Betydelse:

start = index där slicing börjar (inkluderas)

stop = index där slicing slutar (exkluderas)

steg = hur många steg du hoppar varje gång

Alla tre delar är valfria.

#Snabbguide med exempel
1. Standard – ta från start till före stop
a[2:5]


Tar index 2, 3, 4.

#2. Utelämna start → börjar från början
a[:4]

#3. Utelämna stop → går till slutet
a[3:]

#4. Utelämna båda → kopiera listan
a[:]

#5. Använd steg
a[::2]   # varannan
a[::3]   # var tredje

#6. Negativt steg → baklänges
a[::-1]  # vänd hela
a[5:2:-1]  # baklänges mellan index 5 och 3

#Superkort mall att memorera
[start : stop : steg]


Tomt värde betyder “standard”

stop är exklusivt

steg kan vara negativt för baklänges
