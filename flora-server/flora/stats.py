from config2.config import config
from prometheus_client import Counter, Gauge, MetricWrapperBase
from statsd import StatsClient

# https://github.com/prometheus/client_python
# https://github.com/jsocol/pystatsd

use_statsd = config.stats.statsd.use

statsd_client = None
if use_statsd:
  statsd = StatsClient(stats.statsd.config.host, stats.statsd.config.port, prefix=stats.statsd.config.prefix)


use_prometheus = configs.stats.prometheus.use
prometheus_metrics = {}

def prom_metric(metric_name: str, klass = Counter, label_names: list(str)) -> MetricWrapperBase:
  if not metric_name in prometheus_metrics:
    prometheus_metrics = klass(metric_name, metric_name, label_names)

def prom_tags_to_lists(tags: dict = {}) -> (list(str), list()):
  label_names = list(tags.keys())
  label_names.sort()
  label_values = []
  for name in label_names:
    label_values.append(tags[name])
  return (label_names, label_values)

def stats_gauge(metric_name: str, delta: int = 1, tags: dict = {}) -> None:
  if use_statsd:
    statsd.gauge(metric_name, delta)
  if use_prometheus:
    (label_names, label_values) = prom_tags_to_lists(tags)
    prom_metric(metric_name, Gauge, label_names).labels(label_values).gauge(delta)

