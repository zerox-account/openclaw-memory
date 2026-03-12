# TOOLS.md - Agent Cool Tools & Commands

## Command Triggers

| Command | Action |
|---------|--------|
| `/application [type]` | Analyze specific cooling application |
| `/sizing [kW]` | Size absorption chiller for heat input |
| `/economics` | Calculate trigeneration economics |
| `/compare` | Compare LiBr vs. ammonia systems |
| `/partners` | Identify chiller OEM partners |
| `/cases` | Show reference installations |

## Absorption Cooling Fundamentals

### Lithium Bromide (LiBr) Water Chillers
**How it works:**
- LiBr solution absorbs water vapor (evaporation = cooling)
- Heat drives regeneration (separates LiBr and water)
- Water vapor condenses, evaporates, repeats

**Specifications:**
- COP: 0.7-0.8 (single-effect)
- COP: 1.2-1.4 (double-effect, requires 150°C+)
- Heat input: 90°C minimum (single-effect)
- Chilled water: 7°C standard, 5°C possible
- Cooling water: 30°C (cooling tower)

**Advantages:**
- High efficiency at low heat temperatures
- Non-toxic (water + salt)
- Proven technology (decades of operation)
- Quiet operation

**Challenges:**
- Crystallization risk (if temperature drops)
- Vacuum maintenance required
- Limited to above-freezing applications
- Corrosion inhibitors needed

**Major Manufacturers:**
- Carrier (AquaForce)
- Trane (Absorption Chillers)
- Yazaki
- Broad
- Thermax

### Ammonia-Water Absorption
**How it works:**
- Ammonia evaporates at low pressure (cooling)
- Heat drives ammonia out of water solution
- Ammonia condenses, expands, evaporates

**Specifications:**
- COP: 0.5-0.6
- Heat input: 100-150°C
- Can achieve sub-zero temperatures
- Higher pressure operation

**Advantages:**
- Sub-zero cooling possible
- No crystallization issues
- Robust technology

**Challenges:**
- Toxicity (ammonia)
- Higher pressure (safety requirements)
- Lower COP than LiBr
- Noise (pumps, rectifier)

**Applications:**
- Industrial refrigeration
- Ice production
- Cold storage (-10°C to -30°C)

## Sizing Calculations

### Basic Formula
```
Cooling Capacity (kWc) = Heat Input (kWth) × COP

Example:
X-150 waste heat: 350 kWth
LiBr COP: 0.75
Cooling capacity: 350 × 0.75 = 262.5 kWc
```

### Cooling Load Conversion
```
Tons of Refrigeration (TR) = kWc / 3.517

Example:
262.5 kWc = 74.6 TR
(1 TR = 3.517 kW cooling)
```

### Annual Energy Production
```
Cooling Energy (kWh/year) = Cooling Capacity (kW) × Operating Hours

Example:
262.5 kW × 6,000 h/year = 1,575,000 kWh/year
```

## Economic Analysis

### Trigeneration vs. Power-Only

**Power-Only X-150:**
- Electrical output: 150 kWe
- Annual electricity: 150 kW × 6,000 h = 900,000 kWh
- Value @ €0.15/kWh: €135,000/year
- Fuel cost: €54,000/year (assumed)
- Net value: €81,000/year

**Trigeneration X-150:**
- Electrical output: 150 kWe (€135,000/year)
- Cooling output: 262.5 kWc
- Annual cooling: 262.5 kW × 6,000 h = 1,575,000 kWh
- Value @ €0.12/kWh: €189,000/year
- Fuel cost: €54,000/year (same fuel)
- Net value: €270,000/year

**Incremental Value:** €189,000/year (2.3x improvement)

### Payback Calculation
```
Additional Investment: €80,000 (chiller + heat exchangers + installation)
Annual Savings: €189,000 (cooling value)
Simple Payback: €80,000 / €189,000 = 0.42 years (5 months)
```

## Application Profiles

### Data Centers
**Cooling Demand:**
- PUE (Power Usage Effectiveness) target: 1.2-1.4
- Cooling typically 30-40% of total energy
- Baseload operation (8,760 h/year)

**X-150 Fit:**
- Electrical: 150 kW for servers
- Cooling: 262 kW for HVAC
- Perfect match for small-medium edge data centers

**Value Proposition:**
- Reliable baseload cooling
- Reduced grid dependence
- Lower PUE
- Carbon reduction

**Challenges:**
- Reliability requirements (need backup)
- Precision cooling (±1°C)
- 24/7 operation critical

### Food Processing
**Cooling Demand:**
- Cold storage: 0°C to -25°C
- Process cooling: 5°C to 15°C
- Blast freezing: -35°C to -40°C

**X-150 Fit:**
- LiBr for process cooling (5-15°C)
- Ammonia for cold storage/freezing
- Electrical for processing equipment

**Value Proposition:**
- On-site cooling reduces spoilage
- Lower energy costs
- Waste heat utilization
- Food safety compliance

**Target Sub-sectors:**
- Dairy processing
- Meat processing
- Cold storage warehouses
- Breweries

### Pharmaceuticals
**Cooling Demand:**
- Clean rooms: 18-22°C, strict humidity control
- Process cooling: 5-15°C
- Storage: 2-8°C (vaccines)

**X-150 Fit:**
- LiBr for HVAC and process
- Electrical for equipment
- High reliability requirement

**Value Proposition:**
- Reliable cooling for critical processes
- Reduced energy costs
- Backup power + cooling in one system

**Challenges:**
- Validation requirements (GMP)
- Precision control
- Regulatory compliance

## Partner Identification

### Chiller OEMs (Potential Partners)
**Large Industrial:**
- Carrier (USA)
- Trane (USA)
- Johnson Controls (USA)

**European:**
- Viessmann (Germany)
- Bosch (Germany)
- AGO (Germany)

**Asian:**
- Yazaki (Japan)
- Broad (China)
- Thermax (India)

### Integration Approach
**Option 1: OEM Partnership**
- Zero-X provides gasifier + heat exchanger
- OEM provides absorption chiller
- Joint system integration
- Shared project development

**Option 2: Component Procurement**
- Zero-X procures chillers from OEM
- Full system integration by Zero-X
- Single point of responsibility

**Option 3: Turnkey Subcontract**
- Chiller installation by HVAC contractor
- Zero-X focuses on gasification
- Split responsibility

## Reference Installations

### To Research
- [ ] Trigeneration biomass installations in Europe
- [ ] Data center trigeneration projects
- [ ] Food industry CHC applications
- [ ] Hospital trigeneration systems

### Known Examples
- **Austria:** Biomass trigeneration in district heating
- **Germany:** Industrial CHC in paper mills
- **Denmark:** District cooling from biomass

## Technical Resources

### Standards & Guidelines
- **ASHRAE:** Absorption cooling standards
- **VDI:** German engineering guidelines
- **Eurovent:** Chiller performance certification

### Calculation Tools
- **TRNSYS:** System simulation
- **EnergyPlus:** Building energy modeling
- **Excel:** Basic economic analysis

### Key Metrics
- **COP:** Coefficient of Performance (cooling/heat)
- **EER:** Energy Efficiency Ratio (cooling/power)
- **PUE:** Power Usage Effectiveness (data centers)
- **SPF:** Seasonal Performance Factor
