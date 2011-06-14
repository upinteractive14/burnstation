#!/usr/bin/python
# -*- coding: utf-8 -*-

import mpd
import urllib
import sys
from ErrorsHandler import *

client = mpd.MPDClient()           # create client object
#client.stop()
#client.connect("localhost", 6600)  # connect to localhost:6600
#client.close()                     # send the close command
#client.disconnect() 


class OggPlayer:
    """MPD player client for BurnStation
    """

    def __init__(self):
        self._player = None

        self._playing      = False
        self._playlist    = []
        self._current     = -1
        self.volume_level = 0.5

        logger.info("MPD player init complete")

    def ClearPlaylist(self):
        self._playlist = []
        self._current = -1

    def AddToPlaylist(self, uri):
        self.uri = uri
        logger.info("Added " + uri)
        self._playlist.append(uri)

    def Play(self):
        client.connect("localhost", 6600)  # connect to localhost:6600
        client.stop()
        client.play()
        client.close()                     # send the close command
        client.disconnect()

    def Stop(self):
        client.connect("localhost", 6600)  # connect to localhost:6600
        client.stop()
        client.close()                     # send the close command
        client.disconnect()

    def Seek(self, time):
        #os.popen('mpc seek +00:00:10')
        client.connect("localhost", 6600)  # connect to localhost:6600
        client.seek(1, time)
        client.disconnect()

    def SetVolume(self, level):
        self.volume_level = level
        logger.info("player: setting volume to: %f" % level)

