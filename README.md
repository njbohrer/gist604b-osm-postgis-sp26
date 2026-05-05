# PostGIS Database Orchestration and Spatial SQL Analysis

**Student:** Noah Bohrer  
**Course:** GIST 604B – Open Source GIS  
**Module:** Assignment 4 – PostGIS Database Orchestration  
**University of Arizona**

---

## Project Description
This project demonstrates how to build and analyze a spatial database using PostGIS within a PostgreSQL environment. The assignment focuses on loading real-world spatial datasets, executing spatial SQL queries, and performing multi-table spatial analysis. It highlights how spatial databases can be used to efficiently store, query, and analyze geospatial data at scale.

---

## Tools and Technologies
- PostgreSQL  
- PostGIS (spatial database extension)  
- Docker (containerized database environment)  
- SQL (spatial and relational queries)  
- shp2pgsql (data import tool)  
- VS Code + PostgreSQL Explorer  

---

## What I Did
- Configured a PostGIS-enabled PostgreSQL database using Docker  
- Established database connections and enabled PostGIS extensions  
- Imported multiple spatial datasets (neighborhoods, census blocks, streets, subway stations) into the database  
- Converted shapefiles into SQL using `shp2pgsql` and loaded them into relational tables  
- Wrote SQL queries to explore and analyze spatial datasets  
- Performed geometry operations and spatial relationship analysis (e.g., intersections, proximity)  
- Executed spatial joins across multiple tables to derive insights from combined datasets  

---

## How to View / Run
- Launch the project in GitHub Codespaces or a local environment with Docker installed  
- Start the PostGIS container: `docker compose up -d`  
- Connect to the database using PostgreSQL Explorer (VS Code)  
- Run SQL queries from the `/sql` directory files:
  - `01_basic_sql_queries.sql`  
  - `02_geometry_queries.sql`  
  - `03_spatial_relationships.sql`  
  - `04_spatial_joins.sql`  
- Query results will display in the SQL output panel  

---

## Repository Structure
- `/data/nyc` – Spatial datasets (shapefiles)  
- `/sql` – SQL scripts for spatial analysis queries  
- `/docker` or configuration files – Database container setup  
- `README.md` – Project documentation  

---
