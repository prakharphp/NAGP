### 1. Get All Resources in Current Namespace

kubectl get all
This shows:

Pods
Services
Deployments
ReplicaSets
StatefulSets

### 2. View Resources Across All Namespaces
kubectl get all --all-namespaces

### 3. Check PersistentVolume and PersistentVolumeClaim
kubectl get pvc
kubectl get pv

### 4. Check Ingress Resources
kubectl get ingress
kubectl describe ingress fastapi-ingress

### 5. Check Namespaces (if you're using custom namespaces)
kubectl get namespaces
To list resources in a specific namespace:

kubectl get all -n <namespace-name>

### 6. Check Ingress-NGINX Components
kubectl get all -n ingress-nginx

### 7. Describe Resources for More Details
kubectl describe pod <pod-name>
kubectl describe service <service-name>
kubectl describe deployment <deployment-name>