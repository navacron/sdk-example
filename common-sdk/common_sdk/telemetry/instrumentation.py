import logging
from dataclasses import dataclass
from typing import Optional

import os
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk._logs import LoggerProvider, LogRecord
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk.resources import Resource
from opentelemetry._logs import (
    SeverityNumber,
)
import time




@dataclass
class TelemetryConfig:
    service_name: str
    newrelic_license_key: str
    log_level: int = logging.INFO
    otlp_endpoint: str = "https://otlp.nr-data.net:4318"
    enable_traces: bool = True
    enable_metrics: bool = True
     

@dataclass
class Telemetry:
    logger: logging.Logger
    tracer: Optional[trace.Tracer]
    meter: Optional[metrics.Meter]

def init_newrelic_observability(config: TelemetryConfig) -> Telemetry:
    # Create a resource with service information
    resource = Resource.create({
        "service.name": config.service_name,
        "service.version": "1.0.0",
        "environment": "production"
    })

    # Common headers for New Relic
    headers = {
        "api-key": config.newrelic_license_key
    }

    # Setup tracing
    trace_exporter = OTLPSpanExporter(
        endpoint=f"{config.otlp_endpoint}/v1/traces",
        headers=headers
    )
    tracer_provider = TracerProvider(resource=resource)
    tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))
    trace.set_tracer_provider(tracer_provider)

    # Setup metrics
    metric_exporter = OTLPMetricExporter(
        endpoint=f"{config.otlp_endpoint}/v1/metrics",
        headers=headers
    )
    metric_reader = PeriodicExportingMetricReader(metric_exporter)
    meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
    metrics.set_meter_provider(meter_provider)

    # Setup logging
    log_exporter = OTLPLogExporter(
        endpoint=f"{config.otlp_endpoint}/v1/logs",
        headers=headers
    )
    logger_provider = LoggerProvider(resource=resource)
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))
    set_logger_provider(logger_provider)

    # Create and configure logger
    logger = logging.getLogger("newrelic-logger")
    logger.setLevel(logging.INFO)

    class NewRelicHandler(logging.Handler):
        def emit(self, record):
            try:
                # Get current span context
                span_context = trace.get_current_span().get_span_context()
                
                # Map Python logging levels to OpenTelemetry severity numbers
                severity_mapping = {
                    logging.DEBUG: SeverityNumber.DEBUG,
                    logging.INFO: SeverityNumber.INFO,
                    logging.WARNING: SeverityNumber.WARN,
                    logging.ERROR: SeverityNumber.ERROR,
                    logging.CRITICAL: SeverityNumber.FATAL
                }

                # Create log record
                log_record = LogRecord(
                    timestamp=int(time.time() * 1e9),
                    trace_id=span_context.trace_id if span_context else 0,
                    span_id=span_context.span_id if span_context else 0,
                    trace_flags=span_context.trace_flags if span_context else 0,
                    severity_text=record.levelname,
                    severity_number=severity_mapping.get(record.levelno, SeverityNumber.INFO),
                    body=record.getMessage(),
                    attributes={
                        "logger.name": record.name,
                        "function": record.funcName,
                        "service.name": config.service_name
                    },
                    resource=resource
                )
                
                # Get logger and emit
                otel_logger = logger_provider.get_logger(
                    "newrelic-logger",
                    schema_url="",
                    version="1.0"
                )
                otel_logger.emit(log_record)

            except Exception as e:
                print(f"Error sending log to New Relic: {e}")
                import traceback
                traceback.print_exc()

    # Add handler to logger
    logger.addHandler(NewRelicHandler())

    return Telemetry(logger=logger, tracer=trace.get_tracer(__name__), meter=metrics.get_meter(__name__))


