from re import findall
from setuptools import setup, find_packages


with open("pytdbot/__init__.py", "r") as f:
    version = findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name="Pytdbot",
    version=version,
    description="Easy-to-use TDLib wrapper for Telegram bots.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="AYMEN Mohammed",
    author_email="let.me.code.safe@gmail.com",
    url="https://github.com/pytdbot/client",
    license="MIT",
    python_requires=">=3.9",
    project_urls={
        "Source": "https://github.com/pytdbot/client",
        "Tracker": "https://github.com/pytdbot/client/issues",
    },
    packages=find_packages(exclude=["examples"]),
    package_data={
        "pytdbot": [
            "lib/*.so",
        ],
    },
    keywords=["telegram", "tdlib", "bot", "telegram-client", "telegram-bot", "bot-api"],
)
