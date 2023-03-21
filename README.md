# envar_manager

This utility allows you to store your team's .env files in the cloud and utilize environment variables from a single source of truth. This ensures that your team is always using the latest configuration settings, and you don't have to worry about updating each team member's .env file individually. By centralizing your environment variables, you can simplify your deployment process and improve the overall security of your application.

# prerequisite:
* user is authenticated with cloud provider
* user has configured a default cloud profile (.aws/credentials or gcloud init)
* user has access to the bucket where the .env file is stored

# Usage:
```Bash
cd path/to/project/
git clone https://github.com/omergi313/envar_manager.git
export ENVFILE_PATH="gs://path/to/.env"
or
export ENVFILE_PATH="s3://path/to/.env"
```
In python script:
```Python
import envar_manager
```
Now use os.environ / os.getenv as usual.


# TODO:
* add support for Docker
* add support for Kubernetes
