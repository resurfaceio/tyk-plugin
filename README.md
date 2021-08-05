# tyk-plugin

Easily log API requests and responses to your own [system of record](https://resurface.io/).

## Requirements

* Tyk gateway
* docker (to run Resurface)

## Ports Used

* 4002 - Resurface API Explorer
* 4001 - Resurface microservice
* 4000 - Trino database UI

## Python setup

Open a shell inside your Tyk gateway instace, and install the [`logger-python`](https://github.com/resurfaceio/logger-python) dependency:

    pip install usagelogger

<!--Work in progress-->

## Go setup
// TODO

## Protecting User Privacy

Loggers always have an active set of <a href="https://resurface.io/rules.html">rules</a> that control what data is logged
and how sensitive data is masked. All of the examples above apply a predefined set of rules (`include debug`),
but logging rules are easily customized to meet the needs of any application.

<a href="https://resurface.io/rules.html">Logging rules documentation</a>

---
<small>&copy; 2016-2021 <a href="https://resurface.io">Resurface Labs Inc.</a></small>
