from setuptools import setup, find_packages

# get long_description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()
long_description_content_type = "text/markdown"

# get install requirements
with open('requirements.txt') as fh:
    install_requires = [line.split().pop(0) for line in fh.read().splitlines()]

# get version
with open('version.txt') as fh:
    version = fh.read()

setup(
    name='read-GRACE-geocenter',
    version=version,
    description='Reads geocenter coefficients from Sutterley et al. (2019)',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url='https://github.com/tsutterley/read-GRACE-geocenter',
    author='Tyler Sutterley',
    author_email='tsutterl@uw.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='GRACE, GRACE-FO, time-variable gravity, geocenter, degree one harmonics',
    packages=find_packages(),
    install_requires=install_requires,
)
