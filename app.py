from flask import Flask
from flask import render_template
import os
import os.path
from gov.sandia.atomicHost.ah.controller import ControllerWindows
from gov.sandia.atomicHost.evtx.evtxfiles import EvtxFile
from gov.sandia.atomicHost.etc.configuration.attackHostDirs import Config
from gov.sandia.usersimulator.controller.guicontoller.web import Firefox
from gov.sandia.usersimulator.controller.guicontoller.web import Chrome
from gov.sandia.usersimulator.controller.guicontoller.web import Edge
from gov.sandia.usersimulator.controller.guicontoller.microsoft import Word
from gov.sandia.usersimulator.controller.guicontoller.mounts import Mounts

app = Flask(__name__)



@app.route('/')
def atomicgui():
    return render_template('dashboard.html')

@app.route('/winCollection')
def winCollection():
    return render_template('windows-collection.html')



@app.route('/winDiscovery')
def winDiscovery():
    return render_template('windows-discovery.html')

@app.route('/winCredential-access')
def winCredentialAccess():
    return render_template('windows-credential-access.html')

@app.route('/winDefense-Evasion')
def winDefenseEvasion():
    return render_template('windows-defense-evasion.html')


@app.route('/winCommand-and-control')
def winCommandAndControl():
    return render_template('windows-command-and-control.html')

@app.route('/winExecution')
def winExecution():
    return render_template('windows-execution.html')

@app.route('/winExfiltration')
def winExfiltration():
    return render_template('windows-exfiltration.html')

@app.route('/winImpact')
def winImpact():
    return render_template('windows-impact.html')

@app.route('/winInitial-access')
def winInitialAccess():
    return render_template('windows-initial-access.html')

@app.route('/winLateral-movement')
def winLateralMovement():
    return render_template('windows-lateral-movement.html')

@app.route('/winPersistence')
def winPersistence():
    return render_template('windows-persistence.html')

@app.route('/winPrivilege-escalation')
def winPrivilegeEscalation():
    return render_template('windows-privilege-escalation.html')



@app.route('/run/<string:techniqueCategory>/<string:name>/<int:number>/<int:action>/<string:platform>')
def technique(techniqueCategory,name,number,action,platform):

    cf = Config()
    cf.checkFolders()
    cf.clearResults()

    if platform=="W":
        c = ControllerWindows(techniqueCategory,name,number,action,platform,cf.powerShellDir,cf.taggedEventsDirectory,cf.jsonFromEventsDirectory, cf.attackOutputDir,cf.detectOutputDir,cf.discoveryCategoryScriptDir,cf.absInstallationDir)

    elif platform=="X":
        return "<H1>Linux is not yet implemented</H1>"

    elif platform == "M":
        return "<H1>OSX is not yet implemented</H1>"

    else:
        return "Unknown platform. Shoule be W,X or M"


    return "<H1>Attack Host Run Complete</H1>"


@app.route('/run/evtx/<int:num>')
def evtx2json(num):
    c = Config()
    c.checkFolders()


    
    EVTXInputDir = os.path.join(c.inputDir,"evtx")
   
    EVTXFilesForProcessing = os.listdir(EVTXInputDir)

    XMLOutputDir = os.path.join(c.outputDir,"XMLFromEVTX")

    if (num == 0): # We are processing EVTX to XML only
        
        for j in EVTXFilesForProcessing:   
            e = EvtxFile(j,c.dataDir)
            e.saveXML()
    elif (num == 1): # We are processing EVTX to JSON and to XML

        
        for k in EVTXFilesForProcessing:
            e = EvtxFile(k,c.dataDir) # file to process, dataDirectory            
            e.saveJSON()
       
        
    else:
        pass
    return "<H1>Attack Host Run Complete</H1>"


@app.route('/run/usersimulator')
def usersimulator():

    return render_template('usersimdashboard.html')
 
@app.route('/firefox')
def firefox():
    c = Config()
    c.checkFolders()
    f = Firefox(c.absInstallationDir)
    return '2'

@app.route('/chrome')
def chrome():
    c = Config()
    c.checkFolders()
    c = Chrome(c.absInstallationDir)
    return '1'

@app.route('/edge')
def edge():
    c = Config()
    c.checkFolders()
    e = Edge(c.absInstallationDir)


@app.route('/worduser')
def word():
    c = Config()
    c.checkFolders()
    w = Word(c.absInstallationDir,c.filesDir)
    return '3'

@app.route('/mounts')
def mount():
    c = Config()
    c.checkFolders()
    m = Mounts(c.absInstallationDir)
    return '3'
    
    
@app.route('/run/version2')
def version2():

    return render_template('attackHostBase.html')
    









if __name__ == '__main__':
    app.run(debug=True)


