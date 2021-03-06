from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='msd.rdfexport',
      version=version,
      description="RDF Export",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='MSD',
      author_email='webmaster@medsci.ox.ac.uk',
      url='http://www.medsci.ox.ac.uk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['msd'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
