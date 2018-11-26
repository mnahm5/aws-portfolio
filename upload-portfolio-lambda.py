import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes

codebuild_bucket_name = 'codebuild.mdnadimahmed.com'
portfolio_bucket_name = 'mdnadimahmed.com'

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket(portfolio_bucket_name)
build_bucket = s3.Bucket(codebuild_bucket_name)

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('aws-portfolio-project', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        print nm
        print mimetypes.guess_type(nm)[0]
        portfolio_bucket.upload_fileobj(obj, nm,
                                        ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
