from handlers.handlers import Login, Student, Country


url_patterns = [
    ("/v1/login/?([^/]+)?", Login, None, "login"),
    ("/v1/student/?([^/]+)?", Student, None, "student"),
    ("/v1/country/?([^/]+)?", Country, None, "country"),
]