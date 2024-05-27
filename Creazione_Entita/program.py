import os
if __name__ == "__main__":
    while True:
        campi = []
        tipiCampi = []
        scelta = input("Hai inserito i dati nell' input.txt?(se no li dovrai inserire nel terminale) (y/n): ")
        # variabili input
        if scelta.lower() == "y":
            f = open("input.txt", "r")
            prog = f.readline().replace("\n", "")
            entita = f.readline().replace("\n", "")
            entitaPlu = f.readline().replace("\n", "")
            nCam = f.readline().replace("\n", "")
            if(not nCam.isdigit()):
                print("La quarta riga del file input.txt non contiene un numero")
                break
            nCampi = int(nCam)
            for i in range(nCampi):
                riga = f.readline()
                temp = riga.split()
                tipiCampi.append(temp[0]) 
                campi.append(temp[1])
            f.close()
        else:
            prog = input("Nome progetto: ")
            entita = input("Nome entità (con la prima lettera maiuscola): ")
            entitaPlu = input("Nome entità al plurale (con la prima lettera maiuscola): ") 
            nCam = input("Numero campi: ")
            if(not nCam.isdigit()):
                print(nCam+" non è un numero")
                break
            nCampi = int(nCam)
            for i in range(nCampi):
                tipiCampi.append(input("Tipo campo "+ str(i+1)+ ": "))
                campi.append(input("Nome campo "+ str(i+1)+ ": "))

        # variabili 
        Dir = os.getcwd()
        DirP = Dir[:-16]
        DirP += "aspnet-core\\src\\"
        usi = "using "+prog+"."+entitaPlu+";"
        ns = "namespace "+prog+"."+entitaPlu+";"
        dto = entita+"Dto"
        Rep = "I"+entita+"Repository"
        rep = entita.lower()+"Repository"
        rep_ = "_"+rep
        campoZero = campi[0]
        Man = entita+"Manager"
        man = entita.lower()+"Manager"
        man_ = "_"+man
        #direttive
        domE = DirP+prog+".Domain\\"+entitaPlu
        dom_shaE = DirP+prog+".Domain.Shared\\"+entitaPlu
        appE = DirP+prog+".Application\\"+entitaPlu
        app_conE = DirP+prog+".Application.Contracts\\"+entitaPlu
        efcE = DirP+prog+".EntityFrameworkCore\\"+entitaPlu
        da_agg = Dir+"\\Da_Aggiungere"
        dom = da_agg+"\\Domain"
        efc = da_agg+"\\EntityFrameworkCore"
        dom_sha = da_agg+"\\Domain.Shared"
        app = da_agg+"\\Application"
        app_con = da_agg+"\\Application.Contracts"
        FE = da_agg+"\\Front_End"
        #funzioni utilizzate per la scrittura dei campi:
        def campiGet():
            cam = ""
            for i in range(nCampi):
                temp = tipiCampi[i]
                if "?" in temp:
                    temp = temp.replace("?", "")
                cam += ("    public "+temp+" "+campi[i]+" {get; set;}\n")
            return cam
        def campiPar():
            cam = ""
            for i in range(nCampi):
                cam+= tipiCampi[i]+" "+campi[i].lower()
                if i < nCampi-1:
                    cam += ", "
            return cam
        def campiPaNul():
            cam = ""
            for i in range(nCampi):
                cam+="        "+ tipiCampi[i]+" "+campi[i].lower()
                if "?" in tipiCampi[i]:
                    cam+= " = null"
                if i < nCampi-1:
                    cam+=",\n"
            return cam
        def campiCost():
            cam = ""
            for i in range(nCampi):
                if i == 0:
                    cam+= "        SetName("+campi[i].lower()+");\n"
                cam+="        " +campi[i]+" = "+campi[i].lower()+";\n"
            return cam
        def campiEle():
            cam = ""
            for i in range(nCampi):
                cam+="            " +campi[i].lower()
                if i < nCampi-1:
                    cam += ",\n"
            return cam
        def campiCreat():
            cam = ""
            for i in range(nCampi):
                if "?" not in tipiCampi[i] and i != 0 :
                    cam += "    [Required]\n"
                cam+="    public "+tipiCampi[i]+" "+campi[i]+" {get; set;}"
                if i == 0:
                    cam+= " = string.Empty;"
                cam+="\n"
            return cam
        def campiInp():
            cam = ""
            for i in range(nCampi):
                cam+="        input." +campi[i]
                if i < nCampi-1:
                    cam+=",\n"
            return cam
        def campiUpd():
            cam = ""
            for i in range(nCampi):
                if i != 0:
                    cam+="        "+entita.lower()+"."+campi[i]+" = input."+campi[i]+";\n"
            return cam
        def campiForm():
            cam = ""
            for i in range(nCampi):
                cam+="      "+campi[i].lower()+": [this.selected"+entita+"."+campi[i].lower()+" || ''"
                if "?" not in tipiCampi[i]:
                    cam+=", Validators.required"
                cam+="]"
                if i != nCampi-1:
                    cam+=",\n"
            return cam

        #funzione crezione file
        def crea(fil, path, nom):
            # leggi file
            stringa = leggi(fil)
            # apertura cartella
            os.chdir(path)
            # creazione e scrittura file
            f = open(nom, "w")
            f.write(stringa)
            f.close()

        #funione lettura file e crezione stringa
        def leggi(fil):
            os.chdir(Dir+"\\NON_TOCCARE\\files")
            f = open(str(fil), "r")
            stringa = f.read()
            f.close()
            i = 0
            j = 0
            temp = ""
            #ciclo per ogni lettera
            while i < len(stringa):
                if stringa[i] == "+":
                    #se la lettera è + e quella dopo ' allora la parola che segue è una parola chiave
                    if "'" in stringa[i: i+3] :
                        #nella variabile temp custodiamo tutto ciò che c'era da j a prima della parola chiave
                        temp = temp + stringa[j:i]
                        #facciamo tutti i vari controlli per individuare di quale parola chiave si tratta e la rimpiazziamo con ciò che è necessario nella variabile temp
                        if "prog" in stringa[i:i+7]:
                            temp += prog
                        elif "entita" in stringa[i:i+9]:
                            temp += entita
                        elif "entitPlu" in stringa[i:i+11]:
                            temp += entitaPlu
                        elif "dto" in stringa[i:i+6]:
                            temp += dto
                        elif "ns" in stringa[i:i+5]:
                            temp += ns
                        elif "Rep" in stringa[i:i+6]:
                            temp += Rep
                        elif "rep-" in stringa[i:i+7]:
                            temp +=rep
                        elif "usi" in stringa[i:i+6]:
                            temp += usi
                        elif "entitL" in stringa[i:i+9]:
                            temp += entita.lower()
                        elif "rep_" in stringa[i:i+7]:
                            temp += rep_
                        elif "Man" in stringa[i:i+6]:
                            temp += Man
                        elif "man-" in stringa[i:i+7]:
                            temp += man
                        elif "man_" in stringa[i:i+7]:
                            temp += man_
                        elif "campoZero" in stringa[i:i+12]:
                            temp += campoZero
                        elif "campoZL" in stringa[i:i+10]:
                            temp+= campoZero.lower()
                        elif "entitPL" in stringa[i:i+10]:
                            temp+=entitaPlu.lower()
                        elif "campiGet" in stringa[i:i+11]:
                            temp += campiGet()
                        elif "campiPar" in stringa[i:i+11]:
                            temp += campiPar()
                        elif "campiPaNul" in stringa[i:i+13]:
                            temp += campiPaNul()
                        elif "campiEle" in stringa[i:i+11]:
                            temp += campiEle()
                        elif "campiCost" in stringa[i:i+12]:
                            temp += campiCost()
                        elif "campiCreat" in stringa[i:i+13]:
                            temp += campiCreat()
                        elif "campiInp" in stringa[i:i+11]:
                            temp += campiInp()
                        elif "campiUpd" in stringa[i:i+10]:
                            temp += campiUpd()
                        elif "campiForm" in stringa[i:i+11]:
                            temp += campiForm()

                    #la lettera è + ed è seguita da + allora vuol dirre che ci troviamo dopo la parola chiave
                    elif "+" in stringa[i+1]:
                        #impostiamo j sulla lettera subito dopo ++
                        j = i +2        
                i+=1
            #ritorna il file con tutte le parole chiavi sostituite appositamente
            return temp

        #  CREAZIONE CARTELLE E CONTROLLO ESISTENZA
        if not os.path.exists(appE):
            os.makedirs(appE)
        if not os.path.exists(app_conE):
            os.makedirs(app_conE)
        if not os.path.exists(domE):
            os.makedirs(domE)
        if not os.path.exists(dom_shaE):
            os.makedirs(dom_shaE)
        if not os.path.exists(efcE):
            os.makedirs(efcE)

        if not os.path.exists(app):
            os.makedirs(app)
        if not os.path.exists(app_con):
            os.makedirs(app_con)
        if not os.path.exists(dom):
            os.makedirs(dom)
        if not os.path.exists(dom_sha):
            os.makedirs(dom_sha)
        if not os.path.exists(efc):
            os.makedirs(efc)
        if not os.path.exists(FE):
            os.makedirs(FE)

        #CREAZIONE FILE:

        # DOMAIN LAYER:

        crea("entita.txt", domE, entita+".cs")
        crea("entitaManager.txt", domE, entita+"Manager.cs")
        crea("entitaAlreadyExistsException.txt", domE, entita+"AlreadyExistsException.cs")
        crea("IentitaRepository.txt", domE, "I"+entita+"Repository.cs")
        crea("entitaConsts.txt", dom_shaE, entita+"Consts.cs")
        crea("Localization.txt", dom_sha, "Localization_.json")
        crea("progDomainErrorCodes.txt", dom_sha, prog+"DomainErrorCodes.cs")

        # DATABASE INTEGRATION:

        crea("EfCoreEntitaRepository.txt", efcE, "EfCore"+entita+"Repository.cs")
        crea("progDbContext.txt", efc, prog+"DbContext.cs")

        # APPLICATION LAYER:

        crea("IentitaAppService.txt", app_conE, "I"+entita+"AppService.cs")
        crea("dto.txt", app_conE, dto+".cs")
        crea("GetEntitaListDto.txt", app_conE, "Get"+entita+"ListDto.cs")
        crea("CreateDto.txt", app_conE, "Create"+dto+".cs")
        crea("UpdateDto.txt", app_conE, "Update"+dto+".cs")
        crea("progPermissions.txt", app_con, prog+"Permissions.cs")
        crea("progPermissionsDefinitionProvider.txt", app_con, prog+"PermissionsDefinitionProvider.cs")
        crea("entitaAppService.txt", appE, entita+"AppService.cs")
        crea("progApplicationAutoMapperProfile.txt", app, prog+"ApplicationAutoMapperProfile.cs")
        crea("progDataSeederContributor.txt", dom, prog+"DataSeederContributor.cs")

        # Front End:
        crea("typescript.txt", FE, entita.lower()+".component.ts")
        
        print("Generazione eseguita!")
        break 
