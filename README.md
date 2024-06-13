# Ethiopian Medical Business Data Warehouse

## Overview

This project involves building a data warehouse to store and analyze data on Ethiopian medical businesses scraped from Telegram channels. The project includes developing a data scraping and collection pipeline, cleaning and transforming the data, integrating object detection using YOLO, and designing and implementing the data warehouse.

## Table of Contents

- [Business Need](#business-need)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Data Scraping and Collection](#data-scraping-and-collection)
- [Data Cleaning and Transformation](#data-cleaning-and-transformation)
- [Object Detection using YOLO](#object-detection-using-yolo)
- [API Development with FastAPI](#api-development-with-fastapi)
- [Learning Outcomes](#learning-outcomes)
- [Competency Mapping](#competency-mapping)
- [References](#references)

## Business Need

Kara Solutions, a leading data science company, requires a robust and scalable data warehouse to store and analyze data on Ethiopian medical businesses. The centralized data storage allows comprehensive analysis to uncover valuable insights, enabling better decision-making and efficient querying and reporting.

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

## Data Scraping and Collection

1. **Telegram Scraping:**
    - Use the Telegram API or custom scripts to extract data from public Telegram channels.
    - Example channels:
        - [DoctorsET](https://t.me/DoctorsET)
        - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
        - [EAHCI](https://t.me/EAHCI)

2. **Image and Data Scraping:**
    - Collect images from channels like [Chemed Telegram Channel](https://t.me/lobelia4cosmetics) for object detection.
    - Use Python packages like `telethon` for extraction.

## Data Cleaning and Transformation

1. **Data Cleaning:**
    - Remove duplicates, handle missing values, standardize formats, and validate data.

2. **DBT for Data Transformation:**
    - Install and set up DBT.
    - Define and run DBT models for data transformation.
    - Test and document transformations with DBT.

## Object Detection using YOLO

1. **Setting Up YOLO:**
    - Install dependencies like OpenCV, TensorFlow, or PyTorch.
    - Clone the YOLO repository and install requirements.
    
    ```sh
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    ```

2. **Processing Detection Results:**
    - Extract data such as bounding box coordinates, confidence scores, and class labels.
    - Store detection data in a database table.

## API Development with FastAPI

1. **Setting Up FastAPI:**
    - Install FastAPI and Uvicorn.
    - Define project structure and configure the database using SQLAlchemy.

    ```sh
    pip install fastapi uvicorn
    ```

2. **Creating API Endpoints:**
    - Define SQLAlchemy models, Pydantic schemas, and CRUD operations.
    - Implement API endpoints in `main.py`.

## Learning Outcomes

- Telegram scraping using BeautifulSoup, Scrapy, and Selenium
- Object detection using YOLO
- Data cleaning and transformation using ETL processes
- Database schema design for data warehouses
- Implementing and configuring relational DBMS (e.g., PostgreSQL)
- Data integration and enrichment techniques
- End-to-end data pipeline development
- Testing and validation of data systems
- Deployment and maintenance of data warehouses

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

## Author: Abigiya Ayele

