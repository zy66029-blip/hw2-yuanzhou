 # Report

## Business Use Case
This project focuses on drafting customer support responses for a small business. The intended user is a support staff member who receives customer questions, complaints, and refund requests. The system takes a customer message as input and generates a professional first-draft reply in English.

## Model Choice
I used the Gemini API because it was easy to access for lightweight prototyping and allowed me to build a simple command-line workflow. My goal was not to build a production system, but to test whether an LLM could assist with routine customer support drafting.

## Baseline vs. Final Design
My baseline prompt produced polite and safe responses, but it was too conservative. For a normal shipping-delay case, it escalated the message to a human support manager even though the case was low-risk.

In Revision 1, I clarified that routine shipping and missing-item questions should be answered directly rather than escalated. This improved the naturalness of the reply, but the response still made assumptions about the order status.

In Revision 2, I added a stronger instruction not to invent order status or other unknown details. This made the output more balanced. The final version remained polite and professional, while avoiding unnecessary escalation and reducing unsupported assumptions.

## Remaining Failure Cases / Human Review
This workflow should still involve human review for injury claims, legal threats, compensation requests, and refund cases with unclear eligibility. In those situations, the model may still be too cautious or may fail to reflect company-specific policy.

## Deployment Recommendation
I would recommend this workflow only as a draft-generation tool for internal support staff. It can save time in low-risk customer service scenarios, but it should not be used as a fully automated response system.