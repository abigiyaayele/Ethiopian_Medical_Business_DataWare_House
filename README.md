# Ethiopian Medical Business Data Warehouse

## Project Summary

This project involves building a data warehouse to store data on Ethiopian medical businesses scraped from Telegram channels. The project includes developing data scraping and collection pipelines, data cleaning and transformation pipelines, implementing object detection using YOLO, and designing and implementing the data warehouse. The objective is to centralize and analyze data to gain valuable insights, leading to better decision-making.

## Table of Contents

- [Overview](#Overview)
- [Introduction](#Introduction)
- [Objective](#Objective)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Data Scraping and Collection](#Data-Scraping-and-Collection-Pipeline)
- [Data Cleaning and Transformation](#data-cleaning-and-transformation)
- [Object Detection using YOLO](#object-detection-using-yolo)
- [Expose the Collected Data Using Fast API](#Expose-the-Collected-Data-Using-Fast-API)
- [Deliverables](#Deliverables)
- [Competency Mapping](#competency-mapping)
- [References](#references)

## Overview

The data warehouse aims to enhance data analysis by centralizing data, allowing comprehensive analyses to identify trends, patterns, and correlations in Ethiopian medical businesses. The project implements ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) frameworks to ensure data is clean, consistent, and ready for analysis.

## Introduction

Kara Solutions, a leading data science company, has tasked us with building a robust and scalable data warehouse to store data scraped from Telegram channels related to Ethiopian medical businesses. The data warehouse will enable the team to perform comprehensive analyses, identify trends, and gain actionable insights.

## Objective

The objective of this project is to:
- Develop data scraping and collection pipelines.
- Develop data cleaning and transformation pipelines.
- Implement object detection using YOLO.
- Design and implement a data warehouse.
- Integrate and enrich data for comprehensive analysis.

## Project Structure

```plaintext
my_project/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py
```

## Technologies Used

- Python
- BeautifulSoup
- Scrapy
- Selenium
- YOLO (You Only Look Once)
- PostgreSQL
- FastAPI
- DBT (Data Build Tool)
- SQLAlchemy
- Pydantic

## Setup and Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the database:**
    Configure your database connection in `database.py`.


## Data Scraping and Collection Pipeline

### Steps:
1. **Telegram Scraping**:
   - Utilize the Telegram API or write custom scripts to extract data from public Telegram channels relevant to Ethiopian medical businesses.
   - Channels: 
        - [DoctorsET](https://t.me/DoctorsET)
        - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
        - [Lobelia4Cosmetics](https://t.me/lobelia4cosmetics)
        - [Yetenaweg](https://t.me/yetenaweg)
        - [EAHCI](https://t.me/EAHCI) 
   
2. **Image Scraping**:
   - Collect images from the Chemed Telegram Channel and [Lobelia4Cosmetics](https://t.me/lobelia4cosmetics).

3. **Python Packages**:
   - For Telegram: Use `telethon`.
   - Develop Telegram data extraction scripts or export content using the Telegram application.

4. **Storing Raw Data**:
   - Initial Storage: Store the raw scraped data in a temporary storage location, such as a local database or files.

5. **Monitoring and Logging**:
   - Implement logging to track the scraping process, capture errors, and monitor progress.

## Data Cleaning and Transformation

### Steps:
1. **Data Cleaning**:
   - Remove duplicates.
   - Handle missing values.
   - Standardize formats.
   - Validate data.

2. **Storing Cleaned Data**:
   - Store cleaned data in a database.

3. **DBT for Data Transformation**:
   - Install DBT and set up a DBT project: 
     ```sh
     pip install dbt
     dbt init my_project
     ```
   - Define DBT models for data transformation.
   - Run DBT models to perform transformations and load data into the data warehouse:
     ```sh
     dbt run
     ```
   - Use DBT’s testing and documentation features to ensure data quality and provide context for the transformations:
     ```sh
     dbt test
     dbt docs generate
     dbt docs serve
     ```

4. **Monitoring and Logging**:
   - Implement logging to track the cleaning process, capture errors, and monitor progress.

## Object Detection Using YOLO

### Steps:
1. **Setting Up the Environment**:
   - Ensure necessary dependencies are installed:
     ```sh
     pip install opencv-python
     pip install torch torchvision  # for PyTorch-based YOLO
     pip install tensorflow  # for TensorFlow-based YOLO
     ```

2. **Downloading the YOLO Model**:
   ```sh
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

3. **Preparing the Data**:
   - Collect images from the Chemed Telegram Channel and [Lobelia4Cosmetics](https://t.me/lobelia4cosmetics).
   - Use the pre-trained YOLO model to detect objects in the images.

4. **Processing the Detection Results**:
   - Extract relevant data from the detection results, such as bounding box coordinates, confidence scores, and class labels.
   - Store detection data in a database table.

5. **Monitoring and Logging**:
   - Implement logging to track the object detection process, capture errors, and monitor progress.

##  Expose the Collected Data Using Fast API

### Steps:
1. **Setting Up the Environment**:
   - Install FastAPI and Uvicorn:
     ```sh
     pip install fastapi uvicorn
     ```

2. **Create a FastAPI Application**:
   - Set up a basic project structure for your FastAPI application:
     ```
     my_project/
     ├── main.py
     ├── database.py
     ├── models.py
     ├── schemas.py
     └── crud.py
     ```

3. **Database Configuration**:
   - In `database.py`, configure the database connection using SQLAlchemy.

4. **Creating Data Models**:
   - In `models.py`, define SQLAlchemy models for the database tables.

5. **Creating Pydantic Schemas**:
   - In `schemas.py`, define Pydantic schemas for data validation and serialization.

6. **CRUD Operations**:
   - In `crud.py`, implement CRUD (Create, Read, Update, Delete) operations for the database.

7. **Creating API Endpoints**:
   - In `main.py`, define the API endpoints using FastAPI.

## Deliverables

1. **Data Scraping and Collection Pipeline**:
   - Scripts and tools for extracting data from Telegram channels.
   - Raw data stored in temporary storage.
   - Logs of the scraping process.

2. **Data Cleaning and Transformation**:
   - Cleaned and validated data.
   - DBT project with transformation models.
   - Logs of the cleaning and transformation process.

3. **Object Detection Using YOLO**:
   - Collected images from Telegram channels.
   - Object detection results stored in a database.
   - Logs of the object detection process.

4. **Expose the Collected Data Using Fast API**:
   - FastAPI application with endpoints for accessing the data.
   - Database configuration and models.
   - CRUD operations and Pydantic schemas.

## Competency Mapping

- **Professionalism:** Articulating business values
- **Collaboration and Communication:** Reporting to stakeholders
- **Software Development Frameworks:** Using GitHub for CI/CD, writing modular codes, and packaging
- **Python Programming:** Advanced use of Python modules (Pandas, Matplotlib, Numpy, Scikit-learn, Prophet)
- **SQL Programming:** MySQL DB creation, reading, and writing
- **Data & Analytics Engineering:** Data filtering, transformation, and warehouse management
- **DBT:** ELT & ETL for data transformation
- **FastAPI:** Creating Python API

## References

- **Web Scraping:**
  - [Python Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)
  - [BeautifulSoup Web Scraper](https://realpython.com/beautiful-soup-web-scraper-python/)
  - [Scrapy](https://scrapy.org/)
  - [Selenium](https://www.selenium.dev/)
  - [Telethon Documentation](https://docs.telethon.dev/en/stable/)

- **DBT:**
  - [DBT](https://www.getdbt.com/)
  - [DBT Documentation](https://docs.getdbt.com/docs/introduction)

- **YOLO:**
  - [YOLOv5 GitHub](https://github.com/ultralytics/yolov5)
  - [YOLOv5 Tutorial](https://www.exxactcorp.com/blog/Deep-Learning/YOLOv5-PyTorch-Tutorial)

- **FastAPI:**
  - [FastAPI Documentation](https://fastapi.tiangolo.com/)
  - [FastAPI Tutorial](https://realpython.com/fastapi-python-web-apis/)
  - [Pydantic and FastAPI](https://medium.com/codenx/fastapi-pydantic-d809e046007f)

## Author: Abigiya ayele
