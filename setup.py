import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="text-summarization",
    version="0.0.0",
    author="uurcelikk",
    author_email="uurcelikk98@gmail.com",
    description="An end-to-end text summarizer package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uurcelikk/Text-Summarization.git",
    project_urls={
        "Bug Tracker": "https://github.com/uurcelikk/Text-Summarization.git/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
