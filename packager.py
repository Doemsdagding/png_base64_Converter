import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '--name=image_to_base64',
    '--windowed',
    '--onefile',
    '--add-data', 'base64convert\\base.kv:.',
    '--add-data', 'base64convert\\madimione-regular.otf:.',
    '--hidden-import', 'pkg_resources.extern.packaging.version',
    '--hidden-import', 'pkg_resources.extern.packaging.specifiers', 
    '--hidden-import', 'pkg_resources.extern.packaging.requirements',
    '--hidden-import', 'win32timezone',
    '--hidden-import', 'pywin32',
    '--hidden-import', 'PIL',
    '--hidden-import', 'PIL._imagingtk',
    '--hidden-import', 'PIL._imaging',
    '--hidden-import', 'PIL._webp',
    'base64convert\\base.py'
])
