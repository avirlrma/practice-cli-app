from setuptools import setup

setup(
    name = 'Workpdf',
    version = '0.1',
    packages = ['Wpdf'],
    entry_points = {
        'console_scripts': [
            'wpdf = Wpdf.wpdf:getPages'
        ]
    })