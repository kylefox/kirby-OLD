def render_path(path):
    try:
        menu = '<p><a href="/">home</a> | <a href="/about">about</a> | <a href="/newp">not found</a></p>'
        return {
            '/': '<h1>Homepage</h1> %s' % menu,
            '/about': '<h1>about</h1> %s' % menu,
            '/favicon.ico': ''
        }[path]
    except KeyError:
        return None