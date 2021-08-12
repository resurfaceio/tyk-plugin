# tyk-plugin

Easily log API requests and responses to your own [system of record](https://resurface.io/).

## Requirements

* Tyk gateway
* docker (for [Resurface](https://resurface.io/installation))

## Ports Used

* 4002 - Resurface API Explorer
* 4001 - Resurface microservice
* 4000 - Trino database UI

## Option 1: Python plugin

- Open a shell in the same context as your Tyk gateway instance, and install the [`logger-python`](https://github.com/resurfaceio/logger-python) dependency:

      pip3 install --upgrade usagelogger

- Make sure that Python plugins are enabled in the global settings for your Tyk gateway. To do this, you need to add the following block to `tyk.conf` (or `tyk.standalone.conf` if you're using the docker container version):

  ```
  ...
  "coprocess_options": {
    "enable_coprocess": true,
    "python_path_prefix": "/opt/tyk-gateway"
  },
  "enable_bundle_downloader": true,
  "bundle_base_url": "https://github.com/resurfaceio/tyk-plugin/releases/download/v0.1/",
  ...
  ```
  
  The `bundle_base_url` corresponds to the base URL that Tyk will use to download the plugin.
  
- In addition, append the following lines to `tyk.conf`:
 
   ```
   ...
   "USAGE_LOGGERS_URL": "http://localhost:4001/message",
   "USAGE_LOGGERS_RULES": "include debug"
   }
   ```
   These fields are necessary for the plugin to communicate with Resurface:
     - `USAGE_LOGGERS_URL` corresponds to the Resurface database connection URL. If you're running Tyk Gateway as a docker container, you should use your `docker0` IP address instead of `localhost`.
     - `USAGE_LOGGERS_RULES` corresponds to a [set of rules for logging](https://github.com/resurfaceio/tyk-plugin#protecting-user-privacy).
 

- Modify your API spec using the raw JSON editor in the Tyk Dashboard or directly in the JSON file (in the case of the Community Edition) and append the `"custom_middleware_bundle": "bundle.zip"` line to it. Here's an example:

  <pre>
  {
    "name": "Tyk Test API",
    "api_id": "1",
    "org_id": "default",
    ...
    "proxy": {
      "listen_path": "/quickstart/",
      "target_url": "http://httpbin.org",
      "strip_listen_path": true
    },
    <b>"custom_middleware_bundle": "bundle.zip"</b>
  }
  </pre>
  
 - Restart your Tyk gateway (you might need to do it using [the Tyk Python Gateway build](https://tyk.io/docs/plugins/supported-languages/rich-plugins/python/tutorial-add-demo-plugin-api/#running-the-tyk-python-gateway-build)).


## Option 2: Go plugin

Coming soon!

## Protecting User Privacy

Loggers always have an active set of <a href="https://resurface.io/rules.html">rules</a> that control what data is logged
and how sensitive data is masked. All of the examples above apply a predefined set of rules (`include debug`),
but logging rules are easily customized to meet the needs of any application.

<a href="https://resurface.io/rules.html">Logging rules documentation</a>

---
<small>&copy; 2016-2021 <a href="https://resurface.io">Resurface Labs Inc.</a></small>
