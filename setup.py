import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'psycopg2',
    'SQLAlchemy'
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='Pyramid-REST-API',
      version='0.0',
      description='pyr',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Natural Language :: English",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "Topic :: Software Development :: Version Control :: Git",
          "License :: OSI Approved :: MIT License",
      ],
      author='Michael Verdegaal',
      author_email='michaelverdegaal@hotmail.nl',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyr:main
      """,
      )
