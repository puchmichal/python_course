from setuptools import setup, find_packages

setup(
    name="weather-check",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "idna==2.10",
        "requests==2.25.1",
        "urllib3==1.26.2",
    ],
    entry_points={"console_scripts": ["weather-check=weather_check.weather_check:main"]},
)
