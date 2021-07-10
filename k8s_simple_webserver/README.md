a WYSIWYG guide shows you how to manually set up a Kubernetes cluster using microk8s on Ubuntu 20.04

#### Prerequisites:
- Ubuntu 20.04
- Python >= 3.6
- Docker 
    - $ curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
    - Dockerfile based on nginx:stable-alpine, simply copies index.html into the container and expose port 8085

- MicroK8s install using linux guide at: [microk8s](https://microk8s.io/)
    > "Being a snap it runs all Kubernetes services natively while packing the entire set of libraries and binaries needed." 
----
#### Installation:
- Clone the repo
    - docker build -t kuzishai/ngine-test:1.3 .
    - microk8s kubectl apply -f k8s-deploy.yaml
    - $ bash init.sh
        - to get live pod IP
        - to install python requests_html package 
    - $ python3 test.py