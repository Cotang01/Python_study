from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request: HttpRequest):
    logger.info(f"Request: {request}, 'home' page has been visited")
    return HttpResponse(
        """<!DOCTYPE html>
<html>
<body>

<h1>Home page</h1>

<p>Main content</p>

</body>
</html>""")


def about(request: HttpRequest):
    logger.info(f"Request: {request}, 'about' page has been visited")
    return HttpResponse("""<!DOCTYPE html>
<html>
<body>

<h1>About us page</h1>

<p>This is my first django project</p>

</body>
</html>""")
