from setuptools import setup

setup(
    name="simple-releng",
    version="0.0.1",
    description="Simple Release Engineering Toolkit",
    url="https://github.com/alex-dow/simple-releng",
    author="Alex D",
    author_email="adow@psikon.com",
    license="MIT",
    packages=[
        'releng',
        'releng.cli',
        'releng.utils',
        'releng.configs',
        'releng.configs.general',
        'releng.configs.py'
    ],
    zip_safe=True,
    test_suite="tests",
    tests_require=[
        'mock>=1.0.1',
        'coverage>=3.7.0'
    ],
    install_requires=[
        'semantic_version>=2.4.2',
        'docopt>=0.6.2'
    ],
    entry_points={
        'console_scripts': [
            'releng-version=releng.cli.version:main'
        ]
    }
)
