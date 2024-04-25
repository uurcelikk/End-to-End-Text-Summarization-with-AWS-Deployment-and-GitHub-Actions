
#  Text Summarization Project with BART
This repository contains code and configurations for an End-to-End Text Summarization with AWS Deployment and GitHub Actions. 

## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py

## Getting Started

# End-to-end Text Summarization Project

This repository contains code and configurations for an end-to-end Text Summarization project. 

1.Clone the Repository:

```bash 
git clone https://github.com/entbappy/End-to-end-Text-Summarization
```

2.Create Conda Environment:

```bash 
conda create -n summary python=3.8 -y
conda activate summary
```

3.Install Dependencies:

```bash 
pip install -r requirements.txt
```

4.Execute the Application:

```bash 
python app.py
```

5. Acces the Web Interface:

Open your web browser and navigate to your localhost address (typically http://127.0.0.1:5000 or similar).
## AWS CICD Deployment with GitHub Actions

### Prerequisites:

* AWS account with IAM user (EC2 and ECR permissions)
* AWS access keys stored as GitHub Secrets

## Deployment Steps:

- **Build Docker Image**: The GitHub Actions workflow builds a Docker image of the application.
- **Push Image to ECR**: The image is pushed to an AWS Elastic Container Registry (ECR) repository.
- **Launch EC2 Instance**: A new EC2 instance is launched (or an existing one is used).
- **Pull Image from ECR**: The Docker image is pulled from ECR to the EC2 instance.
- **Run Docker Container**: The text summarization application runs within the container on EC2.
## Lisans

[MIT](https://choosealicense.com/licenses/mit/)

  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

  
