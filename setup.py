import pathlib
from setuptools import find_packages, setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="reverse",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Reverse",
    long_description=README,
    long_description_content_type="text/markdown",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    url = 'https://github.com/sukhbinder/revese',
    keywords = ["reverse", "games",],
    entry_points={
        'console_scripts': ['revgame = reverse.reversei:main', ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],

)
