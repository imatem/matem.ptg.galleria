from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='matem.ptg.galleria',
      version=version,
      description="customization to collective.ptg.galleria",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone plonetruegallery addon',
      author='Gildardo Bautista',
      author_email='gil.cano@gmail.com',
      url='https://github.com/imatem/matem.ptg.galleria',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['matem', 'matem.ptg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.plonetruegallery',
          'collective.ptg.galleria'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
