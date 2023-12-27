#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_first_steps.cdk_first_steps_stack import CdkFirstStepsStack
from cdk_first_steps.first_api_gateway_stack import FirstApiGatewayStack


app = cdk.App()
""" CdkFirstStepsStack(app, "CdkFirstStepsStack") """

FirstApiGatewayStack(app, "FirstApiGatewayStack")

app.synth()
