# Spring Boot 應用 Dockerfile
FROM eclipse-temurin:17-jdk-jammy

# 安裝 Maven 和 curl
RUN apt-get update && apt-get install -y maven curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 先複製依賴相關檔案，利用 Docker layer caching
COPY pom.xml ./

# 解決依賴，這步會被 cache
RUN mvn dependency:resolve

# 複製原始碼
COPY src ./src

# 建構應用，跳過測試以加速建構
RUN mvn package -DskipTests

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# 運行應用
ENTRYPOINT ["java", "-jar", "target/user-service-0.0.1-SNAPSHOT.jar"]
