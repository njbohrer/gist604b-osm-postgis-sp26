"""
OSM PostGIS Setup Workflow - Student Implementation

Complete the function in this file.
Use the notebook to build and run the workflow.

📋 FUNCTION TO IMPLEMENT IN THIS FILE:
=====================================
✅ Function: setup_osm_postgis() → notebooks/setup_osm_postgis.ipynb
"""

import os
import psycopg2
import requests
import subprocess
import zipfile
from pathlib import Path
from typing import Optional

# Function: Setup PostGIS + Load OSM Shapefile Data

def setup_osm_postgis(
    osm_url: str,
    db_name: str = "osm_db",
    user: str = "postgres",
    password: str = "postgres",
    host: str = "localhost",
    port: int = 5432,
    data_dir: Optional[Path] = None,
    load_shapefiles: Optional[list[str]] = None
) -> None:
    """
    Create a PostGIS database and load Geofabrik shapefile data.

    This function performs a complete workflow:
    - Connect to PostgreSQL
    - Create a new database
    - Enable PostGIS extension
    - Download shapefile data from Geofabrik
    - Unzip shapefile data
    - Load shapefiles into PostGIS using shp2pgsql

    Args:
        osm_url: URL to Geofabrik shapefile ZIP
        db_name: Name of the database to create
        user: PostgreSQL username
        password: PostgreSQL password
        host: Database host
        port: Database port
        data_dir: Optional directory to store downloaded OSM data
        load_shapefiles: Optional list of shapefile layer names to load

    Returns:
        None

    Example:
        >>> setup_osm_postgis(
        ...     osm_url="https://download.geofabrik.de/north-america/us/arizona-latest-free.shp.zip", db_name="arizona", load_shapefiles=["places_a", "pois"]
        ... )
    """

    # TODO: Implement this function
import os
import requests
import subprocess
import psycopg2
import zipfile

print("Libraries imported!")
# Establish a connection to the postgres database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
)

# Every SQL statement is executed immediately
conn.autocommit = True

# Open a cursor to perform database operations
cur = conn.cursor()

# Check current database by using PostgreSQL built-in function
cur.execute("SELECT current_database();")

# Use fetchone() to return one row from the result of the query
print("Current database:", cur.fetchone()[0])

print("Connected to PostgreSQL server")
db_name = "alaska"

# Check if database name already exists
cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")

# fetchone() returns a row if it exists, otherwise None
exists = cur.fetchone()

if not exists:
    cur.execute(f"CREATE DATABASE {db_name};")
    print(f"Database '{db_name}' created")
else:
    print(f"Database '{db_name}' already exists")

# Close connection to 'postgres' before switching databases
cur.close()
conn.close()

print("Closed connection to 'postgres'")
 # Establish a connection to the working database
conn = psycopg2.connect(
    dbname=db_name,
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
)

# Every SQL statement is executed immediately
conn.autocommit = True

# Open a cursor to perform database operations
cur = conn.cursor()

print(f"Connected to database: {db_name}")

# Create extension if it does not exist
cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")

# Check PostGIS version
cur.execute("SELECT PostGIS_version();")
version = cur.fetchone()
print("PostGIS version:", version) 
osm_url = "https://download.geofabrik.de/north-america/us/alaska-latest-free.shp.zip"

# Define local directory to store OSM data
data_path = f"../data/{db_name}"

# Create directory if it does not exist
os.makedirs(data_path, exist_ok=True)

# Construct full file path using the filename from the URL
zip_path = os.path.join(data_path, osm_url.split("/")[-1])

# Download file only if it does not already exist
if not os.path.exists(zip_path):
    print("Downloading OSM data...")
    print("URL:", osm_url)

    # Send HTTP request (stream=True downloads in chunks)
    response = requests.get(osm_url, stream=True, timeout=300)
    # Raise error if download fails
    response.raise_for_status()
    
    # Get total file size (if available) for progress tracking
    file_size = int(response.headers.get("content-length", 0))
    if file_size > 0:
        print(f"File size: {file_size / (1024 * 1024):.1f} MB")

    downloaded = 0
    
    # Open file in binary write mode
    with open(zip_path, "wb") as f:
        # Download file in chunks to avoid loading entire file into memory
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                
                # Display progress as percentage (if file size is known)
                if file_size > 0:
                    progress = downloaded / file_size * 100
                    print(f"\rProgress: {progress:.1f}%", end="", flush=True)

    print("\nDownload complete")
    print("Saved to:", zip_path)
else:
    # Skip download if file already exists locally
    print("File already exists:")
    print(zip_path)
extract_path = os.path.join(data_path, "shapefiles")

if not os.path.exists(extract_path):
    print("Extracting shapefiles...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    print("Extraction complete")
    print("Extracted to:", extract_path)
else:
    print("Extracted folder already exists:")
    print(extract_path)
# List of shapefiles to load
load_shapefiles = [
    "places", 
    "railway",
    "transport",
    "pois",
    "traffic",
    "landuse",
    "protected_area",
    "water",
    "roads"]

# Set password so shp2pgsql/psql does not prompt
env = os.environ.copy()
env["PGPASSWORD"] = "postgres"

# Find all .shp files
shp_files = [f for f in os.listdir(extract_path) if f.endswith(".shp")]

# Loop through shapefiles and load them
for shp_file in shp_files:
    filename = os.path.splitext(shp_file)[0]

    table_name = (
        filename
        .replace("gis_osm_", "")
        .replace("_free_1", "")
    )

    # Skip shapefiles that are not in our load list
    if table_name not in load_shapefiles: continue

    shp_path = os.path.join(extract_path, shp_file)

    print(f"\nLoading {table_name} from {filename}...")

    cmd = f'shp2pgsql -d -I -s 4326 "{shp_path}" public.{table_name} | psql -h localhost -U postgres -d {db_name}'

    print("Command:", cmd)

    try:
        subprocess.run(cmd, shell=True, env=env, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        print(f"{table_name} loaded successfully")
    except subprocess.CalledProcessError as e:
        print(f"{table_name} failed")
        print(e.stderr.splitlines()[-1])  # show only last error line
list_query = """
SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
"""

# Execute the query
cur.execute(list_query)

# Retrieve all table names
tables = [t[0] for t in cur.fetchall()]
print("Tables created:", tables)

# Row counts for all tables (not hardcoded)
for table in tables:
    try:
        cur.execute(f'SELECT COUNT(*) FROM "{table}";')
        count = cur.fetchone()[0]
        print(f"{table}: {count} rows")
    except Exception as e:
        print(f"{table}: error")
        print(e)

# Close the database connection
cur.close()
conn.close()

print("Database connection closed")
    # Step 9: Close connections



