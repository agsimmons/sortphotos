from setuptools import setup, find_packages

setup(
    name="sortphotos",
    version="1.0.0",
    description="Organizes photos and videos into folders using date/time information ",
    author="Andrew Ning",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["sortphotos = sortphotos.sortphotos:main",]},
)
