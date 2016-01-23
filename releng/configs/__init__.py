from releng.configs.general import sonarqube
from releng.configs.py import setuptools
from releng import RelengException

configs = {
    'sonarqube': {
        'incMajor': sonarqube.incMajor,
        'incMinor': sonarqube.incMinor,
        'incPatch': sonarqube.incPatch
    }
}

class InvalidConfigModule(RelengException):
    pass

class ImportException(RelengException):
    pass

def getConfigModule(name):
    try:
        targetName = 'releng.configs.' + name
        pkg = __import__('releng', fromlist=['configs'])
        mod = getattr(pkg.configs, name)
        return mod
    except AttributeError as e:
        raise InvalidConfigModule(name + ' is not part of the config package, try releng-version types for a list of available types')
    except ImportError as e:
        raise ImportException('Config module could not be imported: ' + name + ' - resolved to: ' + targetName + ' - reason: ' + e)

