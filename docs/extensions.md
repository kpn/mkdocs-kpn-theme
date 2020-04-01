---
title: Extensions
---
## Admonition - Block styled content

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

## Codehilite - Language highlight

```python
def fun():
    print("holis")
```

```bash
some comment
```

## Line highlight

You can highlight using `the output is like:`

## Footnotes

All the other pages are for[^1] demonstration purposes
with the navigation only.

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

```bash
All the other pages are for[^1] demonstration purposes
with the navigation only.

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

## Keyboard

Use keyboard values: ++ctrl+alt+delete++

```bash
++ctrl+alt+delete++
```

## Critics

To insert or remove text you can use ==\{\+\+insert me++\}== and ==\{\--remove me-\-\}== respectively. You can also denote a substitution with ==\{\~~substitute this~\>with this~~\}==.

You can also highlight specific text with ==\{\==highlight me=\=\}==. Or even comment, which is generally done by highlighting text and following it with a comment: ==\{\==highlight me==\}==\{\>\>Add a comment<<\}==.

----

To insert or remove text you can use {++insert me++} and {--remove me--} respectively. You can also denote a substitution with {~~substitute this~>with this~~}.

You can also highlight specific text with {==highlight me==}. Or even comment, which is generally done by highlighting text and following it with a comment: {==highlight me==}{>>Add a comment<<}.

## Emojis

You can also use emojis: :smile: :heart:

```bash
:smile: :heart:
```

## Mark

Ability to add `<mark></mark>` by using `==hello==` ==hello==

## Smart symbols

KPN (tm)

I'd say +/-8

```bash
KPN (tm)
I'd say +/-8
```

## Tasklist

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

~~Delete me~~

CH~3~CH~2~OH

text~a\ subscript~

```
~~Delete me~~

CH~3~CH~2~OH

text~a\ subscript~
```

## More

Read more about the extensions in [pymdown-extensions][pymdown-extensions]

[pymdown-extensions]: https://facelessuser.github.io/pymdown-extensions/extensions/