## Process for CI/CD

Secrets are set in github project. It's use like env variable during CI/CD pipelines.

Zappa needs config file zappa_settings.json to deploy the API.
Temporarily this config file is directly create in githubci.yml but in nexts steps it will be write in Github Secrets
