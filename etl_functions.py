import boto3

CONNECTION_STRING = 'postgresql://ray_sidener:sayridener@ls-2619b6b15c9bdc80a23f6afb7eee54cf0247da21.ca3yee6xneaj.us-east-1.rds.amazonaws.com/postgres'

def download_raw_files():
  #Download raw csv files from S3 buckets and save to raw_data directory.
  #Assumes you have AWS access configured already
  files = ['bengals.csv', 'boyd_receiving.csv', 'chase_receiving.csv', 'higgins_receiving.csv']
  s3 = boto3.resource('s3')
  bucket_name = 'mindex-data-analytics-code-challenge'
  print("starting file downloads")
  for file in files:
    s3.Bucket(bucket_name).download_file(file, 'raw_data/' + file)
  print("downloaded all files from s3")

def map_wins_losses(x):
  #A value of 0 represents a loss, and a value of 1 represents a win.
  #Open question - how should this handle null or other values in the input data?
  if (x == 0):
    return "Loss"
  elif (x == 1):
    return "Win"
