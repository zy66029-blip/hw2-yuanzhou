# Evaluation Set

## Case 1 - Normal case
**Input:**  
Hello, I placed my order five days ago and it still has not shipped. Can you please tell me when it will be sent?

**What a good output should do:**  
Politely acknowledge the delay, apologize, and provide a professional response without sounding defensive.

---

## Case 2 - Normal case
**Input:**  
Hi, I received the package today, but one item is missing. Can you help me?

**What a good output should do:**  
Acknowledge the issue, apologize, and clearly explain the next step in a helpful tone.

---

## Case 3 - Edge case
**Input:**  
This is ridiculous. I emailed twice already and nobody helped me. If this is not fixed today, I am never buying from your company again.

**What a good output should do:**  
Stay calm and professional, avoid sounding robotic, acknowledge frustration, and de-escalate the situation.

---

## Case 4 - Edge case
**Input:**  
Can you refund my order and also waive the return shipping fee? I bought this two months ago and I do not have the receipt anymore.

**What a good output should do:**  
Avoid inventing company policy. Respond carefully and indicate that refund eligibility may need review.

---

## Case 5 - Human review / likely failure case
**Input:**  
Your product caused a serious injury to my hand. I want compensation and I may contact a lawyer.

**What a good output should do:**  
Remain professional, avoid admitting liability, avoid making legal promises, and clearly indicate that this case requires human review.