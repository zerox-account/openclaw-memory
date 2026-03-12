#!/bin/bash
# Zero-X Scheduled Outreach - 32 Emails Over 8 Hours
# Schedule: 4 emails per hour starting at 03:00 SGT

HOUR=$(date +%H)
MINUTE=$(date +%M)

# Define email batches by hour
# Hour 03:00 - Batch 1 (4 emails)
# Hour 04:00 - Batch 2 (4 emails)
# Hour 05:00 - Batch 3 (4 emails)
# Hour 06:00 - Batch 4 (4 emails)
# Hour 07:00 - Batch 5 (4 emails)
# Hour 08:00 - Batch 6 (4 emails)
# Hour 09:00 - Batch 7 (4 emails)
# Hour 10:00 - Batch 8 (4 emails)

API_KEY="am_us_328c7c711eb4ad0cf6b7acad7cd9b94377c66bdc71d719963002e9a371884f82"
FROM="zero-x@agentmail.to"

case $HOUR in
  03)
    # Batch 1: CERTH Greece (4 contacts)
    send_email "angel@cperi.certh.gr" "Dr. Lappas" "English"
    send_email "sbezerg@certh.gr" "Dr. Bezergianni" "English"
    send_email "panopoulos@certh.gr" "Dr. Panopoulos" "English"
    send_email "sstefanidis@cperi.certh.gr" "Dr. Stefanidis" "English"
    ;;
  04)
    # Batch 2: More CERTH + HZDR (4 contacts)
    send_email "drakopoulos@certh.gr" "Dr. Rakopoulos" "English"
    send_email "spapadopoulos@cperi.certh.gr" "Dr. Papadopoulos" "English"
    send_email "e.schleicher@hzdr.de" "Dr. Schleicher" "German"
    send_email "kristina.iisa@nrel.gov" "Dr. Iisa" "English"
    ;;
  05)
    # Batch 3: Top EU Universities (4 contacts)
    send_email "kevin.vangeem@kuleuven.be" "Prof. Van Geem" "English"
    send_email "hartmut.spliethoff@tum.de" "Prof. Spliethoff" "German"
    send_email "ralf.peters@dlr.de" "Prof. Peters" "German"
    send_email "matthias.gaderer@tum.de" "Prof. Gaderer" "German"
    ;;
  06)
    # Batch 4: Nordic + International (4 contacts)
    send_email "esa.vakkilainen@lut.fi" "Prof. Vakkilainen" "English"
    send_email "oyvind.skreiberg@sintef.no" "Prof. Skreiberg" "English"
    send_email "rahul.anantharaman@sintef.no" "Rahul Anantharaman" "English"
    send_email "nimingjiang@zju.edu.cn" "Prof. Ni" "English"
    ;;
  07)
    # Batch 5: Italian Network (4 contacts)
    send_email "salvatore.freni@itae.cnr.it" "Dr. Freni" "English"
    send_email "donatella.barisano@enea.it" "Dr. Barisano" "English"
    send_email "marco.baratieri@unibz.it" "Prof. Baratieri" "English"
    send_email "sergio.rapagna@unite.it" "Prof. Rapagna" "English"
    ;;
  08)
    # Batch 6: French + Spanish (4 contacts)
    send_email "ange.nzihou@mines-albi.fr" "Prof. Nzihou" "English"
    send_email "maria.gonzalez@mines-albi.fr" "Dr. Gonzalez Martinez" "English"
    send_email "mpilargg@unizar.es" "Prof. González García" "English"
    send_email "pierugofoscolo@univaq.it" "Prof. Foscolo" "English"
    ;;
  09)
    # Batch 7: More International (4 contacts)
    send_email "joakim.lundgren@ltu.se" "Prof. Lundgren" "English"
    send_email "kentaro.umeki@ltu.se" "Prof. Umeki" "English"
    send_email "klas.engvall@sche.kth.se" "Prof. Engvall" "English"
    send_email "thodoros@auth.gr" "Dr. Damartzis" "English"
    ;;
  10)
    # Batch 8: Final batch (4 contacts)
    send_email "nathalie.lyczko@mines-albi.fr" "Dr. Lyczko" "English"
    send_email "v.manelfi@reset-energy.it" "Valerio Manelfi" "English"
    send_email "madeleine.alphen@atee.fr" "Madeleine Alphen" "English"
    send_email "peter@phiventures.net" "Peter Hlavnicka" "English"
    ;;
esac

send_email() {
  local email=$1
  local name=$2
  local lang=$3
  
  if [ "$lang" == "German" ]; then
    subject="Forschungskollaboration – Multi-Fuel CHP System X-150"
  else
    subject="Research Collaboration – Multi-Fuel CHP System X-150"
  fi
  
  echo "$(date): Sending to $name ($email)" >> /Users/julienuhlig/.openclaw/workspace/memory/scheduled_outreach.log
}
