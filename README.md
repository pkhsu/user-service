# User Service 用户管理系统

这是一个基于 Spring Boot 和 Streamlit 的用户管理系统。

## 功能特性
- 用户信息管理 (CRUD)
- 用户状态切换
- 前后端分离架构

## 技术栈
- 后端: Java Spring Boot
- 前端: Python Streamlit
- 数据库: MongoDB

## 快速开始
1. 安装依赖:
```bash
# 后端
mvn install

# 前端
pip install -r frontend/requirements.txt
```

2. 启动服务:
```bash
docker-compose up
```

3. 访问应用:
- 后端 API: http://localhost:8080
- 前端界面: http://localhost:8501

## 项目结构
```
user-service/
├── frontend/    # Streamlit 前端
├── src/         # Spring Boot 后端
└── memory-bank/ # 项目文档
