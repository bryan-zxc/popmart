# Architecture

This document describes the high-level architecture of the system, organized as a standard 3-tier web application.

## Frontend

The Frontend layer serves as the user-facing interface, implemented as a client-side application that renders the UI and handles user interactions. It communicates with the API layer through HTTP requests, managing application state and presenting data in an accessible format. This separation ensures the presentation logic remains decoupled from business logic and data persistence concerns.

## API

The API layer acts as the intermediary between the Frontend and Database, exposing RESTful endpoints that encapsulate business logic and data validation. It processes incoming requests, applies authorization rules, orchestrates database operations, and returns structured responses. This layer enforces the application's domain rules while providing a stable contract for client consumption.

## Database

The Database layer provides persistent storage for application data, maintaining referential integrity and supporting transactional operations. It stores structured data in relational tables with defined schemas, enabling efficient querying and data retrieval. The database is accessed exclusively through the API layer, ensuring controlled access patterns and centralized data management.
