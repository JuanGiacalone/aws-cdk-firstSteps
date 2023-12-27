
# Welcome to your CDK Python project!

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`cdk_first_steps_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

 ---
 PERSONAL NOTES

```
 .\source.bat
```
Runs the virtual enviroment for you.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/cdk-*"
            ]
        }
    ]
}
```

```
cdk bootstrap --show-template > bootstrap-template.yaml
https://d-9067f17090.awsapps.com/start
_GW24pS5&$1t?gtgnA
aws s3 ls --profile CloudFormationALL-678953334306
cdk bootstrap --profile CloudFormationALL-678953334306
```

```
cdk bootstrap - its used when first declaring a Stack

cdk diff - shows differences with local setup and actual remote

cdk deploy - deploys the changes to the remote stack

$ # Deploys only to environments foo and bar
$ cdk bootstrap --app='' foo bar
```

IAMFullAccess	AWS managed	Provides full access to IAM via the AWS Management Console.
AWSCloudFormationFullAccess	AWS managed	Provides full access to AWS CloudFormation.
AmazonSSMFullAccess	AWS managed	Provides full access to Amazon SSM.
AmazonS3FullAccess	AWS managed	Provides full access to all buckets via the AWS Management Console.
AmazonEC2ContainerRegistryFullAccess	AWS managed	Provides administrative access to Amazon ECR resources

Enjoy!
