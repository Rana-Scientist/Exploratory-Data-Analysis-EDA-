def extract_data_viaS3Bucket(urls,aws_id,aws_secret,s3_bucket):
    
    try:
       
        import boto3
        import sys
        import csv
        import pandas as pd_aws


         

        session = boto3.Session( 
                aws_access_key_id=aws_id, 
                aws_secret_access_key=aws_secret)
        #Then use the session to get the resource

        s3 = session.resource('s3')
        my_bucket = s3.Bucket(s3_bucket)
        #its print the path-list of all files
        for my_bucket_object in my_bucket.objects.all():
            print("Path_List \n",my_bucket_object.key)
        print('TEST started')
        

        # if sys.version_info[0] < 3: 
        #     from StringIO import StringIO # Python 2.x
        # else:
        #     from io import StringIO # Python 3.x
               
        # client = boto3.client('s3', aws_access_key_id=aws_id,
        #         aws_secret_access_key=aws_secret)  
        # csv_obj = client.get_object(Bucket=s3_bucket, Key=urls)
        # body = csv_obj['Body']
        # csv_string = body.read().decode('utf-8')
        
        # sniffer = csv.Sniffer()
        # dialect = sniffer.sniff(csv_string)
        # delimeter_=dialect.delimiter   
        
        # print('seperator is ',delimeter_)
        # data_frame = pd_aws.read_csv(StringIO(csv_string),sep=delimeter_,header=0,engine = 'python',encoding='latin-1')
            
        return my_bucket_object
        

    except NameError:
      
       print("Something BAD HAPPENED",NameError)      

def print_something(text):
    print("Hello",text)


    