# Spring Boot 應用 Dockerfile
FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:resolve

COPY src ./src

RUN ./mvnw package -DskipTests

ENTRYPOINT ["java", "-jar", "target/user-service-0.0.1-SNAPSHOT.jar"]
