from setuptools import setup

setup(
    name='cqhttp',
    version='1.1.0',
    packages=['cqhttp'],
    url='https://github.com/richardchien/python-cqhttp',
    license='MIT License',
    author='Richard Chien',
    author_email='richardchienthebest@gmail.com',
    description='CQHttp Python SDK',
    install_requires=['Flask', 'requests'],
    python_requires='>=3.5',
    platforms='any'
)
