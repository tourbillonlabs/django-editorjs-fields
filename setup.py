import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-editorjs-fields", # Replace with your own username
    version="0.1.0",
    author="Tourbillon Labs",
    author_email="hello@tourbillonlabs.com",
    description="editorjs.io for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tourbillonlabs/django-editorjs-fields.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
