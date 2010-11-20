from setuptools import setup, find_packages

setup(
    name="Kirby",
    description="Create websites with Markdown + Jinja2 and upload to Amazon CloudFront.",
    version="0.0.1pre-alpha",
    author="Kyle Fox",
    author_email="kyle.fox@gmail.com",
    url="http://github.com/kylefox/kirby",
    scripts=['bin/kirby'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "setuptools",
        "jinja2",
        "markdown",
        "pyyaml",
        "boto"
    ],
    classifiers=[ # see http://diveintopython3.org/packaging.html#trove
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ]
)