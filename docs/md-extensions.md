---
title: Extensions
---

## Admonition - Block styled content

```yaml
# location: mkdocs.yml
markdown_extensions:
  - admonition
```

!!! info "Info"
    This is an admonition box.

!!! important "Important"
    This is an admonition box.

!!! warning "Warning"
    This is an admonition box.

!!! success "Success"
    This is an admonition box.

!!! check ""
    This is an admonition box without a title.

!!! danger "Danger"
    This is an admonition box.

!!! danger "Failure"
    This is an admonition box.

```bash
!!! info "Info"
    This is an admonition box.

!!! important "Important"
    This is an admonition box.

!!! warning "Warning"
    This is an admonition box.

!!! success "Success"
    This is an admonition box.

!!! check ""
    This is an admonition box without a title.

!!! danger "Danger"
    This is an admonition box.

!!! danger "Failure"
    This is an admonition box.
```

## Language highlight

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
```

```python
def fun():
    print("holis")
```

```bash
kubectl apply -f manifest.yml
```

## Line highlight

You can highlight using `the output is like:`

## Footnotes

```yaml
# location: mkdocs.yml
markdown_extensions:
  - footnotes
```

All the other pages are for[^1] demonstration purposes
with the navigation only.

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

```bash
All the other pages are for[^1] demonstration purposes
with the navigation only.

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

## Keyboard

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.keys
```

Use keyboard values: ++ctrl+alt+delete++

```bash
++ctrl+alt+delete++
```

## Critics

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.critic
```

To insert or remove text you can use ==\{\+\+insert me++\}== and ==\{\--remove me-\-\}== respectively. You can also denote a substitution with ==\{\~~substitute this~\>with this~~\}==.

You can also highlight specific text with ==\{\==highlight me=\=\}==. Or even comment, which is generally done by highlighting text and following it with a comment: ==\{\==highlight me==\}==\{\>\>Add a comment<<\}==.

----

To insert or remove text you can use {++insert me++} and {--remove me--} respectively. You can also denote a substitution with {~~substitute this~>with this~~}.

You can also highlight specific text with {==highlight me==}. Or even comment, which is generally done by highlighting text and following it with a comment: {==highlight me==}{>>Add a comment<<}.

## Emojis

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.emoji
```

You can also use emojis: :smile: :heart:

```bash
:smile: :heart:
```

## Mark

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.mark
```

Ability to add `<mark></mark>` by using `==hello==` ==hello==

## Smart symbols

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.smartsymbols
```

KPN (tm)

I'd say +/-8

```bash
KPN (tm)
I'd say +/-8
```

## Tasklist

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.tasklist
```

Task List

- [x] item 1
  - [x] item A
  - [ ] item B
        more text
    - [x] item a
    - [ ] item b
    - [x] item c
  - [x] item C
- [ ] item 2
- [ ] item 3

## Tilde

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.tilde
```

~~Delete me~~

CH~3~CH~2~OH

text~a\ subscript~

```bash
~~Delete me~~

CH~3~CH~2~OH

text~a\ subscript~
```

## More

Read more about the extensions in [pymdown-extensions][pymdown-extensions]

[pymdown-extensions]: https://facelessuser.github.io/pymdown-extensions/extensions/

## Content tabs

```yaml
# location: mkdocs.yml
markdown_extensions:
  - pymdownx.tabbed
```

```md
=== "JS"

    ```js
    date = new Date()
    ```

=== "Python"

    ```python
    import datetime
    datetime.datetime.now()
    ```

=== "List"
    More Markdown **content**.

    - list item a
    - list item b
```

=== "JS"
    ```
    date = new Date()
    ```

=== "Python"
    ```python
    import datetime
    datetime.datetime.now()
    ```

=== "List"
    More `Markdown` **content**.

    - list item a
    - list item b


## PlantUML diagrams

This is a C4 model example

```plantuml format="png" classes="uml myDiagram" alt="My super diagram placeholder" title="C4 Model"
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define DEVICONS https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/devicons
!define FONTAWESOME https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/font-awesome-5
!include DEVICONS/react.puml
!include DEVICONS/python.puml
!include DEVICONS/postgresql.puml
!include FONTAWESOME/users.puml

LAYOUT_WITH_LEGEND()

Person(user, "Customer", "People that need products", $sprite="users")
Container(spa, "SPA", "react", "The main interface that the customer interacts with", $sprite="react")
Container(api, "API", "python", "Handles all business logic", $sprite="python")
ContainerDb(db, "Database", "Postgres SQL", "Holds product, order and invoice information", $sprite="postgresql")

Rel(user, spa, "Uses", "https")
Rel(spa, api, "Uses", "https")
Rel_R(api, db, "Reads/Writes")
@enduml
```

````
```plantuml format="png" classes="uml myDiagram" alt="My super diagram placeholder" title="C4 Model"
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define DEVICONS https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/devicons
!define FONTAWESOME https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/font-awesome-5
!include DEVICONS/react.puml
!include DEVICONS/python.puml
!include DEVICONS/postgresql.puml
!include FONTAWESOME/users.puml

LAYOUT_WITH_LEGEND()

Person(user, "Customer", "People that need products", $sprite="users")
Container(spa, "SPA", "react", "The main interface that the customer interacts with", $sprite="react")
Container(api, "API", "python", "Handles all business logic", $sprite="python")
ContainerDb(db, "Database", "Postgres SQL", "Holds product, order and invoice information", $sprite="postgresql")

Rel(user, spa, "Uses", "https")
Rel(spa, api, "Uses", "https")
Rel_R(api, db, "Reads/Writes")
@enduml
```
````

Add to `mkdocs.yml`

```yaml
markdown_extensions:
- plantuml_markdown:
      server: http://www.plantuml.com/plantuml
```

Check `plantum-markdown` is installed by running: `pip freeze | grep plantuml-markdown`

If not present, run:

```bash
pip install -U plantuml-markdown
```

[VS code extension for PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

## Mermaid diagrams

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

You may need to add the following to your configuration if it doesn't work right away

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:pymdownx.superfences.fence_div_format
extra_javascript:
  - https://unpkg.com/mermaid@8.13.5/dist/mermaid.min.js
```
