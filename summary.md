🧠 Djupgående Sammanfattning av Kursmaterialet
==============================================

_enligt kursens fokusområden och provkrav_

Det är klokt att repetera grunderna, även med lång erfarenhet. Självlärda programmerare tenderar att hoppa direkt till effektiva inbyggda metoder, men i en introduktionskurs förväntas man kunna implementera logiken manuellt och följa kursens idiom.

Nedan följer en översikt i **välstrukturerat Markdown-format**, med fokus på de moment som kursen betonar mest.

1\. Grundläggande Programmering och Syntax
==========================================

Matematiska Operatorer
----------------------

Du ska behärska:

*   **Heltalsdivision:** //
    
*   **Restvärde (modulo):** %
    

Dessa ingår i många grundläggande övningar.

Input och Typkonvertering
-------------------------

*   input() returnerar **alltid en sträng**.
    
*   Typkonvertering krävs för beräkningar: int(), float().
    
*   Fel uppstår om användaren skriver text när en siffra förväntas. Detta är normalt i början.
    

Utskrift och Formatering (F-strängar)
-------------------------------------

Du behöver kunna:

*   **F-strängar**
    
*   Format-specifikationer, t.ex.
    
    *   :.1f — kontroll av decimaler/precision
        
    *   :10.2f — fältbredd + precision
        
*   **Debugging-syntaxen {x=}** (Python 3.8+)
    
*   Utskrift även **utan** f-strängar (testas i t.ex. uppgift 7).
    

2\. Datastrukturer
==================

A. Listor (Mutable Sequences)
-----------------------------

Egenskaper:

*   Muterbara
    
*   Metoder: .append(), .pop()
    
*   Tilldelning via index: a\[2\] = 9
    

### 🔥 Kritisk Punkt: Manuella Algoritmer

Du måste kunna implementera:

*   Hitta **minsta värde**
    
*   Hitta **största värde**
    
*   Beräkna **medelvärde**
    

**Utan** att använda min(), max(), eller sum().

### Slicing och Iteration

*   Delar av listan: x\[2:5\], x\[:3\], x\[::2\]
    
*   Kopiera lista: kop = a\[:\]
    
*   enumerate() för index + värde (kan starta på 1: start=1)
    

### Unika Värden (Bevara Ordning)

Du måste kunna algoritmen:

1.  Skapa en set för sedda element.
    
2.  Gå igenom listan och lägg till element i en ny lista **endast om de inte setts tidigare**.
    
3.  Ordningen ska bevaras.
    

B. Tuples (Immutable Sequences)
-------------------------------

Egenskaper:

*   **Immutable**: går inte att ändra efter skapande.
    
*   Försök att ändra ger fel.
    

Viktiga koncept:

*   x, y = p
    
*   a, b = b, a(använder tuple-packing internt)
    

C. Dictionaries (Key-Value Storage)
-----------------------------------

Egenskaper:

*   Nycklar är unika
    
*   Skapas med {}
    

### Viktiga Idiom

#### Säkert Uppslag – .get()

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   värde = dic.get(nyckel, "okänd")   `

Undviker KeyError.

#### Frekvensräkning – Get-mönstret

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   freq[t] = freq.get(t, 0) + 1   `

Standardmetod för counting.

#### zip() + dict()

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   par = list(zip(lista1, lista2))  d = dict(par)   `

#### Lista av Dictionaries

Kunna iterera och uppdatera värden, t.ex. höja allas poäng med 1.

3\. Strängar och Stränghantering
================================

Strängar är **immutabla**, likt tuples.

Viktiga koncept
---------------

### Immutabilitet i Praktiken

Följande fungerar **inte**:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   s[0] = "r"   `

Man måste konstruera en ny sträng:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   s = "r" + s[1:]   `

### Slicing för Baklängesvändning

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   s[::-1]   `

### Robust Jämförelse

Vid jämförelse för palindrom m.m. ska du använda:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   s.casefold()   `

mer robust än .lower().

### Metoder att kunna:

*   .strip()
    
*   .replace()
    
*   .count()
    
*   .endswith()
    
*   .startswith()
    
*   .split() / .join()
    

⭐ Sammanfattning: Extra Viktiga Punkter att Repetera
====================================================

1.  **Manuella Algoritmer**Implementera minsta, största, och medelvärde utan inbyggda funktioner.
    
2.  **Orderbevarande Dubblettborttagning**Använd set + list för att bevara ordningen.
    
3.  **Dictionary Idioms**Speciellt frekvensräkning med .get(key, 0) + 1.
    
4.  **Strängimmutabilitet**Du kan inte ändra ett tecken i en sträng — skapa en ny.
    

🎓 Avslutande kommentar
=======================

Se det som att lära sig att skriva för hand igen:Du _kan_ skriva snabbt med dator, men här måste du visa att du behärskar de exakta grundstegen — precis som kursen lär ut.
