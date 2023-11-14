## Tạo/Xóa database

Mở file mydb.py để thực hiện xóa database cũ và tạo database mới

```bash
python mydb.py
```

## Tạo bảng từ các model

```bash
python manage.py makemigrations
python manage.py migrate
```

## Tạo superuser

```bash
python manage.py createsuperuser
```

## Khởi động server

```bash
python manage.py runserver
```

Truy cập vào [http://127.0.0.1:8000](http://127.0.0.1:8000/)

## Sửa user và password trong mydb.py

## Sửa file settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library',
        'USER': '[your_dbUser]',
        'PASSWORD': '[your_dbPassword]',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

## Nếu bị lỗi "Could not build wheels for mysqlclient, ..." khi install mysqlclient:
## Thêm vào đầu file settings.py

import pymysql
pymysql.version_info = (1, 4, 6, 'final', 0)  # (major, minor, micro, releaselevel, serial)
pymysql.install_as_MySQLdb()