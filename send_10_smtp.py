#!/usr/bin/env python3
"""Send 10 Horizon Europe emails using Python SMTP"""

import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "zerox@exventure.co"
PASSWORD = "rbhr tvzh bcss osyl"

RESEARCHERS = [
    {
        "name": "Prof. Henrik Thunman",
        "email": "henrik.thunman@chalmers.se",
        "expertise": "DFB gasification, GoBiGas plant",
        "reference": "Your leadership of the GoBiGas project and expertise in dual fluidized bed gasification"
    },
    {
        "name": "Prof. Ange Nzihou",
        "email": "ange.nzihou@mines-albi.fr",
        "expertise": "Thermochemical processes, tar reforming",
        "reference": "Your distinguished work on tar reforming and thermochemical conversion processes"
    },
    {
        "name": "Prof. Pier Ugo Foscolo",
        "email": "pierugo.foscolo@univaq.it",
        "expertise": "DFB gasification, 5 MW pilot plant",
        "reference": "Your pioneering work on dual fluidized bed gasification and the 5 MW L'Aquila pilot plant"
    },
    {
        "name": "Prof. Joakim Lundgren",
        "email": "joakim.lundgren@ltu.se",
        "expertise": "Entrained flow gasification, hydrogen",
        "reference": "Your leadership of IEA Task 33 and expertise in entrained flow gasification"
    },
    {
        "name": "Prof. Sergio Rapagna",
        "email": "srapagna@unite.it",
        "expertise": "DFB gasification, CHP systems",
        "reference": "Your extensive research on DFB gasification and CHP system integration"
    },
    {
        "name": "Dr. Kyriakos Panopoulos",
        "email": "panopoulos@certh.gr",
        "expertise": "Biomass gasification, SOFC",
        "reference": "Your research on biomass gasification and SOFC system integration at CERTH"
    },
    {
        "name": "Prof. Marco Baratieri",
        "email": "marco.baratieri@unibz.it",
        "expertise": "Biomass gasification, CHP",
        "reference": "Your expertise in biomass gasification, CHP systems, and tar characterization"
    },
    {
        "name": "Prof. Klas Engvall",
        "email": "kengvall@kth.se",
        "expertise": "Fluidized bed, tar cracking",
        "reference": "Your work on fluidized bed gasification and catalytic tar cracking"
    },
    {
        "name": "Prof. Kentaro Umeki",
        "email": "kentaro.umeki@ltu.se",
        "expertise": "Fuel conversion, scale-up",
        "reference": "Your research on fuel conversion and gasification system scale-up"
    },
    {
        "name": "Dr. Rahul Anantharaman",
        "email": "rahul.anantharaman@sintef.no",
        "expertise": "Gas technology, CCS",
        "reference": "Your expertise in gas technology and carbon capture systems at SINTEF"
    }
]

def send_email(researcher):
    """Send single email via SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = researcher['email']
        msg['Subject'] = f"Horizon Europe Collaboration - {researcher['expertise']} - Zero-X Labs"
        
        body = f"""Dear {researcher['name']},

I hope this message finds you well. My name is Clemens, and I lead research partnerships at Zero-X Labs, a division of EX Venture headquartered in Germany.

I am reaching out regarding {researcher['reference']}. Your expertise aligns closely with our work on modular biomass gasification CHP systems.

About Zero-X Labs:
We develop 50kW-500kW modular biomass gasification CHP systems for industrial heat and power applications. Our technology focuses on:
- Downdraft and dual fluidized bed (DFB) gasification
- Advanced tar cracking and syngas cleaning
- Containerized, deployable systems for remote/industrial sites
- Waste-to-energy and circular carbon solutions

Horizon Europe Collaboration Opportunity:

We are actively seeking research partners for upcoming Horizon Europe and EIC Accelerator calls, particularly in:

- Green Deal & Clean Energy: Advanced gasification technologies, syngas quality improvement
- Circular Economy: Waste biomass valorization, biochar applications
- Digital & Industry: Smart CHP systems, predictive maintenance
- Climate & Environment: BECCS, carbon-negative energy systems

Given {researcher['reference'].lower()}, I believe a collaboration could be mutually beneficial - combining your academic expertise with our industrial development capabilities.

Would you be open to a brief call in the coming weeks to explore potential synergy? I am particularly interested in discussing:

- Joint Horizon Europe project proposals
- Research collaboration on gasification optimization
- Pilot plant testing opportunities

Please let me know your availability, or if you would prefer to continue this discussion via email first.

Thank you for your time and consideration. I look forward to hearing from you.

Best regards,

Clemens
Head of Research Partnerships
Zero-X Labs | EX Venture

zerox@exventure.co
www.exventure.co | www.zero-x.co

EX Venture GmbH | Am Sandtorkai 72 | 20457 Hamburg | Germany"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        
        print(f"✅ SENT: {researcher['name']} ({researcher['email']})")
        return True
        
    except Exception as e:
        print(f"❌ FAILED: {researcher['name']} - {str(e)[:50]}")
        return False

def main():
    print("="*60)
    print("SENDING 10 HORIZON EUROPE EMAILS - PYTHON SMTP")
    print("="*60)
    print()
    
    sent = 0
    failed = 0
    
    for i, researcher in enumerate(RESEARCHERS, 1):
        print(f"[{i}/10] ", end="", flush=True)
        if send_email(researcher):
            sent += 1
        else:
            failed += 1
        time.sleep(1)
    
    print()
    print("="*60)
    print("SUMMARY")
    print("="*60)
    print(f"✅ Sent: {sent}")
    print(f"❌ Failed: {failed}")
    print(f"Total: {sent + failed}")

if __name__ == "__main__":
    main()