# MLOps Docker Compose Watch Task

This project demonstrates how to use **Docker Compose** to set up and run a multi-container application for monitoring and logging changes using a **watch service**.

---

## 📦 Project Overview

* **Goal:** Automatically detect changes in files or directories and reflect them inside a Dockerized environment.
* **Core Tools:**

  * `Docker`
  * `Docker Compose`
  * File system **watcher**
  * Python-based app or script (inside container)

---

## 🛠 Technologies Used

* Docker
* Docker Compose
* Python
* Watchdog (Python file system monitoring library)

---

## 📁 Directory Structure (Simplified)

```
mlops-docker-compose-watch-task/
├── backend/
│   ├── Dockerfile
    ├── app.py
    └── requirements.txt
├── frontend/
│   ├── Dockerfile
    ├── app.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ushna-Nadeem/mlops-docker-compose-watch-task.git
cd mlops-docker-compose-watch-task
```

### 2️⃣ Build and Run Containers

```bash
docker-compose up --build
```

> This will build the image and start the container with file watching enabled.

### 3️⃣ Make File Changes

Edit `backend/app.py` or add files to see the watch service in action (automatically reloads or logs the change).

---

## ✅ Expected Behavior

* File changes are detected inside the container.
* Logs show updates as they happen.
* Can be extended to trigger scripts, tests, or retraining pipelines.

---

## 🧹 Cleanup

```bash
docker-compose down
```

---

## 📌 Notes

* File watching is implemented using Python’s `watchdog` module.
* Ideal for automating workflows in an MLOps or DevOps pipeline.
