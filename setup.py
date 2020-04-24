from setuptools import setup

APP = ['simulation2.py']
#DATA_FILES = ['1.gif','2.gif'] No images used
DATA_FILES = []
OPTIONS = {
 'iconfile':'applogo.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
 'plist': {
     'CFBundleName': 'Random Walk',
     'CFBundleDisplayName': 'Random Walk',
     'CFBundleGetInfoString': "A simulation of a random walk",
     'CFBundleVersion': "0.0.0",
     'CFBundleShortVersionString': "0.0.0",
     'NSHumanReadableCopyright': 'SoySoy4444 © 2020. All Rights Reserved.'
     }
}

setup(
    app=APP,
    name = "Random Walk",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
