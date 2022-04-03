class AhConst:
    
    def __init__(self):
        self.headerLeft = '"**********"'
        self.headerRight = '"**********"'
        self.suffix = '|  Out-File -FilePath $args[0] -Append'
        self.prefix = 'cmd.exe /c '
        