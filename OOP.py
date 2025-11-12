"""
Exempel på objektorienterad programmering (OOP)
"""

# I detta fall kallar vi klassen för "Bil". Bilen är ett klass som beskriver hur objekt med den klassen konmmer att se ut. 
# Det har egna tilldelade variabler och funktioner.
class Bil:
    def __init__(self, märke, modell, år):
        self.märke = märke
        self.modell = modell
        self.år = år
        self.hastighet = 0

    def starta(self):
        print(f"{self.märke} {self.modell} startar.")

    def gasa(self, ökning):
        self.hastighet += ökning
        print(f"Bilen kör nu i {self.hastighet} km/h.")

    def bromsa(self, minskning):
        self.hastighet = max(0, self.hastighet - minskning)
        print(f"Bilen saktar ner till {self.hastighet} km/h.")

# Skapa ett objekt (en instans av Bil)
min_bil = Bil("Volvo", "XC60", 2022)

# Använd metoderna
min_bil.starta()
min_bil.gasa(50)
min_bil.bromsa(20)
