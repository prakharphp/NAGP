# FastAPI App on GKE with PostgreSQL and Ingress

This project deploys a FastAPI application backed by PostgreSQL to Google Kubernetes Engine (GKE), using:

* **FastAPI** as the web framework
* **PostgreSQL** as the database
* **GKE (Google Kubernetes Engine)** for hosting
* **NGINX Ingress Controller** for routing traffic
* **Persistent Volumes** for database storage

---

## 🔧 Project Structure

```
.
├── app/
│   └── main.py                    # FastAPI app
├── k8s/
│   ├── postgres-deployment.yaml
│   ├── postgres-pvc.yaml
│   ├── fastapi-deployment.yaml
│   ├── fastapi-service.yaml
│   └── ingress.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Deployment Steps

### 1. Build and Push Docker Image

```bash
docker build -t prakhardockerhub/fastapi-sqlite-app:latest .
docker push prakhardockerhub/fastapi-sqlite-app:latest
```

### 2. Create GKE Cluster

```bash
gcloud container clusters create-auto fastapi-cluster --region=us-central1
```

### 3. Connect `kubectl` to the Cluster

```bash
gcloud container clusters get-credentials fastapi-cluster --region=us-central1
```

### 4. Deploy PostgreSQL

```bash
kubectl apply -f k8s/postgres-pvc.yaml
kubectl apply -f k8s/postgres-deployment.yaml
```

### 5. Deploy FastAPI Application

```bash
kubectl apply -f k8s/fastapi-deployment.yaml
kubectl apply -f k8s/fastapi-service.yaml
```

### 6. Install NGINX Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

Verify the controller is running:

```bash
kubectl get pods -n ingress-nginx
```

### 7. Deploy Ingress Resource

```bash
kubectl apply -f k8s/ingress.yaml
```

Get the external IP:

```bash
kubectl get ingress
```

Access the app:

* Swagger UI: `http://<EXTERNAL-IP>/docs`
* Root (Healthcheck) URL: `http://<EXTERNAL-IP>/`

---

## 🛠 Debugging Tips

Check logs:

```bash
kubectl logs <pod-name>
kubectl describe ingress fastapi-ingress
```

Port forward (for local testing):

```bash
kubectl port-forward svc/fastapi-service 8000:8000
```

Then visit:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔗 Code Repository

[👉 GitHub Repository – prakharphp/NAGP](https://github.com/prakharphp/NAGP)

---

## 🐳 Docker Hub Image

[👉 Docker Hub – prakhardockerhub/fastapi-sqlite-app](https://hub.docker.com/repository/docker/prakhardockerhub/fastapi-sqlite-app/general)

Pull the image using:

```bash
docker pull prakhardockerhub/fastapi-sqlite-app:latest
```
