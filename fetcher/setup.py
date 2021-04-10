
from setuptools import setup, find_packages
from myflora-fetcher.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='myflora-fetcher',
    version=VERSION,
    description='Query Xiaomi Flora devices & store data to designated services',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dragos Cirjan',
    author_email='dragos.cirjan@gmail.com',
    url='https://github.com/dragoscirjan/myflora',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'myflora-fetcher': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        myflora-fetcher = myflora-fetcher.main:main
    """,
)
