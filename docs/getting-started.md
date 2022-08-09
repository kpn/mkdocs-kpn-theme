## About mkdocs

[Mkdocs][mkdocs] is a project that enables you into writing documentation for
your project in a super **fast and easy** way.

First, you have to create a `docs/` folder in the root of your project,
inside it, you can start creating markdown (`.md`) files.

The main file of the documentation is called `index.md`. This can be configured
by configuring the [navigation setting][adding-pages] in your `mkdocs.yml` file.

Once you finish writing your documentation, using the command line,
`mkdocs` will get all of these markdown files and will output a rendered
HTML website to the `site/` folder.

That's it!

## Installation

If you are starting from the ground up, you need to install `mkdocs` in your
project.

```bash
python -m pip install mkdocs mkdocs-kpn
```

## Usage

### Creating a configuration

In the root of your project create a file called `mkdocs.yml`
and put this initial configuration:

```yaml
site_name: <My Website Name>

theme:
  name: kpn

markdown_extensions:
  - codehilite:
      guess_lang: false
```

For more settings check the Full Example at the bottom of the page.

### Add search support

Just add to the `mkdocs.yml` the following:

```yaml
plugins:
  - search:
      prebuild_index: true
```

A search input will appear. The search index is offline, so no backend is required.

### Running commands

```bash
python -m mkdocs build
```

Will output the generated website into a `site/` folder. Remember to add it
to your `.gitignore`, the idea is for CI's to automatically build it.

----

```bash
python -m mkdocs serve
```

This command will run a webserver which will reload your browser as soon as you
make a change. This is useful to see your documentation while you are writing it.

## Full configuration example

Full `mkdocs.yml` example:

```yaml
# Project information
site_name: 'KPN Theme'
site_description: 'A KPN theme for MkDocs'
site_author: 'Jon Doe'

# Repository
repo_name: 'kpn/mkdocs-kpn-theme'
repo_url: https://github.com/kpn/mkdocs-kpn-theme

# Copyright
copyright: 'Copyright &copy; KPN'

# Google Analytics Disabled by default
google_analytics:
  - 'UA-XXXXXXXX-X'
  - 'auto'

extra:
  # Use the repo edit url instead of the link to the repo
  use_edit_url: false

# Extensions
markdown_extensions:
  - admonition
  - codehilite:
      guess_lang: false
  - toc:
      permalink: true
  - footnotes
  - pymdownx.critic
  - pymdownx.emoji
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.tasklist
  - pymdownx.tilde
```

[mkdocs]: https://www.mkdocs.org/
[adding-pages]: https://www.mkdocs.org/#adding-pages

## API Documentation

To document your API we recommend using [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings).
