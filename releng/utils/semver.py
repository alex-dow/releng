import semantic_version

def incPatchVersion(ver):
    v = semantic_version.Version(ver)
    return str(v.next_patch())

def incMinorVersion(ver):
    v = semantic_version.Version(ver)
    return str(v.next_minor())

def incMajorVersion(ver):
    v = semantic_version.Version(ver)
    return str(v.next_major())

