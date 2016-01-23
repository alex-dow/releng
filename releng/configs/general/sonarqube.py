from releng.utils import semver

def getCurrentVersion(fn):
    with open(fn) as f:
        for line in f.readlines():
            if line.startswith('sonar.projectVersion'):
                version = line.split('=')[1]
                return version

def saveNewVersion(fn, ver):
    with open(fn) as f:
        newConfigFile = []
        for line in f.readlines():
            if line.startswith('sonar.projectVersion'):
                lineParts = line.split('=')
                lineParts[1] = ver

                line = '='.join(lineParts)
            newConfigFile.append(line.rstrip())
    with open(fn, 'w') as f:
        f.write('\n'.join(newConfigFile))


def incPatch(fn):
    newVersion = semver.incPatchVersion(getCurrentVersion(fn))
    saveNewVersion(fn, newVersion)

def incMinor(fn):
    newVersion = semver.incMinorVersion(getCurrentVersion(fn))
    saveNewVersion(fn, newVersion)

def incMajor(fn):
    newVersion = semver.incMajorVersion(getCurrentVersion(fn))
    saveNewVersion(fn, newVersion)

