title: How to print a date with Python
subtitle: Printing according to RFC1123 is not as easy as you might think.
author: Jonathan Smelquist
date: 2010-11-17

- - -

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi vel risus mi, sed placerat diam. Aliquam erat volutpat. Nullam tincidunt semper nunc, vitae cursus nibh semper in. Mauris ac arcu ac lectus pretium porta ut sit amet lorem. Nunc ligula orci, lacinia ac dictum eu, adipiscing ac purus. Duis faucibus scelerisque ultricies. Phasellus aliquet nisl eu diam elementum placerat. Etiam a risus et dolor lacinia placerat eu nec sapien. Mauris vel convallis justo. Donec ut dui ut metus varius blandit. Aenean varius elementum nisl, at porta nunc tristique sed. Nulla ac arcu turpis. Vivamus ac ipsum metus, eu rhoncus nisi.

    def expiry_date():
        from wsgiref.handlers import format_date_time
        from datetime import datetime, timedelta
        from time import mktime
        future_date = datetime.now() + timedelta(days=10 * 365)
        stamp = mktime(future_date.timetuple())
        return format_date_time(stamp)