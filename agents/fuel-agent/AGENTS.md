# AGENTS.md - Agent Fuel Workspace Rules

## First Run

If `BOOTSTRAP.md` exists, follow initialization, then delete.

## Every Session

Before starting work:

1. **Read SOUL.md** - Who you are (fuel expert)
2. **Read IDENTITY.md** - Calculation methodologies
3. **Read USER.md** - Zero-X fuel context
4. **Read memory/YYYY-MM-DD.md** - Today's activities
5. **Read MEMORY.md** - Fuel database and cases

## Calculation Standards

### Required for Every Fuel Analysis

**Basic Information:**
- [ ] Fuel type and source
- [ ] Moisture content (as-received basis)
- [ ] Heating value (dry basis)
- [ ] Bulk density
- [ ] Ash content

**Conversions:**
- [ ] Wet tons to dry tons calculated
- [ ] Energy per wet tonne determined
- [ ] Energy per cubic meter (if relevant)

**Economics:**
- [ ] Purchase/gate fee cost
- [ ] Transport cost per MWh
- [ ] Pre-processing costs
- [ ] Total delivered cost per MWh

**Logistics:**
- [ ] Transport distance and mode
- [ ] Storage requirements
- [ ] Handling equipment needs
- [ ] Supply reliability assessment

### Sludge-Specific Requirements

**Additional for sludge:**
- [ ] Dewatering method and cost
- [ ] Drying requirements and energy source
- [ ] Regulatory compliance (pathogens, metals)
- [ ] Odour control measures
- [ ] Public perception/acceptance

## Documentation Standards

### Fuel Data Sheet Template

```
FUEL: [Name]
SOURCE: [Supplier/Location]

PHYSICAL PROPERTIES:
- Moisture content: X% (as-received)
- Dry matter: Y%
- Bulk density: Z kg/m³
- Particle size: A-B mm

ENERGY PROPERTIES:
- HHV (dry): X MJ/kg
- HHV (as-received): Y MJ/kg
- Energy density: Z MWh/tonne

ECONOMICS:
- Purchase price: €X/tonne (wet)
- Transport: €Y/tonne
- Pre-processing: €Z/tonne
- TOTAL: €X+Y+Z/tonne wet
- Cost per MWh: €(X+Y+Z)/Z

LOGISTICS:
- Max transport distance: X km
- Storage requirements: Y m³/MWh
- Supply reliability: [High/Med/Low]

RECOMMENDATION: [Use/Reject/Investigate]
```

## Quality Control

### Red Flags (Stop and Escalate)

- Moisture content >80% without drying plan
- Transport cost >€50/MWh
- Inconsistent supply (no backup)
- Regulatory uncertainty
- High contamination (damage risk)

### Yellow Flags (Investigate Further)

- Moisture 50-70% (drying needed)
- Transport 100-300km
- Seasonal availability
- New supplier (no track record)
- Complex handling requirements

## Communication Rules

### With User (Clemens/Zero-X)

- Lead with cost per MWh (not per tonne)
- Specify moisture content every time
- Show wet and dry calculations
- Highlight risks and mitigation
- Recommend alternatives if marginal

### External Communications (if authorized)

- Use standard fuel data sheet format
- Include all assumptions
- Provide ranges, not single points
- Note measurement methods

## Continuous Improvement

### Weekly
- Update fuel pricing database
- Review new fuel sources
- Refine calculation tools

### Monthly
- Benchmark against actual projects
- Update transport cost indices
- Review sludge opportunities

### Quarterly
- Full fuel database review
- New technology assessment
- Regional market analysis
