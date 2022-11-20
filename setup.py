from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gondermgt/__init__.py
from gondermgt import __version__ as version

setup(
	name="gondermgt",
	version=version,
	description="gonder vehicle mgt system",
	author="360ground",
	author_email="bisrat@360ground.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
