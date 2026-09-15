# Gabriel Perroud
# Veterinaire
# 2026-09-15


#Interface des Information

Titre = "INFORMATION SUR LE SPÉCIMEN"
Tiret = "-"

print(f"{Titre:-^60}")
print(f"")
Nom = str(input("Nom de l'animal : "))
Espèce = int(input("Espèce de l'animal (1 = requin, 2 = tigre, 3 = gnou) : "))
Âge = int(input("Âge de l'animal (en mois) : "))
Masse = float(input("Masse de l'animal (en livres) : "))
Température =  float(input("Tempéraure corporelle de l'animal (en °F) : "))
print(f"")
print(f"{Tiret:-^60}")
print(f"")

#Conversion des donnée

Kilogrammes = (Masse * 0.453592)
Celsius = ((Température - 32) * 0.555555556)

#IF et ELSE et MATCH Température/Masse

match Espèce:
    case 1:
        Type_espèce = "requin"
        if Celsius >= 22.0:
            Température_C = "Bonne"
            if Celsius <= 26.0:
                Température_C = "Bonne"
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= 60.0:
            Poid = "Bon"
            if Kilogrammes <= 150.0:
                Poid = "Bon"
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"


    case 2:
        Type_espèce = "tigre"
        if Celsius >= 37.5:
            Température_C = "Bonne"
            if Celsius <= 39.0:
                Température_C = "Bonne"
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= 100.0:
            Poid = "Bon"
            if Kilogrammes <= 260.0:
                Poid = "Bon"
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"

    case 3:
        Type_espèce = "gnou"
        if Celsius >= 37.5:
            Température_C = "Bonne"
            if Celsius <= 39.0:
                Température_C = "Bonne"
            else:
                Température_C = "Mauvaise"
        else:
            Température_C = "Mauvaise"
        if Kilogrammes >= 120.0:
            Poid = "Bon"
            if Kilogrammes <= 2700.0:
                Poid = "Bon"
            else:
                Poid = "Mauvais"
        else:
            Poid = "Mauvais"

print(Type_espèce)
print(Température)
print(Masse)
print(Kilogrammes)
print(Celsius)
print(Température_C)
print(Poid)

#Interface des données

# LigneÉgal = "="
# Nom_Bâtiment = "CLINIQUE VÉTÉRINAIRE EXOTIQUE"
# Lieux_Bâtiment = "DES ÎLES ST-MAURICE"


# print(f"{LigneÉgal:=^60}")
# print(f"{Nom_Bâtiment:^60}")
# print(f"{Lieux_Bâtiment:^60}")
# print(f"{LigneÉgal:=^60}")
