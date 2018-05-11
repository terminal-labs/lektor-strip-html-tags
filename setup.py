import ast
import io
import re

from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_strip_html_tags.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    description=description,
    keywords='Lektor plugin html static-site regex jinja2 jinja filter',
    license='BSD-3-Clause',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-strip-html-tags',
    py_modules=['lektor_strip_html_tags'],
    url='https://github.com/terminal-labs/lektor-strip-html-tags',
    version='0.3',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'lektor.plugins': [
            'strip-html-tags = lektor_strip_html_tags:StripHTMLTagsPlugin',
        ]
    }
)
