import re
import sys
from releng.utils import semver
from releng import RelengException

def getCurrentVersion(fn):

    rexp = "version=[\"|'](.+)[\"|']"

    try:
        with open(fn) as f:
            for line in f.readlines():
                matches = re.match(rexp, line.strip())
                if matches != None:
                    return matches.groups()[0]
    except IOError as e:
        raise RelengException('Unable to open ' + fn)


def saveNewVersion(fn, newver):

    curver = getCurrentVersion(fn)

    newlines = []
    with open(fn) as f:
        for line in f.readlines():
            line = line.rstrip()
            if "version=\"" + curver + "\"" in line or "version='" + curver + "'" in line:
                line = line.replace(curver, newver)
            newlines.append(line)
    with open(fn, 'w') as f:
        f.write("\n".join(newlines))



def incMajor(fn):
    newver = semver.incMajorVersion(getCurrentVersion(fn))
    saveNewVersion(fn, newver)

def incMinor(fn):
    newver = semver.incMinorVersion(getCurrentVersion(fn))
    saveNewVersion(fn, newver)

def incPatch(fn):
    newver = semver.incPatchVersion(getCurrentVersion(fn))
    saveNewVersion(fn, newver)

