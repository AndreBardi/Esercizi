import os


def CercaStringaInNomefile(sFile, sStringa):
    sFileLC = sFile.lower()
    sStringaLC = sStringa.lower()

    if(sFileLC.find(sStringaLC)>=0):
        return True
    else:
        return False
    
def CercaStringaInContenutoFile(sPathFile, sStringa):
    return False

sRoot = input("Inserisci la root directory: ")
sParola = input("Inserisci la parola da cercare: ")
sOutDir = input("Inserisci directory di output: ")


iNumFileTrovati = 0
for root, dirs, files in os.walk(sRoot):
    print(f"Sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} files")
    for file in files:
        print(f"Devo vedere se {file} contiene {sParola}")
        iRet = CercaStringaInNomefile(file, sParola)
        if iRet == True:
            iNumFileTrovati += 1
        else:
            sFilePathCompleto = os.path.join(root, file)
            iRet = CercaStringaInContenutofile(sFilePathCompleto)
            if(iRet==True):
                iNumFileTrovati += 1

print(f"Ho trovato {iNumFileTrovati} files")