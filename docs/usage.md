# Markdown

Markdown is a simple language that will become HTML.

The syntax is quite simple, use this [cheatsheet](cheatsheet) as reference.

Coming up next we'll see some examples

## Code block

In order to add a code block you need to wrap your coude around 3 backticks

    ```python
    @requires_authorization(roles=["ADMIN"])
    def somefunc(param1='', param2=0):
        r'''A docstring'''
        if param1 > param2: # interesting
            print 'Gre\'ater'
        return (param2 - param1 + 1 + 0b10l) or None

    class SomeClass:
        pass

    >>> message = '''interpreter
    ... prompt'''
    ```

## Image

```text
![alternative text](https://www.kpn.com/public/images/logos/logo-kpn-groot.png)
```

![alternative text](https://www.kpn.com/public/images/logos/logo-kpn-groot.png)


## Code inside `table`

| Example | Bla      |
| ------- | -------- |
| `name`  | `String` |

## Code inside a `list`

- `name`
- `list`

## Quote


> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut tortor sed lorem auctor vulputate id hendrerit quam. Integer maximus molestie elit, non elementum libero rutrum ac. Suspendisse a gravida massa, vitae ullamcorper urna. Quisque varius finibus leo, et ornare est bibendum et. Donec feugiat vitae ipsum fringilla volutpat. Duis hendrerit iaculis pellentesque. Nullam sed egestas nisi. Proin aliquet faucibus mi lacinia maximus. Integer urna ligula, malesuada in purus et, cursus tincidunt tortor. Donec et nunc consectetur, gravida nulla eu, viverra lorem. Nullam suscipit nibh sed nisl fringilla, sit amet tristique ante vulputate. Sed ultrices purus vel erat lacinia pellentesque. Phasellus elit mi, auctor eget nisl vehicula, sollicitudin ultrices risus. Etiam venenatis tempus arcu at dignissim.

[cheatsheet]: https://www.markdownguide.org/cheat-sheet/
