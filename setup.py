from setuptools import setup

setup(
    name='lektor-strip-html-tags',
    version='0.2',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    description = u'Strip HTML tags, effectively turning HTML into plain text.',
    license='BSD-3-Clause',
    py_modules=['lektor_strip_html_tags'],
    entry_points={
        'lektor.plugins': [
            'strip-html-tags = lektor_strip_html_tags:StripHTMLTagsPlugin',
        ]
    }
)
