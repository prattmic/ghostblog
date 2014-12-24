Python Ghost Library
====================

`ghostblog` is a Python module for accessing the
[Ghost](https://github.com/TryGhost/Ghost) API.

This is based around Ghost's 'private' admin API, documented on their
[wiki](https://github.com/TryGhost/Ghost/wiki/%5BWIP%5D-API-Documentation).

This API is not considered public, and is intended only for use on the Ghost
admin console.  As such, it requires authentication to access, and may break on
future versions of Ghost.  Currently, this module has only been tested on Ghost
**0.5.7**.

We can use `ghostblog` to get all of the posts in Ghost:

```python
>>> import ghostblog
>>> g = ghostblog.Ghost('https://example.com/blog/', 'user@example.com', 'pass')
>>> g.posts()['posts'][0]['title']
u'Welcome to Ghost'
```
