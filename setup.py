from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cqhttp',
    version='1.2.0',
    packages=['cqhttp'],
    url='https://github.com/richardchien/python-cqhttp',
    license='MIT License',
    author='Richard Chien',
    author_email='richardchienthebest@gmail.com',
    description='CQHttp Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['Flask', 'requests'],
    python_requires='>=3.5',
    platforms='any',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
