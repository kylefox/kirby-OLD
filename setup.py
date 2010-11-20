from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os


########################################################################
#
#   Code for finding packages & data files taken from Django's setup.py
#
def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('kirby'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])
#
########################################################################


setup(
    name="Kirby",
    description="Create websites with Markdown + Jinja2 and upload to Amazon CloudFront.",
    version="0.0.1pre-alpha",
    author="Kyle Fox",
    author_email="kyle.fox@gmail.com",
    url="http://github.com/kylefox/kirby",
    scripts=['bin/kirby'],
    packages=packages,
    data_files=data_files,
    classifiers=[ # see http://diveintopython3.org/packaging.html#trove
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ]
)