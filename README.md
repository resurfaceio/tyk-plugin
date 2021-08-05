# tyk-plugin

Easily log API requests and responses to your own [system of record](https://resurface.io/).

## Requirements

* Tyk gateway
* docker (for [Resurface](https://resurface.io/installation))

## Ports Used

* 4002 - Resurface API Explorer
* 4001 - Resurface microservice
* 4000 - Trino database UI

## Python plugin

Open a shell inside your Tyk gateway instace, and install the [`logger-python`](https://github.com/resurfaceio/logger-python) dependency:

    pip3 install --upgrade usagelogger

Follow [Tyk's official guide](https://tyk.io/docs/plugins/supported-languages/rich-plugins/python/tutorial-add-demo-plugin-api/) to add a python plugin to you Tyk Gateway. Set `bundle_base_url` to `https://github.com/resurfaceio/tyk-plugin/releases/download/v0.1/bundle.zip` in your `tyk.conf` file.

//TODO

## Go plugin
// TODO

## Protecting User Privacy

Loggers always have an active set of <a href="https://resurface.io/rules.html">rules</a> that control what data is logged
and how sensitive data is masked. All of the examples above apply a predefined set of rules (`include debug`),
but logging rules are easily customized to meet the needs of any application.

<a href="https://resurface.io/rules.html">Logging rules documentation</a>

---
<small>&copy; 2016-2021 <a href="https://resurface.io">Resurface Labs Inc.</a></small>
