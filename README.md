# aws-sam-<Project name>

<Project description>. 

## Deployment
Building and packaging the application:
```bash
sam build && sam package
```
Deploy the application:
```bash
sam deploy --config-file samconfig.toml
```

## Invocation
Invoke the application with AWS Lambda locally:
```bash
sam local invoke <Function Name> --event events/event.json
```