# ServerWatch System Architecture

## Overview

ServerWatch is an infrastructure monitoring and incident management platform.

The platform consists of five major components:

1. Monitoring Agent
2. Backend API
3. PostgreSQL Database
4. Web Dashboard
5. External Integrations

## High-Level Flow

Linux Server
    ↓
Monitoring Agent
    ↓
ServerWatch API
    ↓
PostgreSQL
    ↓
Incident Engine
    ↓
Jira / Slack

The Web Dashboard communicates with the Backend API to display server health,
metrics, and incidents.

## Components

### Monitoring Agent

Runs on monitored Linux servers and collects infrastructure and application
health metrics.

### Backend API

Receives metrics, processes monitoring information, manages incidents, and
provides APIs for the web dashboard.

### PostgreSQL

Stores servers, metrics, incidents, incident events, alert rules, and
notification records.

### Frontend

Provides a web-based interface for monitoring infrastructure and managing
incidents.

### External Integrations

Jira is used for incident tracking.

Slack is used for operational notifications.