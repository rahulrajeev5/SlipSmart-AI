# SlipSmart AI – API Design

## Purpose

This document defines the initial REST API contract for the SlipSmart AI backend.

## Base URL

Development:

http://localhost:8000

## Core Endpoints

### Health

GET /health

Returns backend health status.

### Matches

GET /matches/upcoming

Returns upcoming matches.

### Predictions

GET /predictions

Returns available prediction picks.

GET /predictions/{match_id}

Returns predictions for a specific match.

### Slip Generator

POST /slips/generate

Generates diversified slips.

Request:

{
  "budget": 10,
  "number_of_slips": 10,
  "picks_per_slip": 4,
  "strategy": "balanced",
  "max_overlap": 0.4
}

Response:

{
  "generation_id": "uuid",
  "slips": []
}

### AI Explanation

POST /ai/explain

Returns explanation for generated slips.

### Future Endpoints

POST /auth/register
POST /auth/login
GET /users/me
POST /slips/save
GET /slips/history
POST /ai/chat