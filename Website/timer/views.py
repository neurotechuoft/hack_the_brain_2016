from django.shortcuts import render
from yapsy.PluginManager import PluginManager

#!/usr/bin/env python2.7
import argparse  # new in Python2.7
import os
import time
import string
import atexit
import threading
import logging
import sys

# Create your views here.
def index(request):
    context = {}
    return render(request, 'timer/index.html', context)

#Take a baseline EEG measurement
def start_baseline(request):
    manager = PluginManager()
    plugin_name = request.data["plugin_name"]
    plugin = manager.getPluginByName(plugin_name)
    board = bci.OpenBCIBoard(port=args.port,
                                 daisy=args.daisy,
                                 filter_data=args.filtering,
                                 scaled_output=True,
                                 log=args.log)    
    if (plugin_name == "packets_to_csv"):
        plugin.plugin_object.pre_activate({}, sample_rate=board.getSampleRate(), eeg_channels=board.getNbEEGChannels(), aux_channels=board.getNbAUXChannels())
        
        
        
    
    
    
    
    
    