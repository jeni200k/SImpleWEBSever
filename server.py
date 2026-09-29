from django.http import HttpResponse


def home(request):

    html = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>My Webpage</title>

        <style>
            body {
                font-family: Arial;
                background-color: lightpink;
                text-align: center;
                padding-top: 150px;
            }

            h1 {
                color: darkblue;
                font-size: 40px;
            }

            h2 {
                color: purple;
                font-size: 28px;
            }
        </style>
    </head>

    <body>

        <h1>Welcome to My Webpage</h1>

        <h2>Name: Jeni J</h2>

        <h2>Register Number: YOUR REGISTER NUMBER</h2>

    </body>
    </html>
    """

    return HttpResponse(html)