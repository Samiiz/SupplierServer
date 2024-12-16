#!/bin/bash

# 1. install git, python 3.12
sudo yum update -y
sudo yum install -y git python3.12 nginx
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo yum install -y nodejs

# python version
python3.12 --version

# 2. git clone
REPO_URL=">3<repository_address"
echo "Cloning repository..."
git clone $REPO_URL
REPO_NAME=$(basename "$REPO_URL" .git)

# 3. virtual environment setting
echo "Creating and activating Python virtual environment..."
python3.12 -m venv .venv
source .venv/bin/activate

cd $REPO_NAME

# 4. install pkages
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping package installation."
fi


# 5. Django initialization
if [ -f "manage.py" ]; then
    echo "Running Django migrations and server setup..."

    # db migration
    python manage.py makemigrations
    python manage.py migrate

    # create super user
    echo "Creating superuser..."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', '1234')" | python manage.py shell

    # django runserver(background)
    nohup python manage.py runserver 0.0.0.0:8000 > django.log 2>&1 &
else
    echo "manage.py not found. Please check your Django project structure."
fi


# 6. create nginx conf
NGINX_CONF="/etc/nginx/conf.d/app.conf"
sudo bash -c "cat > $NGINX_CONF" << EOF
server {
    listen 80;
    server_name 3.25.100.75;  # EC2 퍼블릭 IP 또는 도메인 이름

    # React 앱의 정적 파일 서빙
    location / {
        root /home/ec2-user/SuppilerServer/web/build;  # React 빌드된 파일 위치
        try_files $uri /index.html;
    }

    # Django API 요청을 Gunicorn으로 전달
    location /api/ {
        proxy_pass http://127.0.0.1:8000;  # Gunicorn 서버의 주소
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    # Django 정적 파일 서빙 (필요시)
    location /static/ {
        alias /home/ec2-user/your_project_name/static/;  # Django의 정적 파일 경로
    }

    # Django 미디어 파일 서빙 (필요시)
    location /media/ {
        alias /home/ec2-user/your_project_name/media/;  # Django의 미디어 파일 경로
    }
}

EOF

# 7. nginx restart
echo "Restarting Nginx..."
sudo nginx -t && sudo systemctl restart nginx

# 8. complate
echo "Django development server is running"
