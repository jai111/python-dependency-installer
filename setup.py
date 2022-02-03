from setuptools import setup


setup(
    name="jb",
    version="1.0.0",
    description="Tool for installing Python packages.",
    license="MIT",
    author="Jai Bajpai",
    author_email="bajpaijai51@gmail.com",
    packages=["jb"],
    entry_points={
        'console_scripts': ['jb=jb.command_line:main'],
    },
    install_requires=[
        "click==8.0.3",
        "colorama==0.4.4",
        "commonmark==0.9.1",
        "importlib-metadata==4.10.1",
        "Pygments==2.11.2",
        "rich==11.1.0",
        "typer==0.4.0",
        "typing-extensions==4.0.1",
        "zipp==3.7.0",
    ],
    python_requires=">=3.7",
)
