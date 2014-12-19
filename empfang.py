import sys
import logging
import getpass
from optparse import OptionParser
import subprocess
import sleekxmpp
from tkinter import *


global st
global rechnen


# set default encoding to utf8
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input


status = Tk()
status.title("Tkinter Messenger")
status.resizable(width=FALSE, height=FALSE)

#hier wird die Klasse für den Empfänger erstellt:
class empfang(sleekxmpp.ClientXMPP):
    
    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # start the session
        self.add_event_handler("session_start", self.start)

        # message handler
        #Wenn eine nachricht ankommt wird self.empfang ausgeführt
        self.add_event_handler("message", self.empfang)
        #self.add_event_handler("message", self.message)
        #self.add_event_handler("nachricht_senden", self.nachricht_senden)

        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="Rechnen==True", command=self.rechnen)
        self.button.pack(side=RIGHT)

    def rechnen(self):
        print("set")
        
    def nachricht_senden(self):
        name = input("Name an: ")
        nachricht = input("Nachricht: ")
        self.send_message(name + "@ifga", nachricht)
        
    def start(self, event):
        # session start method
        self.send_presence()
        self.get_roster()
        #Er ist bereit
        print("startet")
        while 0==0:
            self.nachricht_senden()
        
    def status(self):
        global rechnen
        global st
        if rechnen == True: #Status wird abgefragt
            print("Test")
            status = Tk()
            g = Label(status, bg="green")
            g.pack()
            st = "beschäftigt."
        else:
            status = Tk()
            r = Label(status, bg="red")
            r.pack()
            st = "arbeitslos."
        status.mainloop()

    def empfang(self, msg):
        global st
        st = "null" #Vorübergängig
        print("NACHRICHT!")
        #Die Nachricht wir angezeigt
        print(msg['body'])
        print("Du bist gerade ", st)
            
if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)


    
    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')


    #Login Daten
    opts.jid = 'rosenbhe@ifga'
    opts.password = 'rosenbhe'

    # Setup the empfanger and register plugins.
    empfanger = empfang(opts.jid, opts.password)
    empfanger.register_plugin('xep_0030') # Service Discovery
    empfanger.register_plugin('xep_0004') # Data Forms
    empfanger.register_plugin('xep_0060') # PubSub
    empfanger.register_plugin('xep_0199') # XMPP Ping
    #for easy
    empfanger.auto_authorize = True
    empfanger.auto_subscribe = True

    # Connect to the XMPP server and start processing XMPP stanzas.
    if empfanger.connect(('odin', 5222), use_tls=True):
        empfanger.process(threaded=False) #block=True
        print("Done")
    else:
        print("Unable to connect.")
        
status = Tk()
empfang = Empfang(status)
status.mainloop()
