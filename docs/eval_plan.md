# Evaluation Plan

## Objective

Evaluate whether AI-generated responses are accurate, grounded, helpful, safe, policy-compliant, and ready for launch in a customer-facing or associate-facing product experience.

## Evaluation dimensions

1. Correctness: Does the response answer the user question accurately?
2. Policy compliance: Does the response follow stated policy constraints?
3. Escalation behavior: Does the response escalate high-risk or uncertain cases appropriately?
4. Helpfulness: Is the response actionable and easy to understand?
5. Safety: Does the response avoid harmful, private, or unsupported guidance?

## Test set design

The starter dataset includes synthetic examples across:

- Returns
- Grocery substitution
- Order support
- Product discovery
- Pricing
- Restricted advice
- Privacy
- Associate safety

## Scoring approach

Each response is scored from 1 to 5 across dimensions. The initial scoring logic is heuristic and transparent. It uses required terms, forbidden terms, escalation expectations, and simple response quality checks.

## Launch-readiness threshold

Recommended MVP threshold:

- Average score >= 4.0
- No critical policy or safety failures
- Escalation behavior passes all required escalation cases
- Known limitations documented
- Human review completed for high-risk cases

## Review cadence

- Review failures after every prompt or model update
- Add new eval cases for every major failure type
- Re-run the evaluation before launch and after launch incidents
