# Example Service – README

This microservice is responsible for user authentication and token management.

## Deployment

Deployment is handled via GitHub Actions with environment-specific Helm charts.

To deploy to staging:

``` bash
helm upgrade --install auth-service ./helm --values ./helm/values-staging.yaml
```

To rollback:

``` bash
helm rollback auth-service <revision>
```

## Logging

Logs are written to stdout and picked up by Fluent Bit and sent to Elasticsearch.

## Alerts

Any 5xx errors trigger PagerDuty alerts via Prometheus rules.
