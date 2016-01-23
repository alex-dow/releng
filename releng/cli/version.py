from docopt import docopt
import importlib
import sys
from releng.configs import getConfigModule
from releng import RelengException


validConfigTypes = [
    'sonarqube',
    'setuptools'
]

doc = """Simple Releng Toolkit - Version Tool

  Usage:
    version.py incMajor <fn> (--type=<type> | --re=<re>) [options]
    version.py incMinor <fn> (--type=<type> | --re=<re>) [options]
    version.py incPatch <fn> (--type=<type> | --re=<re>) [options]
    version.py types
    

  Options:
    --type TYPE         What kind of config file is it
    --version           Show version number
    -h --help           Show this help
"""

def showTypes():
    print "Simple Releng - Version Tool"
    print " "
    print "Valid Configuration Types:"
    for confType in validConfigTypes:
        print "  " + confType

def main():
    arguments = docopt(doc, version='0.0.1')

    if arguments['types'] == True:
        showTypes()
        sys.exit(0)

    confModName = arguments['--type']

    try:
        confMod = getConfigModule(confModName)
        fn = arguments['<fn>']
        
        if arguments['incMajor']:
            confMod.incMajor(fn)

        if arguments['incMinor']:
            confMod.incMinor(fn)

        if arguments['incPatch']:
            confMod.incPatch(fn)

        print '[INFO] New version set in ' + fn + ': ' + confMod.getCurrentVersion(fn)
    except RelengException as e:
        print '[ERROR] ' + str(e)
        sys.exit(1)


 
if __name__ == '__main__':
    main()
       
