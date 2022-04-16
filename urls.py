from handlers.handlers import Login, Student, Country
from handlers.upload import Upload


url_patterns = [
    ("/v1/login/?([^/]+)?", Login, None, "login"),
    ("/v1/student/?([^/]+)?", Student, None, "student"),
    ("/v1/country/?([^/]+)?", Country, None, "country"),
    ("/v2/upload", Upload, None, "upload_v2"),
]