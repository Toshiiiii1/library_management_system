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