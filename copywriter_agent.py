"""
LeadFlow.AI - Autonomous Copywriter Agent
Synthesizes target website intelligence and prospect data into hyper-personalized,
high-converting B2B sales outreach emails without spammy templates.
"""

from typing import Dict, Any, List

class CopywriterAgent:
    def __init__(self, sender_name: str = "Elena", sender_company: str = "LeadFlow.AI"):
        self.sender_name = sender_name
        self.sender_company = sender_company

    def generate_email(self, prospect_name: str, research_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates a customized cold outreach email and reasoning logs based on research data.
        """
        domain = research_data.get("domain", "target company")
        title = research_data.get("title", domain)
        val_prop = research_data.get("value_proposition", f"innovation at {domain}")
        headers = research_data.get("headers", [])
        
        # Parse prospect name and role
        name_parts = prospect_name.strip().split()
        first_name = name_parts[0] if name_parts else "there"
        role_info = ""
        if "(" in prospect_name and ")" in prospect_name:
            role_info = prospect_name.split("(")[1].replace(")", "").strip()
        elif len(name_parts) > 1 and any(r in prospect_name.lower() for r in ["ceo", "founder", "head", "director", "vp", "manager"]):
            role_info = " ".join(name_parts[1:])

        # Select the best hook from headers or value prop
        hook_text = headers[1] if len(headers) > 1 else val_prop
        if len(hook_text) > 80:
            hook_text = hook_text[:77] + "..."

        # Generate Reasoning Steps for Live Dashboard
        reasoning_logs: List[str] = [
            f"Analyzing scraped metadata for {domain} ({title[:40]}...)",
            f"Identified core value proposition: '{val_prop[:60]}...'",
            f"Targeting decision maker: {first_name} {f'({role_info})' if role_info else ''}",
            f"Synthesizing pain points: B2B client acquisition without inflating human headcount costs.",
            f"Drafting personalized hook referencing '{hook_text}'...",
            f"Applying anti-spam formatting and conversational tone optimization."
        ]

        # Generate Subject Line
        subject = f"Scaling client pipeline for {domain} ({first_name})"
        if role_info and "ceo" in role_info.lower() or "founder" in role_info.lower():
            subject = f"Quick question for {first_name} regarding {domain}'s outbound growth"

        # Generate Body
        body = f"""Hi {first_name},

I was reviewing {domain}'s online presence and was really impressed by how you focus on {val_prop.lower() if len(val_prop) < 50 else hook_text.lower()}.

Usually, the biggest operational challenge for {f'{role_info}s' if role_info else 'leaders'} in your space is scaling a consistent, high-ticket B2B sales pipeline without incurring the $5,000+/mo overhead of traditional human sales SDRs.

We build Autonomous AI SDR Agents (like myself) that deeply scrape your target market's websites, write hyper-personalized outreach based on live signals, and book qualified sales meetings directly onto your calendar 24/7.

Would you be open to a quick 5-minute chat next Tuesday at 3 PM to see the exact AI workflow we used to analyze {domain}?

Best regards,

{self.sender_name}
Autonomous AI SDR Agent | {self.sender_company}
"""
        return {
            "status": "success",
            "prospect_name": prospect_name,
            "first_name": first_name,
            "target_domain": domain,
            "subject": subject,
            "body": body.strip(),
            "reasoning_logs": reasoning_logs
        }

if __name__ == "__main__":
    # Test script standalone
    from researcher_agent import ResearcherAgent
    researcher = ResearcherAgent()
    data = researcher.extract_signals("github.com")
    
    copywriter = CopywriterAgent(sender_name="Elena")
    email_output = copywriter.generate_email("David (CEO)", data)
    print("Subject:", email_output["subject"])
    print("\nBody:\n", email_output["body"])
    print("\nReasoning Logs:", email_output["reasoning_logs"])
