from handlers.handlers import Login


url_patterns = [
    ("/v1/login/?([^/]+)?", Login, None, "login"),
]