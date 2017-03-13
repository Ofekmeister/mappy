from setuptools import setup, find_packages

with open('README.rst', 'r') as infile:
    read_me = infile.read()

setup(
    name='mappy',
    version='0.1.0',
    description='Efficient, well-tested collection of mappings',
    long_description=read_me,
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    maintainer='Ofek Lev',
    maintainer_email='ofekmeister@gmail.com',
    url='https://github.com/Ofekmeister/mappy',
    download_url='https://github.com/Ofekmeister/mappy',
    license='MIT',
    platforms=None,

    keywords=[
        'collections',
        'map',
        'mapping',
        'dict',
        'dictionary',
        'multimap',
        'bidirectional map',
        'case insensitive',
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=[],

    packages=find_packages(),
)
