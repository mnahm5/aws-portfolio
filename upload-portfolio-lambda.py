import json
import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    # TODO implement
    location = {
        "bucketName": 'codebuild.mdnadimahmed.com',
        "objectKey": 'aws-portfolio-project'
    }
    portfolio_bucket_name = 'mdnadimahmed.com'
    sns_topic_name = 'arn:aws:sns:ap-southeast-2:947526780140:aws-portfolio-project-update'

    sns = boto3.resource('sns')
    topic = sns.Topic(sns_topic_name)

    try:
        job = event.get("CodePipeline.job")

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                location = artifact["location"]["s3Location"]

        print "Building from" + str(location)

        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

        portfolio_bucket = s3.Bucket(portfolio_bucket_name)
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                                                ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print "Job Done"

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
        print "CodePipeline ID Sent"

        topic.publish(Subject="Portfolio Updated", Message="Success")
    except:
        topic.publish(Subject="Portfolio Update Failed", Message="Failed")
        raise

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }