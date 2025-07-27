# marimo-dashboard
An example project for hosting Marimo notebooks as apps behind an ASGI webserver.

# Motivation
Productivity/scalability for my team at work (financial sector).

# Background
I introduced & distributed marimo notebooks to my team at the end of 2024 (replacing Jupyter).
Given the powerful reactive state & UI controls - this triggered a wave of new apps / dashboards.
We now have an explosion problem to control & consequently, I put together this framework to consolidate our apps.

This template is based off:

- https://github.com/marimo-team/marimo/tree/main/examples/frameworks/fastapi

# Packaging
Unfortunately, legacy lock-in at work forces `conda` for package management.
I would recommend using a modern alternative e.g. `uv` or `Poetry`. 
