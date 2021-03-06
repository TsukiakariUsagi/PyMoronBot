# -*- coding: utf-8 -*-
"""
Created on Dec 05, 2013

@author: Tyranic-Moron
"""

from CommandInterface import CommandInterface
from IRCMessage import IRCMessage
from IRCResponse import IRCResponse, ResponseType

from Utils import WebUtils


class Gif(CommandInterface):
    triggers = ['gif']
    help = 'gif - fetches a random gif posted during Desert Bus'
    
    def execute(self, message):
        """
        @type message: IRCMessage
        """
        url = "http://greywool.com/desertbus/gifs/random.php"

        webPage = WebUtils.fetchURL(url)

        link = webPage.body

        return IRCResponse(ResponseType.Say, u"Random DB gif: {0}".format(link), message.ReplyTo)
