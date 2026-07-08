# SlipSmart AI – Requirements

## MVP Goal

Build a full-stack sports analytics platform that allows users to view upcoming matches, see prediction picks, and generate 10 diversified betting slip combinations with controlled overlap and risk scoring.

The MVP will not place bets, handle money, or provide guaranteed outcomes.

## Functional Requirements

### Matches

- Users can view upcoming football matches.
- Each match shows league, home team, away team, kickoff time, and status.

### Predictions

- Users can view suggested prediction picks for matches.
- Each prediction includes market type, pick, probability, odds, and risk level.
- Initial version can use sample data before real sports API integration.

### Slip Generator

- Users can enter a budget.
- Users can choose risk strategy: safe, balanced, or aggressive.
- Users can generate 10 diversified slips.
- Each slip shows stake, total odds, potential return, average probability, and risk score.
- The optimizer should reduce repeated picks across slips.
- The optimizer should avoid duplicate matches inside the same slip.

### AI Explanation

- Users can receive an explanation of generated slips.
- Initial version can use a mock explanation.
- Later version will use an LLM such as OpenAI or Gemini.

### Saved Slips

- Users should eventually be able to save generated slips.
- MVP can start without authentication and add saving later.

## Non-Functional Requirements

- The app should be mobile responsive.
- Backend response time should be under 2 seconds for slip generation.
- The backend should use a modular monolith structure.
- The database should use PostgreSQL.
- The backend should be containerized with Docker.
- Environment variables should be used for secrets and configuration.
- The system should be deployable to AWS later.

## Out of Scope for MVP

- Real-money betting
- User deposits
- Peer-to-peer betting
- Payment processing
- Gambling wallet
- Mobile app
- Advanced ML model
- Live odds
- Full user authentication
- Paid subscription

## MVP Success Criteria

- User can open the website.
- User can see upcoming matches.
- User can generate 10 diversified slips.
- User can see risk and probability information.
- User can read an AI-style explanation.
- Project can run locally with frontend and backend.
