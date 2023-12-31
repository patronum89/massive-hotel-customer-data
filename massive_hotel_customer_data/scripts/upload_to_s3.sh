#!/bin/bash

# Set your AWS credentials (replace with your actual values)
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=your_region

# Set your S3 bucket name
S3_BUCKET=your-unique-bucket-name

# Path to the directory containing JSON files
JSON_DIR=/path/to/json/files

# Upload each JSON file to S3
for file in $JSON_DIR/*.json; do
    [ -e "$file" ] || continue  # Skip if no files found
    echo "Uploading $file to S3..."
    aws s3 cp "$file" "s3://$S3_BUCKET/"
done
