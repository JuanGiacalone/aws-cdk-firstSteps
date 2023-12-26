#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_first_steps.cdk_first_steps_stack import CdkFirstStepsStack


app = cdk.App()
CdkFirstStepsStack(app, "CdkFirstStepsStack")

app.synth()
