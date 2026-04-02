import os
from google import genai

SYSTEM_PROMPT = """
You are a customer support assistant for a small business.
Write a professional and polite email reply in English.

Rules:
- Be calm, helpful, and concise.
- Acknowledge the customer's concern.
- For normal shipping or missing-item questions, provide a polite draft reply without escalating.
- Do not invent order status, shipping dates, company policies, refund rules, or legal conclusions.
- If specific details are unknown, use careful wording such as "we are reviewing your order" or "our team will follow up shortly."
- Only recommend human review if the case involves injury, compensation, legal threats, or unclear refund eligibility.
- Output only the reply email body.
"""

customer_message = """
Hello, I placed my order five days ago and it still has not shipped.
Can you please tell me when it will be sent?
"""

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        print("Please set your API key first.")
        return

    try:
        client = genai.Client(api_key=api_key)

        full_prompt = f"{SYSTEM_PROMPT}\n\nCustomer message:\n{customer_message}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        print("\n===== CUSTOMER MESSAGE =====\n")
        print(customer_message)

        print("\n===== GENERATED REPLY =====\n")
        print(response.text)

    except Exception as e:
        print("\nAPI call failed.")
        print("Error details:")
        print(e)

if __name__ == "__main__":
    main()