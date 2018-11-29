import setuptools

with open('README.md', 'r') as fh:
    long_desc = fh.read()

setuptools.setup(
    name="Pylarm",
    version="1.0.10",
    author="Brandon Benefield",
    author_email="bsquared18@gmail.com",
    description="A CLI to set alarms",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/bbenefield89/PythonAlarm",
    packages=setuptools.find_packages(),
    py_modules=["Pylarm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'bin/Pylarm'
    ]
)
