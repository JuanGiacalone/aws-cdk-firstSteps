from constructs import Construct
from aws_cdk import (
    aws_apigatewayv2 as apigateway,
    aws_apigatewayv2_integrations as apigatewayInt,
    aws_s3 as s3,
    Stack,
    RemovalPolicy
)

class FirstApiGatewayStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self, 'FirstBucket', removal_policy=RemovalPolicy.DESTROY)  # Be cautious with removal_policy

        # Create an API Gateway
        api = apigateway.HttpApi(self, 'MyApi')

          # Create an integration between the API Gateway V2 and S3
        s3_integration = apigatewayInt.HttpUrlIntegration(
            id='firstBucket',
            url=f'http://{bucket.bucket_name}.s3-website-{Stack.of(self).region}.amazonaws.com/{{proxy+}}'
        )
        api = api.add_routes(  
            integration = s3_integration, 
            path='/myresource/{proxy}',
            methods = [apigateway.HttpMethod.ANY],

        )

        # Create a route for the API Gateway V2
"""         api.add_routes(
            path='/myresource/{proxy+}',
            methods=[apigatewayInt.HttpServiceDiscoveryIntegrationProps],
            integration=s3_integration
        ) """














