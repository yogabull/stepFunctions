# AWS Step Functions

### Description

Contains workup files for an AWS Step Funciton.
- The function invokes a lambda function that checks the temperature.
- A decision state determines if the temp is above/below freezing.
- If the temperature is below freezing, the step function publishes it to an SNS topic.
- Both results are written to a DyanmoDB table.
