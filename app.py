from flask import Flask
from flask import render_template
import os
import os.path
from gov.sandia.attackHost.controller import ControllerWindows
from gov.sandia.attackHost.evtx.evtxfiles import EvtxFile
from gov.sandia.attackHost.etc.configuration.attackHostDirs import Config
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
    print("OUT")
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
    
    if platform=="W":
        c = ControllerWindows(techniqueCategory,name,number,action,platform,cf.powerShellDir,cf.taggedEventsDirectory,cf.jsonFromEventsDirectory, cf.attackOutputDir,cf.detectOutputDir,cf.absInstallationDir)
        return "<H1>Attack Host Run Complete</H1>"
    elif platform=="X":
        return "<H1>Linux is not yet implemented</H1>"
    elif platform == "M":
        return "<H1>OSX is not yet implemented</H1>"
    else:
        return "Unknown platform. Should be W,X or M"
    return "<H1>Attack Host Run Complete</H1>"

    
@app.route('/dummy1')
def dummy1():
    
    return render_template('dummy1.html')

@app.route('/dummy2')
def dummy2():
    
    return render_template('dummy2.html')

@app.route('/dummy3')
def dummy3():
    
    return render_template('dummy3.html')

@app.route('/dummy4')
def dummy4():
    
    return render_template('dummy4.html')

@app.route('/dummy5')
def dummy5():
    
    return render_template('dummy5.html')

@app.route('/dummy6')
def dummy6():
    
    return render_template('dummy6.html')

@app.route('/dummy7')
def dummy7():
    
    return render_template('dummy7.html')

@app.route('/dummy8')
def dummy8():
    
    return render_template('dummy8.html')

@app.route('/dummy9')
def dummy9():
    
    return render_template('dummy9.html')

@app.route('/dummy10')
def dummy10():
    
    return render_template('dummy10.html')

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


RR