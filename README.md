# Miscellaneous Ansible filters

## email

Check if a string is a valid e-mail address.

```python
{{ 'firstname.lastname@gmail.com' | email }}
# => True

{{ 'localhost' | email }}
# => False

{{ ['localhost', 'firstname.lastname@gmail.com'] | email }}
# => [False, True]
```

## hostname

Check if a string is a valid hostname (including FQDNs).

```python
{{ 'localhost' | hostname }}
# => True

{{ 'my_host' | hostname }}
# => False

{{ 'drive.google.com' | hostname }}
# => True

{{ ['localhost', 'google.25'] | hostname }}
# => [True, False]
````

## url

Break an URL string up in components (using [`urlparse`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse) Python function):

Attribute  | Value                              | Value if not present
---------- | ---------------------------------- | --------------------
`scheme`   | URL scheme specifier               | _scheme_ parameter
`netloc`   | Network location part              | empty string
`path`     | Hierarchical path                  | empty string
`params`   | Parameters for last path element   | empty string
`query`    | Query component                    | empty string
`fragment` | Fragment identifier                | empty string
`username` | User name                          | `None`
`password` | Password                           | `None`
`hostname` | Host name (lower case)             | `None`
`port`     | Port number as integer, if present | `None`

```python
{{ 'https://user:password@hostname.com:8080/path/page.html?param1=arg1&param2=arg2#fragment' | urlparse }}
# => {'scheme': 'https', 'netloc': 'user:password@hostname.com:8080', 'path': '/path/page.html', 'params': '', 'query': 'param1=arg1&param2=arg2', 'fragment': 'fragment', 'username': 'user', 'password': 'password', 'hostname': 'hostname.com', 'port': 8080}

{{ 'https://user:password@hostname.com:8080/path/page.html?param1=arg1&param2=arg2#fragment' | urlparse('hostname') }}
# => 'hostname.com'

{{ 'https://user:password@hostname.com:8080/path/page.html?param1=arg1&param2=arg2#fragment' | urlparse('query') }}
# => 'param1=arg1&param2=arg2'

{{ 'https://user:password@hostname.com:8080/path/page.html?param1=arg1&param2=arg2#fragment' | urlparse('port') }}
# => 8080
```