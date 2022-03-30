from setuptools import find_packages
from setuptools import setup

setup(
    name="django-invitations",
    packages=find_packages(),
    package_data={"invitations": ["templates/*.*"]},
    include_package_data=True,
    zip_safe=False,
    version="1.9.3",
    description="Generic invitations app with support for django-allauth",
    author="https://github.com/bee-keeper",
    author_email="none@none.com",
    url="https://github.com/jazzband/django-invitations.git",
    keywords=["django", "invitation", "django-allauth", "invite"],
    license="GPL-3.0-only",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Topic :: Internet",
        "Framework :: Django",
        "Framework :: Django:: 3.2",
        "Framework :: Django:: 4.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GPL-3.0-only",
    ],
)
