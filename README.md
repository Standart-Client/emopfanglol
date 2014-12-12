emopfanglol
===========


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    this file is a slightly modified echobot from
    sleekXMPP (C) 2010  Nathanael C. Fritz
    needs sleekxmpp
"""

import sys
import logging
import getpass
from optparse import OptionParser
import subprocess
import sleekxmpp

global st




# set default encoding to utf8
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input


class empfang(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # start the session
        self.add_event_handler("session_start", self.start)

        # message handler
        self.add_event_handler("message", self.empfang)

    def start(self, event):
        # session start method
        self.send_presence()
        self.get_roster()
        print("startet")


        

#    def hallo(self, msg):
#        print("hallo wurde ausgeführt")
#        print("%(body)s" % msg)
        



#message empfangen
    def empfang(self, msg):
        global st
        st = "null"
        # process incoming messages
        print("NACHRICHT!")
        print(msg['body'])
        print("Dein Partner ist gerade ", st)
       # print("asd"+out.decode("utf-8")+"asd")
       # msg.reply(out.decode("utf-8")).send()


            
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

    opts.jid = 'rosenbhe@ifga'
    opts.password = 'rosenbhe'

    # Setup the EchoBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    empfanger = empfang(opts.jid, opts.password)
    empfanger.register_plugin('xep_0030') # Service Discovery
    empfanger.register_plugin('xep_0004') # Data Forms
    empfanger.register_plugin('xep_0060') # PubSub
    empfanger.register_plugin('xep_0199') # XMPP Ping
    empfanger.auto_authorize = True
    empfanger.auto_subscribe = True

    # Connect to the XMPP server and start processing XMPP stanzas.
    if empfanger.connect(('odin', 5222), use_tls=True):
        empfanger.process(threaded=False) #block=True
        print("Done")
    else:
        print("Unable to connect.")




