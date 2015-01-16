import os
from pyobjus import autoclass
from plyer.facades import Dialog

from pyobjus.dylib_manager import load_framework, INCLUDE
load_framework(INCLUDE.AppKit)

from pyobjus import objc_arr, objc_str

NSURL = autoclass('NSURL')
NSOpenPanel = autoclass('NSOpenPanel')
NSSavePanel = autoclass('NSSavePanel')
NSOKButton = 1

class Dialog(Dialog):
    '''Manage system open/save/load... dialogs.
    '''

    def open(self, path='', choose_dir=False,
        choose_files=True, multiselect=False, filetypes=[],
        prompt=''):
        '''
        '''

        panel = None
        panel = NSOpenPanel.openPanel()

        panel.setCanCreateDirectories_(True)
        panel.setCanChooseDirectories_(choose_dir)
        panel.setCanChooseFiles_(choose_files)

        if path:
            url = NSURL.fileURLWithPath_(path)
            panel.setDirectoryURL_(url)

        #
        if filetypes:
            ftypes = []
            for file in filetypes:
                ftypes.append(objc_str(file))
            ftypes = objc_arr(ftypes)

        if panel.runModalForTypes_(filetypes):
            return panel.filename().UTF8String()
        return ''

    def save(self, path='', filetypes=[], prompt=''):
        '''
        '''
        panel = None
        panel = NSSavePanel.savePanel()

        if name_field:
            panel.setNameFieldLabel_(name_field)
        
        if path:
            url = NSURL.fileURLWithPath_(path)
            panel.setDirectoryURL_(url)

        if filetypes:
            ftypes = []
            for file in filetypes:
                ftypes.append(objc_str(file))
            ftypes = objc_arr(ftypes)

        if panel.runModalForTypes_(filetypes):
            return panel.filename().UTF8String()
        return ''

def instance():
    return Dialog()
