# Configuration

In order to enable the features appearing in the extensions website you need
to add them to your `mkdocs.yml` in the `markdown_extensions` list.

```yaml
site_name: KPN Theme
theme:
  name: kpn

repo_url: https://github.com/kpn/mkdocs-kpn-theme

markdown_extensions:
  - admonition
  - codehilite
  - footnotes
  - pymdownx.critic
  - pymdownx.emoji
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.tasklist
  - pymdownx.tilde
```
