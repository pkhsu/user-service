# User Service - 用戶管理微服務系統

## 📖 項目概述

這是一個用戶管理微服務系統，提供完整的用戶數據 CRUD 操作 REST API 以及直觀的 Web 管理界面。該系統採用微服務架構設計，可作為大型系統中的用戶域服務組件。

### 🚀 主要功能

- **RESTful API**: 完整的用戶 CRUD 操作接口
- **Web 管理界面**: 基於 Streamlit 的用戶管理後台
- **數據持久化**: MongoDB 資料庫存儲
- **容器化部署**: Docker + Docker Compose 一鍵部署
- **健康檢查**: 內建服務健康監控

### 🏗️ 架構圖

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │   Backend API   │    │    MongoDB      │
│   (Streamlit)   │◄──►│  (Spring Boot)  │◄──►│   (Database)    │
│   Port: 8501    │    │   Port: 8080    │    │   Port: 27017   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ 技術棧

| 組件 | 技術 | 版本 |
|------|------|------|
| **後端** | Spring Boot + Java + Maven | 3.2.0 + JDK 17 |
| **前端** | Python + Streamlit + PyMongo | 3.9+ + 1.30.0 |
| **資料庫** | MongoDB | Latest |
| **容器化** | Docker + Docker Compose | Latest |

## 🚀 快速開始 (Docker 方式 - 推薦)

### 📋 前置條件

確保您的系統已安裝：
- [Docker](https://docs.docker.com/get-docker/) 
- [Docker Compose](https://docs.docker.com/compose/install/)

### ⚡ 一鍵啟動指令

```bash
# 克隆項目 (如果尚未克隆)
git clone <your-repository-url>
cd user-service

# 啟動所有服務
docker-compose up -d
```

### 🌐 服務訪問地址

啟動完成後，您可以通過以下地址訪問各服務：

| 服務 | 地址 | 說明 |
|------|------|------|
| **Web 管理界面** | http://localhost:8501 | 用戶管理後台 |
| **REST API** | http://localhost:8080/api/users | 用戶 API 接口 |
| **健康檢查** | http://localhost:8080/actuator/health | 服務健康狀態 |
| **MongoDB** | localhost:27017 | 資料庫連接 |

### 🔧 停止服務

```bash
# 停止所有服務
docker-compose down

# 停止服務並清除數據卷 (慎用)
docker-compose down -v
```

---

🎉 **恭喜！** 您的用戶管理微服務系統現在已經運行起來了。請打開瀏覽器訪問 http://localhost:8501 開始使用 Web 管理界面。 