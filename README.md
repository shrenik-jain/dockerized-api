# dockerized-api

This repository contains the source code for dockerizing a Flask API and MongoDB seperately, connecting the two services, and finally deploying the dockerized container. 

## Repo-Structure
```
├── app.py
├── docker-compose.yml
├── Dockerfile
├── documentation
│   ├── dockerizing_steps.txt
│   └── kubernetes_steps.txt
├── mongo_utils
│   ├── delete_in_range.py
│   ├── percent_alert_city.py
│   └── percent_each_alert.py
├── README.md
├── requirements.txt
└── yamls
    ├── docker_database_api_svc.yaml
    ├── docker_database_api.yaml
    ├── mongo-pvc.yaml
    ├── mongo-pv.yaml
    ├── mongo-svc.yaml
    └── mongo.yaml
```

## Usage
Refer to the `documentation` directory for usage and stepwise implementation.
