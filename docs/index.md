# KPN Theme

Theme for your favorite documentation tool:

- [MkDocs v1]
- [ProperDocs]
- [Zensical]

[MkDocs v1]: (https://www.mkdocs.org/)
[ProperDocs]: (https://properdocs.org/)
[Zensical]: (https://zensical.org/)

## Create a Beautiful KPN Project Documentation

KPN Theme is a theme for [MkDocs v1], [ProperDocs] or [Zensical]. These are excellent static site generators geared towards project documentation.
It is built using [KPN Styles][kpn_styles].

## Quickstart

Install the latest version of KPN theme with pip (after your favorite doc library):

```bash
pip install mkdocs-kpn
```

Append the following line to your project's `mkdocs.yml`:

```yaml
theme:
  name: 'kpn'
```

## What to Expect

- Responsive design and fluid layout for all kinds of screens and devices,
designed to serve your project documentation in a user-friendly way.
- Support for a lot of Markdown extensions.

## Change Repo Icon

```yaml
# options: github | gitlab | bitbucket | gitea
extra:
  repo_icon: 'github'
```

## Add Version to Site

Edit `mkdocs.yml` with

```yaml
extra:
  version:
    provider: 'manual'
    version: 1.2.2
```

[kpn_styles]: https://style.kpn.com/
