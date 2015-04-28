from distutils.core import setup

setup(
	name="python-daemonize",
	version="0.0.1",
	author="Roger G. Coram",
	author_email="roger.coram@bl.uk",
	packages=[ "daemonize" ],
	license="LICENSE.txt",
	description="Python 2.x daemon implementation.",
	long_description=open( "README.md" ).read(),
	install_requires=[
	],
)
