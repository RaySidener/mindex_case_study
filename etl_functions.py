import pandas as pd
import boto3

def download_raw_files():
  files = ['bengals.csv', 'boyd_receiving.csv', 'chase_receiving.csv', 'higgins_receiving.csv']
  s3 = boto3.resource('s3')
  bucket_name = 'mindex-data-analytics-code-challenge'
  print("starting file downloads")
  for file in files:
    s3.Bucket(bucket_name).download_file(file, 'raw_data/' + file)
  print("downloaded all files from s3")

def map_wins_losses(x):
  if (x == 0):
    return "Loss"
  elif (x == 1):
    return "Win"
