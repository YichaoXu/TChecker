from setuptools import setup, find_packages
import os, shutil

cur_path = os.path.dirname(os.path.abspath(__file__))
build_path = os.path.join(cur_path, 'build')
if os.path.isdir(build_path):
    print('INFO del dir ', build_path) 
    shutil.rmtree(build_path)

setup(
    version='0.1', 
    name = 'tchecker-wrapper', 
    author='yichao@hopkins', 
    description='a wrapper for the php', 
    install_requires = [
        'typer==0.6.1', 
        'python-dotenv==0.20.0'
    ],
    scripts=['tchecker']
)