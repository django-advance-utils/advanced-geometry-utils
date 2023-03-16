import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="advanced-geometry-utils",
    version="0.0.1",
    author="Tom Turner",
    description="A collection of geometry utils for 3d and 2d",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/django-advance-utils/advanced-geometry-utils",
    include_package_data=True,
    packages=['geometry_utils',
              'geometry_utils.three_d',
              'geometry_utils.two_d'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
