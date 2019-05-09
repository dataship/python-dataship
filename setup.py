from distutils.core import setup
setup(
  name = 'dataship',
  packages = ['dataship', 'dataship.beam'],
  install_requires=['numpy', 'pandas'],
  version = '0.7.0',
  description = 'Lightweight tools for reading, writing and storing data, locally and over the internet.',
  author = 'Waylon Flinn',
  author_email = 'waylonflinn@gmail.com',
  url = 'https://github.com/dataship/python-dataship', # use the URL to the github repo
  keywords = ['numpy', 'pandas', 'data-science', 'javascript', 'interoperability', 'columnar', 'data', 'compressed'], # arbitrary keywords
  classifiers = [],
)
