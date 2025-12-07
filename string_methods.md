# Vanliga Strängmetoder i Python

Här är en översikt över de mest använda strängmetoderna, deras funktion och exempel.  

> **Notera:** Strängar är immutabla i Python. Alla metoder som ändrar innehållet **returnerar en ny sträng**. Den ursprungliga strängen förändras **inte** om man inte tilldelar resultatet till en variabel.

---

# 1. `.strip()`

**Funktion:** Tar bort mellanslag eller angivna tecken i början och slutet av strängen.  

**Exempel:**

s = "   hej världen   "
ny = s.strip()
print(ny)  # "hej världen"

# 2. .replace()

Funktion: Byter ut ett tecken eller en delsträng mot något annat. Returnerar en ny sträng.

Exempel:

text = "hej världen"
ny_text = text.replace("världen", "Python")
print(ny_text)  # "hej Python"

# 3. .count()

Funktion: Räknar hur många gånger ett tecken eller en delsträng förekommer.

Exempel:

s = "banan"
print(s.count("a"))  # 3

# 4. .endswith()

Funktion: Returnerar True om strängen slutar med en viss delsträng, annars False.

Exempel:

fil = "rapport.pdf"
print(fil.endswith(".pdf"))  # True

# 5. .startswith()

Funktion: Returnerar True om strängen börjar med en viss delsträng, annars False.

Exempel:

text = "Hej världen"
print(text.startswith("Hej"))  # True

# 6. .split()

Funktion: Delar en sträng i en lista baserat på ett avgränsningstecken (default = mellanslag).

Exempel:

s = "Hej världen Python"
ord_lista = s.split()
print(ord_lista)  # ["Hej", "världen", "Python"]

data = "äpple,banan,kiwi"
print(data.split(","))  # ["äpple", "banan", "kiwi"]

# 7. .join()

Funktion: Sätter ihop en lista till en sträng med en angiven separator.

Exempel:

ord_lista = ["Hej", "Python"]
text = " ".join(ord_lista)
print(text)  # "Hej Python"

text2 = "-".join(["2025", "12", "07"])
print(text2)  # "2025-12-07"

# `.find()` – Söka efter en delsträng i Python

**Funktion:**  
`.find()` används för att **hitta indexet** där en delsträng först förekommer i en sträng.  

- Returnerar indexet (ett heltal) för den första förekomsten.  
- Returnerar `-1` om delsträngen inte hittas.  
- Strängar är immutabla; metoden ändrar **inte** originalsträngen.

---

## Syntax

str.find(substring, start, end)

# isX-metoder
print("12345".isdigit()) 
print("abc".isalpha()) 
print("abc123".isalnum()) 
print(" \t\n".isspace())

# ⚠️ Viktigt att komma ihåg

Strängar är immutabla → metoder som .replace(), .strip(), .upper() etc. skapar nya strängar.

Den ursprungliga strängen förändras inte om du inte tilldelar resultatet till en variabel:

s = "hej världen"
s = s.replace("världen", "Python")  # måste tilldela nytt värde
