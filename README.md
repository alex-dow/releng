# Simple Release Engineering Toolkit

This is a collection of opinionated tools to simply and automate various tasks that one has to do when preparing a release.

These tools will parse various configuration files to increment major, minor, and patch numbers.

## Expectations

These tools are designed with expectations in mind, and as such, may not be appropriate for your project.

Look through these requirements, and check out the examples, to see if these tools would be a good fit for your project.

1. Your versioning scheme follows the [Semver](http://semver.org) standard.
2. Any configuration or build files contain the version number inside them
3. Your RCS is git
4. The master branch contains the latest stable release
5. New releases are tagged from the master branch

### Assumed Workflow

1. All changes for the new release are in the master branch
2. You increase the version number in your build files
3. You commit and push the changes to the master branch
4. You tag the release
5. You create various packaged forms of your project
6. You upload the packages to various repositories

## Installation

```
$ git clone https://github.com/alex-dow/simple-releng
$ python setup.py install
```

## Usage

### Command Line

The toolkit comes with several command line tools:

###### releng-version

Use this tool to increase the version of your project. You must call this command for every config file you need to modify.

For example, if you wanted to increase the major version in your python project's setup.py file you can do this:

```python
# setup.py
from setuptools import setup
setup(
  name="myProject",
  version="0.1.3",
  description="My awesome project"
)
```

```
$ releng-version incMajor setup.py --type=setuptools
```

```python
# new setup.py
from setuptools import setup
setup(
  name="myProject",
  version="1.0.0",
  description="My awesome project"
)
```

For a list of supported configuration types, try:

```
$ releng-version types
```

### API

###### Changing Verions

All config modules have the following functions:

* `incMajor(fn)` Increase the major version number for the given filename
* `incMinor(fn)` Increase the minor version number for the given filename
* `incPatch(fn)` Increase the patch version number for the given filename
* `getCurrentVersion(fn)` Returns the current version number stored in the given filename

Example with Sonarqube:

```python
from releng.configs import sonarqube
from releng import RelengException

try:
  sonarqube.incMajor('sonar-project.properties')
except RelengException as e:
  print e
```

Example with Setuptools:

```python
from releng.configs import setuptools
from releng import RelengException

try:
  sonarqube.incPatch('setup.py')
except RelengException as e:
  print e
```
