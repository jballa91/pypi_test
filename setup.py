import setuptools

with open("README.md", "r") as file:
  long_description = file.read()

setuptools.setup(
  name="pypi_gh_test",
  version='0.0.1',
  author="James Ballard",
  author_email="jballard@bluewater-fintech.com",
  description="test",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/jballa91/pypi_test",
  packates=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3"
  ],
  install_requires=[
    'django==2.2.1'
  ]
)