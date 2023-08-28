import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__VERSION__ = "0.1.0"
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Sainath6566"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "sainathsainath990@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__VERSION__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
