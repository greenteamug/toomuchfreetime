def zahl_ausschreiben(zahl):
    if not isinstance(zahl, int) or zahl < 0:
        return "Bitte eine positive ganze Zahl eingeben."
    
    einheiten = ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    zehner = ["", "zehn", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
    besondere_zehner = ["zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
    
    if zahl == 0:
        return "null"
    elif zahl < 10:
        return einheiten[zahl]
    elif 10 <= zahl < 20:
        return besondere_zehner[zahl - 10]
    elif 20 <= zahl < 100:
        zehner_stelle = zahl // 10
        einer_stelle = zahl % 10
        if einer_stelle == 0:
            return zehner[zehner_stelle]
        else:
            return einheiten[einer_stelle] + "und" + zehner[zehner_stelle]
    elif 100 <= zahl < 1000:
        hunderter_stelle = zahl // 100
        rest = zahl % 100
        hunderter_text = "hundert" if hunderter_stelle == 1 else einheiten[hunderter_stelle] + "hundert"
        if rest == 0:
            return hunderter_text
        else:
            return hunderter_text + zahl_ausschreiben(rest)
    elif 1000 <= zahl < 1000000:
        tausender_stelle = zahl // 1000
        rest = zahl % 1000
        tausender_text = "tausend" if tausender_stelle == 1 else zahl_ausschreiben(tausender_stelle) + "tausend"
        if rest == 0:
            return tausender_text
        else:
            return tausender_text + zahl_ausschreiben(rest)
    else:
        return "Zahl zu groß für dieses Beispiel (max. 999.999)"

# Benutzereingabe
try:
    eingabe = int(input("Gib eine Zahl ein (0-999.999): "))
    print(zahl_ausschreiben(eingabe))
except ValueError:
    print("Bitte eine gültige ganze Zahl eingeben.")
