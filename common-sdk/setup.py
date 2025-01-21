from setuptools import setup, find_packages

setup(
    name="common-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'opentelemetry-api>=1.20.0',
        'opentelemetry-sdk>=1.20.0',
        'opentelemetry-instrumentation-requests>=0.40b0',
        'opentelemetry-exporter-otlp>=1.20.0',
        'opentelemetry-exporter-otlp-proto-http>=1.20.0'
    ],
) 