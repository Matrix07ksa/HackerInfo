from setuptools import setup
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(name='hackinfo',
      version='1.0.0',
      description='Hacker_Info',
      url='https://github.com/Matrix07ksa/HackerInfo/tree/master/HackerInfo_scan',
      author='Hejab Zaeri',
      author_email = "hjoooby9900@gmail.com", 
      license ='GBLV3',
      packages=['source'],
      install_requires=['requests==2.22.0'],
      python_requires=">=3",
)
      
