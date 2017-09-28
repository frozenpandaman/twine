#!/usr/bin/env python2
#
# This builds an .app out of Twine for use with OS X.
# Call this with this command line: buildapp.py py2app

from distutils.core import setup
from version import versionString
import py2app

setup(app = ['app.py'], options = dict(py2app = dict( argv_emulation = True,
                                       iconfile = 'appicons/app2.icns', \
                                       resources = ['icons', 'targets', 'appicons/doc.icns'], \
                                       plist = dict( \
                                       CFBundleShortVersionString = versionString, \
                                       CFBundleName = 'Twine', \
                                       CFBundleSignature = 'twee', \
                                       CFBundleIconFile = 'app2.icns',\
                                       CFBundleGetInfoString = 'An open-source tool for telling interactive stories',\
                                       CFBundleDocumentTypes = [dict( \
                                           CFBundleTypeIconFile = 'doc.icns',\
                                           CFBundleTypeName = 'Twine story',\
                                           CFBundleTypeRole = 'Editor',\
                                           CFBundleTypeExtensions=["tws"]\
                                       )],\
                                       NSHumanReadableCopyright = 'GNU General Public License v3'))))
