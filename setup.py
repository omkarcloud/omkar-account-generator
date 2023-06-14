from distutils.core import setup


install_requires = [
    "requests"

]
extras_require = {}
cpython_dependencies = [
    "PyDispatcher>=2.0.5",
]

def get_description():
    try:
      return open("README.rst", encoding="utf-8").read()
    except:
      return None
    
            
setup(
    name='omkar_account_generator',
    packages=['omkar_account_generator'],
    version='1.1.1',
    license='MIT',
    project_urls={
        "Documentation": "https://github.com/omkarcloud/omkar-account-generator",
        "Source": "https://github.com/omkarcloud/omkar-account-generator",
        "Tracker": "https://github.com/omkarcloud/omkar-account-generator/issues",
    },

    description="Generate user accounts",
    long_description=get_description(),
    # long_description_content_type="text/markdown",
    author='Chetan Jain',
    author_email='chetan@omkar.cloud',
    maintainer="Chetan Jain",
    maintainer_email="chetan@omkar.cloud",

    keywords=['account-generator', 'account-creator',  'accountgenerator', 'generator', 'user-generator', 'dummy-users', 'user-data', 'fake-user', 'python', 'random-user-generator', 'account'],
    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
)