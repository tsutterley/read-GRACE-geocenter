from setuptools import setup, find_packages
setup(
	name='read-GRACE-geocenter',
	version='1.0.0.0',
	description='Reads geocenter coefficients from Sutterley et al. (2019)',
	url='https://github.com/tsutterley/read-GRACE-geocenter',
	author='Tyler Sutterley',
	author_email='tsutterl@uw.edu',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Physics',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
	],
	keywords='GRACE time-variable gravity, geocenter, degree one harmonics',
	packages=find_packages(),
	install_requires=['numpy','pyyaml'],
)
