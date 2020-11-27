from random import*
#https://docs.google.com/document/d/1CtQ28_5EbubqkQx8SyDfMNdcTejZ4NYBTpWc4KLkUrI/edit
inutile=""
stop=0
def menu():
    print("Bienvenue dans Emperor !")
    print("1-Jouer")
    print("2-Règles")
    choixjouer=input("---------------------------------- ")
    if choixjouer=="2":
        print("Dans Emperor, vous incarnez un empereur romain.")
        print("Vous ferez face à des choix qui influeront sur votre argent, votre influence, votre peuple et la puissance de votre armée.")
        print("Faites votre choix en entrant 1 ou 2. Entrer autre chose vous fera choisir 1.")
        print("Lorsqu'un domaine atteint 0 ou 100, vous perdez la partie.")
        print("Bonne chance")
        input("Appuyez sur entrée pour continuer")
        print("----------------------------------")
        menu()
menu()
peuple=50
argent=50
armee=50
influence=50
annee=-44
reine=-1
chefgaulois=0
nom=input("Entrez votre nom d'Empereur : ")
champignoninverse=0
sourd=0
toursreine=0
toursespion=0
tourschefgarde=0
gardecorps=0
toursoracle=0
tourschefgaulois=0
jesus=0
resultat=""
while 100>peuple>0 and 100>armee>0 and 100>argent>0 and 100>influence>0:
    event=""
    randomevent=randint(1,4)
    if champignoninverse!=0 :
        champignoninverse=champignoninverse-1
    if sourd!=0 :
        sourd=sourd-1
    if toursreine!=0 :
        toursreine=toursreine-1
    if toursespion!=0 :
        toursespion=toursespion-1
#Evenement1 : Rencontre de la reine
    if annee==-1 :
        event="Un enfant bénit va naître d’ici peu à Bethléem !"
        reponse1event="1-J'y envoie de suite l'armée."
        reponse2event="2-Fantastique !"
        replique1event="Seigneur, pardonnez notre empereur !"
        replique2event="Vous assisterez bientot à des miracles..."
        def consequence1event():
            global peuple,armee,argent,influence
            argent=argent+10
            resultat="Après avoir arrété l'enfant, votre armée a croisé trois vieillards et a pris leurs biens."
        def consequence2event():
            global peuple,armee,argent,influence,jesus
            jesus=jesus+1
            resultat="Des rumeurs commencerent a circuler sur un enfant divin..."
    elif randomevent==1 and reine==-1 and champignoninverse==0 and sourd==0  :
        print("----------------------------------")
        print("Année : ",annee," / Argent : ",argent," / Peuple : ",peuple," / Armée : ",armee," / Influence : ",influence)
        print("Explorateur : Une fameuse Reine egyptienne veut vous rencontrer !")
        print("1-Ammenez la ici.")
        print("2-Cela ne m'interesse pas.")
        choix=input("")
        if choix!="2" :
            reine=0
        else :
            print("Vous n'entendrez plus jamais parler de cette reine.")
            reine=-2
        annee=annee+1
    elif reine==0 :
        print("----------------------------------")
        print("Année : ",annee," / Argent : ",argent," / Peuple : ",peuple," / Armée : ",armee," / Influence : ",influence)
        print("Reine : Bonjour Empereur ",nom,". Comme le disaient les rumeurs, votre beauté est sans égal, c'est pourquoi je voudrais entretenir une liaison particulière avec vous...")
        print("1-Bien, voyons nous ce soir !")
        print("2-Je ne suis pas intéressé par ce genre de relations.")
        choix=input("")
        if choix=="2" :
            reine=reine+1
            print("Bien...")
        elif choix!="2":
            reine=-2
            print(";)")
        annee=annee+1
#Evenement2 : Rencontre du chef gaulois
    elif randomevent==2 and chefgaulois==0 and champignoninverse==0 and sourd==0 and tourschefgaulois==0:
        tourschefgaulois=3
        print("----------------------------------")
        print("Année : ",annee," / Argent : ",argent," / Peuple : ",peuple," / Armée : ",armee," / Influence : ",influence)
        print("Chef de l'armée : Le chef des gaulois veut vous voir.")
        print("1-Qu'est-ce qu'il me veut ?")
        print("2-Ce peuple inférieur ne m'interesse pas.")
        choix=input("")
        if choix!="2" :
            print("Chef gaulois : Bonjour Empereur ",nom,", je viens vous demander la permission de m'installer dans Rome. Je ne vous causerai evidemment aucun soucis !")
            print("1-D'accord, installez vous donc ici.")
            print("2-Non, retournez dans votre pays.")
            choixgaulois=input("")
            if choixgaulois!="2" :
                print("Chef gaulois : Je vous remercie pour votre acceuil !")
                chefgaulois=1
            else :
                print("Chef gaulois : D'accord...")
                chefgaulois=-1

        annee=annee+1
#Evenement3 : Pack Reine egyptienne
    elif randomevent==3 and reine==1 and toursreine==0 :
        personnage="Reine :"
        toursreine=3
        randomreine=randint(1,8)
        if randomreine==1 :
            event="Reine : Mettez de Côté votre poste et venez passer une journée avec moi !"
            reponse1event="1-D'accord"
            reponse2event="2-Désolé, j'ai beaucoup de travail."
            replique1event="Super ;)"
            replique2event="Une autre fois peut-être..."
            def consequence1event():
                global peuple,armee,argent,influence
                armee,peuple=armee-15,peuple+10
            def consequence2event():
                global peuple,armee,argent,influence
                armee,peuple=armee+10,peuple-10,3
        elif randomreine==2 :
            event="Puis-je faire venir mon peuple d’Égypte ici ?"
            reponse1event="Oui, faites le donc venir ici !"
            reponse2event="Non, votre peuple restera la où il est."
            replique1event="Merci beaucoup !"
            replique2event="D'accord, je comprends..."
            def consequence1event() :
                global peuple,armee,argent,influence
                peuple,influence=peuple+25,influence-25
            def consequence2event() :
                global peuple,armee,argent,influence
                peuple,influence=peuple-5,influence+10
        elif randomreine==3 :
            event="Vous avez besoin d’aide pour garder votre royaume en ordre, je vais faire venir mes gardes à Rome."
            reponse1event="Oui, je n’arrive plus à le contrôler..."
            reponse2event="Non, j'arrive a gérer mon peuple seul."
            replique1event="Bien, mais ne venez pas vous plaindre ensuite..."
            replique2event="Parfait, ils arriveront dans quelques semaine."
            def consequence1event() :
                global peuple,armee,argent,influence
                peuple,influence,armee=peuple-10,influence-15,armée+20
            def consequence2event() :
                global peuple,armee,argent,influence
                peuple,influence,armee=peuple+10,influence+10,armée-15
        elif randomreine==4 :
            event="Je doit faire un choix d’une haute importance : retourner en égypte ou rester à Rome."
            reponse1event="Rentrez donc dans votre pays."
            reponse2event="Restez avec moi ma chère."
            replique1event="C'est ce que je comptais faire de toute façon. *Vous ne reverez plus jamais cette femme*"
            replique2event="Comment pourrai-je vous quitter..."
            def consequence1event() :
                global peuple,armee,argent,influence
                peuple,legion,influence,armee,reine=peuple-5,legion-5,influence-5,armee-5,reine-3
            def consequence2event() :
                global peuple,armee,argent,influence
                peuple,legion,influence,armee=peuple+5,legion+5,influence+5,armee+5
        elif randomreine==5 :
            event="J’ai une annonce annonce à vous faire... Je veux vous épouser !"
            reponse1event="1-D’accord, marions nous !"
            reponse2event="2-Desolé, je ne suis pas encore pret."
            replique1event="Je suis si heureuse !"
            replique2event="Je comprend, ma demande était brusque..."
            def consequence1event() :
                global peuple,armee,argent,influence
                peuple=peuple+15
            def consequence2event() :
                global peuple,armee,argent,influence
                influence=influence+15
        elif randomreine==6 :
            event="Qui est donc cette autre femme que vous frequentez ?"
            reponse1event="1-Une amie."
            reponse2event="2-Euh..."
            replique1event="Cela me rassure !"
            replique2event="J'en etait sûre ! *Elle rentra en Egypte*"
            def consequence1event() :
                peuple=peuple+5
            def consequence2event() :
                peuple,reine=peuple-5,reine-3
        elif randomreine==7 :
            event="Mon peuple est assiégé donner moi votre puissance militaire !"
            reponse1event="1-Soldats, aidez cette femme !"
            reponse2event="2-Non, elle est déja bien assez occupée."
            replique1event="Merci beaucoup !"
            replique2event="Je comprends..."
            def consequence1event() :
                global peuple,armee,argent,influence
                armee,influence=armee-15,influence+15
            def consequence2event() :
                global peuple,armee,argent,influence
                armee,influence=armee+15,peuple-15
        elif randomreine==8 :
            event="C’est bientôt l’anniversaire de notre rencontre et je vous ai acheté un petit quelque chose !"
            reponse1event="1-Oui, moi aussi..."
            reponse2event="2-J'avais complètement oublié !"
            replique1event="Comme c'est gentil !"
            replique2event="Je compte si peu que ça pour vous ?!"
            def consequence1event() :
                global peuple,armee,argent,influence
                argent,peuple=argent-15,peuple+5
            def consequence2event() :
                global peuple,armee,argent,influence
                argent,peuple=argent+15,peuple-10
#Pack Espion, plusieurs events comportent un facteur chance
    elif randomevent==4 and toursespion==0 :
        personnage="Espion :"
        toursespion=3
        randomespion=randint(1,7)
        if randomespion==1 :
            event="J’ai vu un habitant faire de grand gestes et parler dans une langue étrangère, dois-je m’en soucier ?"
            reponse1event="1-Abattez le"
            reponse2event="2-Laissez le tranquille"
            replique1event="Bien."
            replique2event="Bien."
            randomvillageoisfou=randint(1,2)
            if randomvillageoisfou==1 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    peuple,influence,armee=peuple+5,influence+5,armee+5
                    resultat="Il était bel et bien fou, et tous les citoyens se réjouirent de sa mort."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    peuple,influence,armee=peuple-5,influence-5,armee-5
                    resultat="Il continua d'embêter les autres habitants durant des mois."
            elif randomvillageoisfou==2 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    peuple,influence,armee=peuple-5,influence-5,armee-5
                    resultat="Le meurtre d'un innocent fit grand bruit dans la ville."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    resultat="On n'entendit plus parler de cet étrange persone."
        elif randomespion==2 :
            event="Des habitants se sont rassemblés et effraient la population, que faire ?"
            reponse1event="1-Montrons leur qui est l'Empereur !"
            reponse2event="2-Laissons les..."
            replique1event="Bien."
            replique2event="Bien."
            randomgang=randint(1,2)
            if randomgang==1 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    peuple,influence,armee=peuple-10,influence-10,armee-5
                    resultat="Martyriser de jeunes enfants n'était peut-être pas la meilleure solution..."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    resultat="Ce n'était que des enfants qui jouaient."
            elif randomgang==2 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    peuple,influence=peuple+10,influence+10
                    resultat="L'arrestation de ces grands criminels ajouta un nouvel exploit a votre grand palmares."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    peuple,influence,armee,argent=peuple-5,influence-10,armee-5,argent-5
                    resultat="Cette bande de brigands fit par la suite de grands degats dans la ville."
        elif randomespion==3 :
            event="Je pense que des habitants magnigancent quelquechose d'étrange, dois-je m'en soucier ?"
            reponse1event="1-Arretez les !"
            reponse2event="2-Non, ils ne font rien de mal."
            replique1event="Bien."
            replique2event="Bien."
            randommagnigance=randint(1,3)
            if randommagnigance==3 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    peuple,armee,influence,argent=peuple+5,armee+5,influence+5,argent+5
                    resultat="Ces habitants allaient tenter de prendre le pouvoir."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    peuple,armee,influence,argent=peuple-5,armee-5,influence-5,argent-5
                    resultat="Ces habitants ont par la suite tentés de prendre le pouvoir, ce qui a occasionné quelques pertes."
            else :
                def consequence1event():
                    global peuple,armee,argent,influence
                    peuple=peuple+5
                    armee,influence,argent=armee+5,influence+5,argent+5
                    resultat="Ces habitants essayaient de créer un plat inedit, et l'espion les y a bien aidé."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    peuple=peuple+5
                    resultat="Quelques temps après, les cuisiniers de la ville vous presentèrent un nouveau plat qu'ils avaient préparé en secret."
        elif randomespion==4 :
            event="J’ai repéré une faille dans la défense énemie, mais bien que très rentable en cas de réussite, attaquer demanderait beaucoup de troupes et d'argent."
            reponse1event="1-Attaquons immediatement !"
            reponse2event="2-Je ne pense pas que ce soit une bonne idée..."
            replique1event="Bien."
            replique2event="Bien."
            randomfaille=randint(1,2)
            if randomfaille==1 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    peuple,armee,argent,influence=peuple+20,armee+20,argent+20,influence+20
                    resultat="Cette victoire ecrasante restera dans les annales."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    resultat="Vous avez peut-être ratté l'occasion de gagner cette guerre..."
            elif randomfaille==2 :
                def consequence1event():
                    global peuple,armee,argent,influence
                    peuple,armee,argent,influence=peuple-20,armee-20,argent-20,influence-20
                    resultat="Malgré les moyens colossaux employés, vous avez subi une défaite ecrasante."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    resultat="Vous avez peut-être evitté une énorme défaite."
        elif randomespion==5 :
            event="Je trouve que je fais du très bon travail, serait-il possible d’avoir une augmentation ?"
            reponse1event="1-Oui."
            reponse2event="2-Non."
            replique1event="Merci beaucoup !"
            replique2event="Bien, veuillez excuser ma demande."
            def consequence1event() :
                global peuple,armee,argent,influence
                argent=argent-15
                resultat="Il ne merittait pas vraiment cet argent..."
            def consequence2event() :
                global peuple,armee,argent,influence
                resultat="Il ne merittait pas vraiment cet argent..."
        elif randomespion==6 :
            event="Certains consuls veulent se rebeller, que dois-je faire ?"
            reponse1event="1-Tue les."
            reponse2event="2-Tu te fais de fausses idées"
            replique1event="Bien."
            replique2event="Bien."
            randomconsuls=randint(1,2)
            if randomconsuls==1 and gardecorps!=0 :
                def consequence1event() :
                    global peuple,armee,argent,influence
                    resultat="Après enquete, beaucoup de hauts placés ont été arrétés pour trahison."
                def consequence2event() :
                    global peuple,armee,argent,influence
                    influence=0
            elif randomconsuls==2 :
                def consequence1event():
                    global peuple,armee,argent,influence
                    armee,influence=armee-5,influence-10
                    resultat="Ils preparaient seulement votre anniversaire surprise..."
                def consequence2event():
                    global peuple,armee,argent,influence
                    resultat="Rien d'étrange n'arriva."
        elif randomespion==7 :
            event="Je soupçonne un fermier de cacher une partie de ses récoltes pour ne pas payer les taxes, que faire ?"
            reponse1event="1-Prenons lui tous ce qu'il a !"
            reponse2event="2-Je ne pense pas qu'il cache grand chose..."
            replique1event="Bien."
            replique2event="Bien."
            def consequence1event() :
                global peuple,armee,argent,influence
                peuple,argent=peuple-15,argent+15
                resultat="Il ne cachait rien, mais ses nombreux biens vous ont rendu plus riche."
            def consequence2event() :
                global peuple,armee,argent,influence
                resultat="Rien ne se passa..."
#Pack Chef de la garde
    elif randomevent==5 and tourschefgarde==0:
        personnage="Chef de la garde :"
        tourschefgarde=3
        randomchefgarde=randint(1,7)
        if randomchefgarde==1 :
            event="Nos troupes n’ont pas assez d’équipement, aidez les en leur en procurant de nouveaux."
            reponse1event="1-Bien, vous aurez l'équipement que vous voulez."
            reponse2event="2-Vos armes sont assez bien pour ce que vous en faites."
            replique1event="Merci bien."
            replique2event="Ce sera peut être cause de futures défaites..."
            def consequence1event():
                global peuple,armee,argent,influence
                armee,argent=armee+15,argent-15
                resultat="Des armes en or n'étaient peut être pas necessaires pour combattre..."
            def consequence2event():
                global peuple,armee,argent,influence
                armee=armee-10
                resultat="Leurs équipements étaient vraiment abimés"
        elif randomchefgarde==2:
            event="Notre armée manque cruellement de soldats. Pouvez-vous inciter des habitants à rejoindre l’armée ?"
            reponse1event="1-Oui, nous allons enroler les jeunes."
            reponse2event="2-Vous avez deja 6000 hommes..."
            replique1event="Merci beaucoup, ces recrues ne seront pas gachées !"
            replique2event="On n'en a jamais assez voyons..."
            def consequence1event():
                global peuple,armee,argent,influence
                peuple,armee=peuple-15,armee+15
                resultat="Ces pauvres recrues furent blessées après avoir servi d'échelle humaine."
            def consequence2event():
                global peuple,armee,argent,influence
                armee=armee-10
                resultat="Vous avez evitté une catastrophe, mais votre armée était trop faible et a subbi de lourdes pertes."
        elif randomchefgarde==3:
            event="Puis-je devenir votre garde du corps attitré ?"
            reponse1event="1-Oui, je commençais justement a me sentir vulnerable..."
            reponse2event="2-Non, je n'en ai pas besoin."
            replique1event="Bien, je vous protègerait au peril de ma vie !"
            replique2event="Mais je ne veut que votre bien..."
            def consequence1event():
                global peuple,armee,argent,influence
                gardecorps,argent=1,argent-5
                resultat="Bien que peut utile, il vous evita quelques fois une blessure grave."
            def consequence2event():
                global peuple,armee,argent,influence
                resultat="Vous auriez parfois eu besoin de la protection d'un vaillant guerrier..."
        elif randomchefgarde==4 :
            event="Les soldats n’ont rien à faire, voulez-vous qu’ils aident les gens du village ?"
            reponse1event="1-Oui, faites donc."
            reponse2event="2-Non, on ne sait jamais quand l'ennemi peut arriver..."
            replique1event="Bien."
            replique2event="Bien, nous nous remettons a nos postes."
            def consequence1event():
                global peuple,armee,argent,influence
                peuple=peuple+15
                resultat="Le peuple fut très heureux de recevoir un petit coup de main."
            def consequence2event():
                global peuple,armee,argent,influence
                peuple=peuple-10
                resultat="Les habitants avaient besoin d'aide et se sont effondrés sous les taches"
        elif randomchefgarde==5 :
            event="Nous avons intercepté un convoi ennemi, à qui devons nous donner les tresors ?"
            reponse1event="1-A moi."
            reponse2event="2-Au peuple."
            replique1event="Bien."
            replique2event="Bien."
            def consequence1event():
                global peuple,armee,argent,influence
                argent=argent+25
                resultat="Tous ces objets de valeur vous ont rendu très riche."
            def consequence2event():
                global peuple,armee,argent,influence
                peuple=peuple+25
                resultat="Les habitants furent très contents de ce cadeau."
        elif randomchefgarde==6 :
            event="Je pense que le village possède une faille énorme au niveau de ses défenses, voulez-vous que j’y remédie ?"
            reponse1event="Oui, faites donc..."
            reponse2event="Non, nous dépensons assez pour l'armée comme ça."
            replique1event="Merci !"
            replique2event="Bien..."
            def consequence1event():
                global peuple,armee,argent,influence
                argent,armee=argent-15,armee+5
                resultat="Il combla la petite faille et dépensa le reste en alcool. "
            def consequence2event():
                global peuple,armee,argent,influence
                armee=armee-15
                resultat="Cette petite faille fut exploitée par l'ennemi et l'armee subit beaucoup de pertes."
        elif randomchefgarde==7 :
            event="Nous avons capturés un soldat ennemi, que dois-je lui faire ?"
            reponse1event="Torturez le."
            reponse2event="Laissez le partir, seul leur dirigeant m'interesse."
            replique1event="Bien !"
            replique2event="Nous aurions pu en tirer quelquechose..."
            def consequence1event():
                global peuple,armee,argent,influence
                armee,influence,peuple=armee+10,influence+10,peuple-15
                resultat="Les informations tirées de ce pauvre homme ont été utiles, mais le peuple fut choqué par la violance des actes."
            def consequence2event():
                global peuple,armee,argent,influence
                peuple=peuple+15
                resultat="Il vous fut reconnaissant de l'avoir liberé et aida les habitants dans leurs travaux."
        elif randomchefgarde==7 :
            event="Les agriculteurs s’étalent de plus en plus sur notre terrain d’entrainement."
            reponse1event="Faites les donc reculer !"
            reponse2event="L'agriculture prime sur le militaire."
            replique1event="C'est bien ce que je comptais faire !"
            replique2event="Mais..."
            def consequence1event():
                global peuple,armee,argent,influence
                armee,peuple=armee+10,peuple-10
                resultat="Certains agriculteur perdirent foi en vous."
            def consequence2event():
                global peuple,armee,argent,influence
                armee,peuple=armee-10,peuple+10
                resultat="Vos soldats continuerent de s'entrainer sur ce minuscule terrain."
#Pack Oracle
    elif randomevent==4 and toursoracle==0 :
        personnage="Oracle :"
        toursoracle=3
        randomoracle=randint(1,3)
        if randomoracle==1 :
            event="J’ai eu une vision cette nuit, votre peuple est en danger et vous devez fortifier la ville !"
            reponse1event="1-Vous avez raison, construisons des murs !"
            reponse2event="2-Nous somme deja bien à l'abri !"
            replique1event="Oui !"
            replique2event="Ma vision était pourtant très réaliste... "
            def consequence1event():
                global peuple,armee,argent,influence
                argent,peuple=argent-10,peuple+10
                resultat="Le peuple n'était pas vraiment en danger, mais il fut rassuré par ces murs.")
            def consequence2event():
                global peuple,armee,argent,influence
                peuple=peuple-15
                resultat="Après avoir quitté la salle, il alla racconter a tout le monde son reve, ce qui terrifia le peuple durant des jours.")
        elif randomoracle==2 :
            event="Un consul m’a manqué de respect et m’a dit que je devrais être emprisonné car un humain ne peut pas avoir des visions."
            reponse1event="1-Il a raison. GARDES !"
            reponse2event="2-Laissez le, il n'y comprend rien."
            replique1event="אני מקלל אותך"
            replique2event="Vous êtes un homme bon."
            def consequence1event():
                global peuple,armee,argent,influence
                influence,sourd=influence+10,sourd+6
                resultat="Peu de temps après, votre ouïe devenut defaillante."
            def consequence2event():
                global peuple,armee,argent,influence
                influence=influence-15
        elif randomoracle==3 :
            event="Je dois vous emmener à un endroit sacré, venez avec moi !"
            reponse1event="1-Tous avec moi !"
            reponse2event="2-Non, vous êtes bien trop étrange."
            replique1event="Super !"
            replique2event="Ce lieu saint est pourtant bien réel..."
            randomlieusaint=randint(1,3)
            if randomlieusaint==1 :
                def consequence1event():
                    global peuple,armee,argent,influence
                    argent=argent+20
                    resultat="Il vous emmena dans une grotte pleine d'or."
                def consequence2event():
                    global peuple,armee,argent,influence
                    peuple=peuple+10
                    resultat="Le peuple fut heureux de voir que son chef ne sombre pas dans des choses absurdes."
            else :
                def consequence1event():
                    global peuple,armee,argent,influence
                    peuple,influence=peuple-5,influence-10
                    resultat="Il n'y avait rien et beaucoup de gens perdirent foi en vous."
                def consequence2event():
                    global peuple,armee,argent,influence
                    peuple=peuple+10
                    resultat="Le peuple fut heureux de voir que son chef ne sombre pas dans des choses absurdes."
        elif randomoracle==4 :
            event=""
            reponse1event="1-"
            reponse2event="2-"
            replique1event=""
            replique2event=""
            def consequence1event():
                global peuple,armee,argent,influence
                influence,sourd=influence+10,sourd+6
                resultat=""
            def consequence2event():
                global peuple,armee,argent,influence
                influence=influence-15
                resultat=""
        elif randomoracle==5 :
            event=""
            reponse1event="1-"
            reponse2event="2-"
            replique1event=""
            replique2event=""
            def consequence1event():
                global peuple,armee,argent,influence
                influence,sourd=influence+10,sourd+6
                resultat=""
            def consequence2event():
                global peuple,armee,argent,influence
                influence=influence-15
                resultat=""

    #Print des evenements et des reponses (J'ai fait ça pour pouvoir faire le champignon qui inverse les questions et la surdité)
    if event!="" :
        print("----------------------------------")
        print("Année : ",annee," / Argent : ",argent," / Peuple : ",peuple," / Armée : ",armee," / Influence : ",influence)
        print("")
        print(personnage)
        if champignoninverse!=0 :
            lenevent=len(event)
            lenreplique1=len(replique1event)
            lenreplique2=len(replique2event)
            replique1inverse=""
            replique2inverse=""
            eventinverse=""
            for i in range(lenevent,0,-1):
                l=event[i-1]
                eventinverse=eventinverse+l
            for i in range(lenreplique1,0,-1):
                l=replique1event[i-1]
                replique1inverse=replique1inverse+l
            for i in range(lenreplique2,0,-1):
                l=replique2event[i-1]
                replique2inverse=replique2inverse+l
            print(eventinverse)
            print(reponse1event)
            print(reponse2event)
            choix=input("")
            if choix!="2" :
                print(replique1inverse)
                consequence1event()
                print(resultat)
            elif choix=="2" :
                print(replique2inverse)
                consequence2event()
                print(resultat)

        elif sourd!=0 :
            lenevent=len(event)
            lenreplique1=len(replique1event)
            lenreplique2=len(replique2event)
            replique1sourd=""
            replique2sourd=""
            eventsourd=""
            for i in event :
                rand=randint(1,3)
                if rand==3 :
                    eventsourd=eventsourd+" "
                else :
                    eventsourd=eventsourd+i
            print(eventsourd)
            print(reponse1event)
            print(reponse2event)
            choix=input("")
            if choix!="2":
                print(replique1sourd)
                consequence1event()
                print(resultat)

            elif choix=="2":
                print(replique2sourd)
                consequence2event()
                print(resultat)
        else :
            print(event)
            print(reponse1event)
            print(reponse2event)
            choix=input("")
            if choix!="2":
                print(replique1event)
                consequence1event()
                print(resultat)
            elif choix=="2":
                print(replique2event)
                consequence2event()
                print(resultat)
        annee=annee+1
if peuple<=0 :
    print("Affamé et ruiné, les habitants vous firent executer.")
elif armee<=0 :
    print("Votre armée, trop faible, ne sut defendre la ville contre les ataques de l'ennemi.")
elif argent<=0 :
    print("Ruiné, vous avez été ejecté par les plus riches.")
elif influence<=0 :
    print("Un senateur ayant perdu foi en vous, il vous assasina lachement avec un poignard.")










