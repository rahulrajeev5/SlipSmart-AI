# SlipSmart AI – Product Decisions

## Decision 001 – Use Next.js for Frontend

Date: 2026-01-24

### Decision

Use Next.js instead of plain React.

### Reason

- Better SEO for public prediction pages
- Built-in routing
- Production-ready React framework
- Good fit for future landing pages and daily prediction pages

### Status

Accepted

---

## Decision 002 – Use FastAPI for Backend

Date: 2026-01-24

### Decision

Use FastAPI as the backend framework.

### Reason

- Python-friendly
- Works well with ML models
- Automatic OpenAPI documentation
- Lightweight and fast for APIs

### Status

Accepted

---

## Decision 003 – Use PostgreSQL

Date: 2026-01-24

### Decision

Use PostgreSQL instead of MongoDB.

### Reason

- Data is highly relational
- Users, matches, predictions, slips, and slip items need joins
- Strong transaction support
- Better fit for reporting and analytics

### Status

Accepted

---

## Decision 004 – Start with Modular Monolith

Date: 2026-01-24

### Decision

Build the backend as a modular monolith.

### Reason

- Faster for solo development
- Easier to debug
- Lower deployment complexity
- Clear module boundaries allow future microservice extraction

### Status

Accepted