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

# Escape-sekvenser i Python

Escape-sekvenser används för att representera specialtecken i strängar. De börjar med en backslash `\`. Python tolkar dem vid exekvering. Här är en komplett lista över de vanligaste escape-sekvenserna:

---

## 1. Nya rader och tabbar
| Escape-sekvens | Beskrivning | Exempel |
|----------------|------------|---------|
| `\n` | Ny rad | `"Rad1\nRad2"` → Rad1 (ny rad) Rad2 |
| `\r` | Carriage return (återställ till radens början) | `"Rad1\rRad2"` → skriver Rad2 över början av Rad1 |
| `\t` | Horisontell tab | `"Kol1\tKol2"` → Kol1   Kol2 |

---

## 2. Backslash och citattecken
| Escape-sekvens | Beskrivning | Exempel |
|----------------|------------|---------|
| `\\` | Backslash | `"C:\\Users"` → `C:\Users` |
| `\'` | Enkel citationstecken | `'It\'s ok'` → `It's ok` |
| `\"` | Dubbel citationstecken | `"She said \"Hello\""` → `She said "Hello"` |

---

## 3. Formatering och kontrolltecken
| Escape-sekvens | Beskrivning | Exempel |
|----------------|------------|---------|
| `\b` | Backspace | `"abc\b"` → tar bort c → `ab` |
| `\f` | Form feed (ny sida) | `"Hej\fVärlden"` |
| `\v` | Vertikal tab | `"Hej\vVärlden"` |

---

## 4. Unicode och teckenrepresentation
| Escape-sekvens | Beskrivning | Exempel |
|----------------|------------|---------|
| `\uxxxx` | 16-bit Unicode | `"\u00A9"` → `©` |
| `\Uxxxxxxxx` | 32-bit Unicode | `"\U0001F600"` → 😀 |
| `\N{name}` | Unicode-tecken via namn | `"\N{GRINNING FACE}"` → 😀 |
| `\xhh` | Hexadecimalt värde | `"\x41"` → `A` |
| `\ooo` | Oktalt värde | `"\101"` → `A` |

---

## 5. Råsträngar
- Prefix `r` eller `R` anger **råsträng** → inga escape-sekvenser tolkas.  
- Exempel:
```python
s = r"C:\Users\Melissa\Dokument"
print(s)  # C:\Users\Melissa\Dokument


# Kort sagt:

Använd \\ i vanliga strängar för backslash

Använd r"..." för råsträngar

Escape-sekvenser som \n, \t, \r fungerar i vanliga strängar
