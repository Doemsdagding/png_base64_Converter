import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '--name=image_to_base64',
    '--windowed',
    '--onefile',
    '--add-data', 'base64convert\\base.kv:.',
    '--hidden-import', 'pkg_resources.extern.packaging.version',
    '--hidden-import', 'pkg_resources.extern.packaging.specifiers', 
    '--hidden-import', 'pkg_resources.extern.packaging.requirements',
    'base64convert\\base.py'
])
