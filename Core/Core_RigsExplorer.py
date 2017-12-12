import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import os

class Core_RigsExplorer(object):

    def __init__(self):
        """
        """

    def ScanFolders(self):
        """
        Barrido completo

        Se hace un barrido general de todas las carpetas de rig del servidor
        se buscan todas las que contienen rigs
        """

        Server_Z = "Z:/"
        Server_MASTER = "//MASTER/master/"

        # Mexicartoons
        #   Z:\MKF_animacion\MEXICARTOONS\PERSONAJES/Personaje**/RIGGING/ MASTER o version

        # Otros candidatos
        #   Z:\MKF_animacion\OTROS CANDIDATOS\PERSONAJES/Personaje**/RIGGING/ MASTER o version

        path = Server_Z
        files_ = os.listdir(path)

        reporter = mel.eval( 'string $tmp = $gCommandReporter;' )
        cmds.cmdScrollFieldReporter(reporter, e=True, clear=True)

        for f in files_:
            if f.find(".") is -1:
                #print f
                new_files = os.listdir(path+ "/"+f)
                for nf in new_files:
                    if nf.find("RIGGING") is not -1:
                        rigFiles = os.listdir(path + "/"+f+"/"+nf)
                        print path + "/"+f+"/"+nf
                        rigVersion = ""
                        rigMaster = ""
                        for rf in rigFiles:
                            validaciones = self.validacionArchivo(rf)
                            if validaciones[0]:
                                    rigMaster = rf
                        
                            if validaciones[1]:
                                if rigVersion != "":
                                    print rf
                                    cur_ver = self.GetVersion(rf)
                                    print "  " + rigVersion + "  " + str(cur_ver)
                                    if int(self.GetVersion(rigVersion)) < cur_ver:
                                        rigVersion = rf
                                else:
                                    rigVersion = rf

                        if rigMaster != "":
                            print "   Master: " + rigMaster
                        else:
                            print "   Version: " + rigVersion
        "   " + rigVersion





    def ScanElements(self, web_ids):
        """
        Barrido de elementos web

        Aqui van la lista de elementos ligados a la escena, 
        estos se mandaran desde la base de datos web.
        """

    def ScanTrelloElements(self, trello_boards):
        """
        Barrido y acomo de objetos por tableros


        """

    def GetVersion(self, file):
        version = file

        parts = version.split("_V")
        lastPart = parts[len(parts)-1]
        lastPart = lastPart.split(".m")[0]
        return int(lastPart)

    def ValidacionArchivo(self, file):
        valido = False
        validoMaster = False
        validoVersion = False

        if file.find(".ma") is not -1 or file.find(".mb") is not -1:
            if file[0] != ".":
                valido = True

        # Validacion para Master
        if valido:
            posibles = ["MASTER", "master", "Master"]
            for pos in posibles:
                sections = file.split("_")
                if sections[-1].find(pos) is not -1:
                    validoMaster = True

        # Validacion para version
        if valido:
            sections = file.split("_")
            lastP = sections[-1]
            lastP = lastP.split(".m")[0]
            lastP = lastP.split("V")[-1]
            try:
                val = int(lastP)
                validoVersion = True
            except:
                pass

        valido = validoMaster or validoVersion
        return (validoMaster, validoVersion)

