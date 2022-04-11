class SubTechniqueSignature:

    def __init__(self,record):
        self.record = record
        self.numberOfSubtechniqueCommands = self.record["numberSubCommands"]
        self.coreSignatureRecord = self.record['subCommands']
        for i in self.coreSignatureRecord:
            print(str(i) + ", " + str(self.coreSignatureRecord[i]))

    def printRecord(self):
        print("Full Record: " + str(self.record))

    def printNumberOfSubCommands(self):
        print("Number of subcommands: " + str(int(self.numberOfSubtechniqueCommands)))


class SubTechniqueCommandRecord:
    """
        A class representing the command sets in a SubtechniqueRecord Class

        ...

        Attributes
        ----------
        commandSet : List
            A list of Command Class Objects
        eventID : int
            The ID of the sysmon event type
        inputDict : dict
            the sound that the animal makes
        numberCommands : int
            The number of Command Class Objects in the SubtechniqueCommandRecord Object


        """

    def __init__(self, designation, eventID=0):
        self.commandDesignation = designation
        self.eventID = eventID




class Evt1SubTechniqueCommandRecord(SubTechniqueCommandRecord):
    def __init__(self):
        self.image = ""
        self.description = ""
        self.originalFileName = ""
        self.commandLine = ""
        super().__init__(eventID=1)
        print(list(self.inputDict))
