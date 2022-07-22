 
## getting start 

### change config 
change all <your account id> to your real account id 

### login AWS sso 
```shell
aws sso login && yawsso --default
```

### deploy lambda

```shell
sls deploy 
```

### deploy step function 

```
aws stepfunctions  create-state-machine --definition "$(cat demo.asl.json)" --name "gamma-mapreduce-test" --role-arn "arn:aws:iam::<your account id>:role/gamma-stepfunction-mapreduce-test"
```

IAM role should contain policy name `AWSLambdaVPCAccessExecutionRole`

IAM Trusted entities should contain Service `states.amazonaws.com`

### run step function 

#### in console 
param :
```json
{
  "ship-date": "2016-03-14T01:59:00Z",
  "detail": {
    "delivery-partner": "UQS"
  }
}

```



##  additional


https://gist.github.com/yokada/ffc92d84a5844008fbab14ab6aeda054

https://aws.amazon.com/premiumsupport/knowledge-center/step-functions-iam-role-troubleshooting/