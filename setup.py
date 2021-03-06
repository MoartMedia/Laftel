from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="laftel",
    version="0.0.1",
    description="라프텔(애니메이션) API Wrapper (laftel.net)",
    license="GPL-V3",
    author="LeoK",
    author_email="support@leok.kr",
    url="https://github.com/331leo/laftel",
    download_url="https://github.com/331leo/laftel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["aiohttp"],
    packages=find_packages(),
    keywords=["anime", "laftel", "info", "API", "wrapper"],
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Development Status :: 3 - Alpha',
        #"Development Status :: 5 - Production/Stable",
    ],
)
