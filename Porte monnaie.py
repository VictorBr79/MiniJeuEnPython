import os


def main():
    print("Avant de commencer je vais vous expliquer les règles du jeu. "
          "Le but du jeu c'est de finir le jeu sans etre pauvre. "
          "Vous allez devoir entrer des prix (chiffres) mais vous ne pourrez pas entrer des nombres a virgule. "
          "Voila c'est parti!")
    os.system("PAUSE")
    print("Dans votre porte monnaie vous avez actuellement 1000 euros!")
    prm = int(input("Vous entrez dans le H&M, combiez depansez vous? : "))
    if prm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = 1000 - prm
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    print("Il ne vous reste plus que " + str(prt) + "€.")
    dxm = int(input("Vous entrez maintenant dans le Media Markt. Combien depensez vous? : "))
    if dxm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - dxm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    trm = int(input("Vous entrez maintenant dans le Delhaize. Combien depensez vous? : "))
    if trm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - trm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    qtm = int(input("Vous allez maintenant manger dans un restaurant. Combien depensez vous? : "))
    if qtm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - qtm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    sqm = int(input("Vous entrez maintenant dans une boulangerie. Combien depensez vous? : "))
    if sqm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - sqm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    print("Jour de paye! Vous recevez votre salaire qui est de 500 euros.")
    prt = prt + 500
    print("vous avez maintenant " + str(prt) + "€.")
    sxm = int(input("Vous entrez dans un night shop, combiez depansez vous? : "))
    if sxm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - sxm
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    print("Il ne vous reste plus que " + str(prt) + "€.")
    stm = int(input("Vous entrez maintenant dans le Colruyt. Combien depensez vous? : "))
    if stm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - stm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    htm = int(input("Vous entrez maintenant chez Samsung. Combien depensez vous? : "))
    if htm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - htm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    nvm = int(input("Vous allez maintenant manger au McDonald's. Combien depensez vous? : "))
    if nvm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - nvm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    dxm = int(input("Vous allez maintenant chez un docteur. Combien depensez vous? : "))
    if dxm <= 0:
        print("Vous n'avez rien depensez. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    if prt <= 0:
        print("Vous n'avez plus d'argent. Vous ètes mort.")
        os.system("PAUSE")
        exit()
    prt = prt - dxm
    print("Il ne vous reste plus que " + str(prt) + "€.")
    print("Jour de paye! Vous recevez votre salaire qui est de 500 euro.")
    prt = prt + 500
    print("vous avez maintenant " + str(prt) + "€.")
    print("Vous avez réussi le jeu sans etre pauvre!")
    print("Merci d'avoir jouer!")


if __name__ == '__main__':
    main()


os.system("PAUSE")
