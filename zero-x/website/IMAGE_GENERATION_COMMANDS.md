# IMAGE GENERATION COMMANDS FOR ZERO-X WEBSITE
## Using DALL-E 3 (OpenAI)

---

## IMAGE 1: HERO BACKGROUND - X-150 Container

**Prompt:**
```
Industrial 20-foot shipping container in clean white color with blue and green accents, labeled "ZERO-X" on the side, showing advanced gasification technology inside with visible pipes, reactors, and control systems. Professional product photography style, dramatic lighting, industrial setting with clean concrete floor, sunset sky in background, modern sustainable energy aesthetic, 8k quality, photorealistic
```

**Size:** 1792x1024 (wide)
**Quality:** HD
**Save as:** hero-x150-container.png

---

## IMAGE 2: PROCESS DIAGRAM - Waste to Energy Flow

**Prompt:**
```
Clean technical infographic showing waste-to-energy process flow: left side shows organic waste/biomass entering, middle shows gasification reactor with flames and heat, right side shows clean syngas and electricity output. Blue and green color scheme, white background, modern flat design style, icons for each step, arrows showing flow direction, professional engineering diagram aesthetic, minimal text
```

**Size:** 1024x1024 (square)
**Quality:** HD
**Save as:** process-flow-diagram.png

---

## IMAGE 3: PARTNER ECOSYSTEM VISUAL

**Prompt:**
```
Abstract network visualization showing 5 connected nodes in a circle, each node representing a company partner. Central hub labeled "ZERO-X GROUP". Nodes connected by glowing lines. Blue, green, and orange color palette. Modern tech aesthetic, dark background with glowing elements, futuristic but professional, corporate partnership visualization, 3D isometric style
```

**Size:** 1792x1024 (wide)
**Quality:** HD
**Save as:** partner-ecosystem.png

---

## IMAGE 4: TECHNOLOGY CLOSE-UP - Gasification Reactor

**Prompt:**
```
Close-up technical photograph of industrial gasification reactor chamber, showing high-grade steel construction, glowing orange heat inside, intricate pipe connections, pressure gauges, professional industrial photography, dramatic lighting highlighting metal textures, clean engineering, power plant aesthetic, photorealistic, 8k detail
```

**Size:** 1024x1024 (square)
**Quality:** HD
**Save as:** reactor-closeup.png

---

## IMAGE 5: RESEARCH COLLABORATION

**Prompt:**
```
Modern research laboratory setting with scientists in white coats working with advanced equipment, gasification testing apparatus, computer screens showing data, Fraunhofer institute style clean white lab, professional scientific photography, bright natural lighting, teamwork and collaboration, high-tech research environment, photorealistic
```

**Size:** 1792x1024 (wide)
**Quality:** HD
**Save as:** research-lab.png

---

## IMAGE 6: BLOG HEADER - Sustainability

**Prompt:**
```
Abstract sustainability concept: circular economy visualization, green leaves intertwined with industrial gears, renewable energy symbols, clean blue sky background, hopeful and innovative mood, modern corporate illustration style, blue and green color scheme, professional marketing aesthetic, 16:9 aspect ratio
```

**Size:** 1792x1024 (wide)
**Quality:** HD
**Save as:** blog-sustainability.png

---

## COMMANDS TO RUN

**With environment variable set:**
```bash
export OPENAI_API_KEY="your-key-here"

# Hero image
cd /opt/homebrew/lib/node_modules/openclaw/skills/openai-image-gen
python3 scripts/gen.py --model dall-e-3 --prompt "PROMPT_HERE" --output ~/.openclaw/workspace/zero-x/website/images/hero-x150-container.png --quality hd --size 1792x1024

# Process diagram
python3 scripts/gen.py --model dall-e-3 --prompt "PROMPT_HERE" --output ~/.openclaw/workspace/zero-x/website/images/process-flow-diagram.png --quality hd --size 1024x1024

# Partner ecosystem
python3 scripts/gen.py --model dall-e-3 --prompt "PROMPT_HERE" --output ~/.openclaw/workspace/zero-x/website/images/partner-ecosystem.png --quality hd --size 1792x1024

# Reactor closeup
python3 scripts/gen.py --model dall-e-3 --prompt "PROMPT_HERE" --output ~/.openclaw/workspace/zero-x/website/images/reactor-closeup.png --quality hd --size 1024x1024

# Research lab
python3 scripts/gen.py --model dall-e-3 --prompt "PROMPT_HERE" --output ~/.openclaw/workspace/zero-x/website/images/research-lab.png --quality hd --size 1792x1024

# Blog header
python3 scripts/gen.py --model dall-e-3 --prompt "PROMPT_HERE" --output ~/.openclaw/workspace/zero-x/website/images/blog-sustainability.png --quality hd --size 1792x1024
```

---

## UPLOAD TO BASE44

After generation, upload images to:
1. Go to https://app.base44.com/apps/6989df145d41eebf80a51614/editor/preview
2. Navigate to Assets/Images section
3. Upload each image
4. Reference in respective sections

---

**All prompts optimized for DALL-E 3 HD quality**
