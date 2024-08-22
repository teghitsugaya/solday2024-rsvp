## To Re-Build this Apps
    git clone https://github.com/teghitsugaya/solday2024-rsvp.git
    cd solday2024-rsvp
    docker build -t solday-rsvp:latest .

    ###push to dockerhub
    docker login
    docker tag solday-rsvp:latest teghitsugaya/solday-rsvp:latest
    docker push teghitsugaya/solday-rsvp:latest
   
## Deploy to Kubernetes Cluster
  ### Deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: solday-rsvp-deployment
      labels:
        app: solday-rsvp
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: solday-rsvp
      template:
        metadata:
          labels:
            app: solday-rsvp
        spec:
          containers:
          - name: solday-rsvp
            image: teghitsugaya/solday-rsvp
            ports:
            - containerPort: 5000
            env:
            - name: MYSQL_HOST
              value: "<ip_address/domain-db>"
            - name: MYSQL_PORT
              value: "<mysql_port_db>"
            - name: MYSQL_USER
              value: "<user_db>"
            - name: MYSQL_PASSWORD
              value: "<mysql_pass>"
            - name: MYSQL_DATABASE
              value: "<mysql_db>"
  
  ### execute
    kubectl apply -f deployment.yaml
    kubectl expose deployment solday-rsvp --type=NodePort --port=80 --target-port=5000
