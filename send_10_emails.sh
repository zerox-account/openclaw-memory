#!/bin/bash
# Send 10 Horizon Europe emails using Himalaya

RESEARCHERS=(
  "henrik.thunman@chalmers.se:Prof. Henrik Thunman:Chalmers University of Technology:DFB gasification, GoBiGas plant, waste gasification:Your leadership of the GoBiGas project and expertise in dual fluidized bed gasification"
  "ange.nzihou@mines-albi.fr:Prof. Ange Nzihou:IMT Mines Albi:Thermochemical processes, tar reforming, biochar:Your distinguished work on tar reforming and thermochemical conversion processes"
  "pierugo.foscolo@univaq.it:Prof. Pier Ugo Foscolo:University of L'Aquila:DFB gasification, 5 MW pilot plant:Your pioneering work on dual fluidized bed gasification and the 5 MW L'Aquila pilot plant"
  "joakim.lundgren@ltu.se:Prof. Joakim Lundgren:Luleå University of Technology:Entrained flow gasification, hydrogen, IEA Task 33:Your leadership of IEA Task 33 and expertise in entrained flow gasification"
  "srapagna@unite.it:Prof. Sergio Rapagna:University of Teramo:DFB gasification, CHP systems, syngas:Your extensive research on DFB gasification and CHP system integration"
  "panopoulos@certh.gr:Dr. Kyriakos Panopoulos:CERTH/CPERI:Biomass gasification, syngas, SOFC integration:Your research on biomass gasification and SOFC system integration at CERTH"
  "marco.baratieri@unibz.it:Prof. Marco Baratieri:Free University of Bozen:Biomass gasification, CHP, tar analysis:Your expertise in biomass gasification, CHP systems, and tar characterization"
  "kengvall@kth.se:Prof. Klas Engvall:KTH Royal Institute of Technology:Fluidized bed, tar cracking, catalysts:Your work on fluidized bed gasification and catalytic tar cracking"
  "kentaro.umeki@ltu.se:Prof. Kentaro Umeki:Luleå University of Technology:Fuel conversion, gasification, scale-up:Your research on fuel conversion and gasification system scale-up"
  "rahul.anantharaman@sintef.no:Dr. Rahul Anantharaman:SINTEF Energy Research:Gas technology, CCS, industrial applications:Your expertise in gas technology and carbon capture systems at SINTEF"
)

echo "=========================================="
echo "SENDING 10 HORIZON EUROPE EMAILS"
echo "=========================================="
echo ""

sent=0
failed=0

for researcher in "${RESEARCHERS[@]}"; do
  IFS=':' read -r email name institution expertise reference <<< "$researcher"
  
  subject="Horizon Europe Collaboration - ${expertise%%,*} - Zero-X Labs/EX Venture"
  
  body="Dear ${name},

I hope this message finds you well. My name is Clemens, and I lead research partnerships at Zero-X Labs, a division of EX Venture headquartered in Germany.

I am reaching out regarding ${reference}. Your expertise aligns closely with our work on modular biomass gasification CHP systems.

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

Given ${reference,,}, I believe a collaboration could be mutually beneficial - combining your academic expertise with our industrial development capabilities.

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

EX Venture GmbH | Am Sandtorkai 72 | 20457 Hamburg | Germany"

  echo "Sending to: ${name} (${email})"
  
  if echo "$body" | himalaya message write -H "To:${email}" -H "Subject:${subject}"; then
    echo "  ✅ Sent successfully"
    ((sent++))
  else
    echo "  ❌ Failed"
    ((failed++))
  fi
  
  sleep 3
done

echo ""
echo "=========================================="
echo "SUMMARY"
echo "=========================================="
echo "Sent: ${sent}"
echo "Failed: ${failed}"
echo "Total: $((sent + failed))"