# aws-sam-<Project name>

<Project description>. 

## Deployment
Building, packaging and deploy the application in production environment.
```bash
sam build && sam package && sam deploy
```
Deploy in the test environment (if you have set up the environment in `samconfig.toml` file)
```bash
sam build --config-env test && sam package --config-env test && sam deploy --config-env test
```

## Invocation
Invoke the application with AWS Lambda locally:
```bash
sam local invoke <Function Name> --event events/event.json
```