from setuptools import setup, find_packages

version = '0.0.0'

setup(
    name='ipytube',
    version=version,
    description='IPython youtube search embed',
    author='Brian McFee',
    author_email='brian.mcfee@nyu.edu',
    url='http://github.com/bmcfee/ipytube',
    download_url='http://github.com/bmcfee/ipytube/releases',
    packages=find_packages(),
    long_description='IPython youtube search embed',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ],
    keywords='',
    license='MIT',
    install_requires=[
        'ipython>=2.0',
        'google-api-python-client',
    ],
    extras_require={}
)
