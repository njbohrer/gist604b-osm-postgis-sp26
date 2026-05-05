# OpenStreetMap (OSM) and PostGIS Spatial Analysis – Alaska Case Study

**Student:** Noah Bohrer  
**Course:** GIST 604B – Open Source GIS  
**Module:** Assignment 5 – OSM & PostGIS Spatial Analysis  
**University of Arizona**

---

## Project Description
This project demonstrates a complete geospatial data pipeline using OpenStreetMap (OSM), PostGIS, and Python. The workflow includes automating database setup, loading OSM datasets, executing spatial SQL queries, and analyzing results through Jupyter Notebooks. The analysis was extended to a custom area of interest (Alaska), showcasing the ability to adapt spatial workflows to new geographic regions.

---

## Tools and Technologies
- Python  
- PostgreSQL  
- PostGIS (spatial database extension)  
- OpenStreetMap (OSM) data  
- GeoFabrik (OSM data source)  
- Docker (containerized database environment)  
- SQL (spatial queries and analysis)  
- Jupyter Notebooks  
- shp2pgsql (data import tool)  

---

## What I Did
- Built a reusable Python workflow to create and configure a PostGIS database :contentReference[oaicite:0]{index=0}  
- Automated downloading and loading of OSM spatial datasets into PostgreSQL  
- Connected Python to PostGIS for executing and managing spatial queries  
- Explored and executed complex spatial SQL queries using OSM data  
- Used Common Table Expressions (CTEs) to organize multi-step spatial queries  
- Ran SQL queries through Jupyter Notebooks for analysis and visualization  
- Adapted the full workflow to a new Area of Interest (Alaska)  
- Designed and executed custom spatial queries:
  - Feature extraction (filtering OSM layers)  
  - Aggregation and summarization by region or category  
  - Spatial relationship analysis (e.g., proximity, density, or clipped features) :contentReference[oaicite:1]{index=1}  
- Visualized and interpreted spatial results directly within notebooks  

---

## How to View / Run
- Launch the project in GitHub Codespaces or a local environment with Docker installed  
- Start the PostGIS container: `docker compose up -d`  
- Run the setup workflow notebook:
  - `/notebooks/setup_osm_postgis.ipynb`  
- Explore and execute queries:
  - `/notebooks/osm_postgis_queries.ipynb` (Arizona baseline)  
  - `/notebooks/osm_postgis_alaska.ipynb` (custom analysis)  
- SQL queries are stored in the `/sql` directory  
- Results and visualizations are generated directly within Jupyter Notebooks  

---

## Repository Structure
- `/notebooks` – Jupyter Notebooks for setup and analysis workflows  
- `/src` – Python scripts for database setup and automation  
- `/sql` – SQL query files for spatial analysis  
- `/data` – Downloaded OSM datasets  
- `README.md` – Project documentation  

---
