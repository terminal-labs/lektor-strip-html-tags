# lektor-strip-html-tags

This is a simple Lektor plugin that creates a template filter to remove HTML tags from a string. The use it was created for was to do processing on HTML outputted from a Markdown content field. The Markdown is rendered into HTML, and this filter can turn that into simple text, which was then passed to the [lektor-natural-language](https://github.com/terminal-labs/lektor-natural-language) filters to get keywords, unsullied by things like `<div>` tags.

Example usage:

`{{ this.body|striphtmltags }}`

```jinja
{% set var = '<p><strong>Hello</strong>World!</p>' %}
{{ var|striphtmltags }}

```

The last example will render as "Hello World!"
