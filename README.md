# Generate CSV and Convert to Partitioned Snappy Parquet

Quick script that generates a fake dataset in CSV format and then converts it to a set of partitioned snappy parquet files.

## Usage

### 1. Install requirements

> pip install -r requirements.txt`

### 2. Update the script to meet desired results

The script can be split to generate different fake data as a CSV or take an existing CSV and convert it to partitioned snappy parquet.

### 3. Run the python script

> python generate_and_convert.py <Number of records>