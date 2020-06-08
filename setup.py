import setuptools

setuptools.setup(
    name="bitcommit",
    version='0.1.0',
    url="https://github.com/sachin235/bitcommit",
    author="Sachin Singla",
    description="Jupyter extension to enable user push notebooks to a bitbucket repo",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'bitcommit': ['static/*']},
)
