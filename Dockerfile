# 使用官方Python运行时作为父镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器内的/app
COPY . /app

# 安装FastAPI和uvicorn
RUN pip install fastapi uvicorn

# 命令行运行FastAPI应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
