# Usage Manual: AN/VQX-9 EGREGOROS

## Overview
EGREGOROS operates as an asynchronous voice synthesis framework. It fetches raw audio from a cloud proxy (`edge-tts`) and processes it locally using `pydub`.

## Execution
Use the provided shell templates located in `scripts/`:

1. **Synthesis:**
   ```bash
   ./scripts/run_synthesis.sh "<Your Text>" <output_filename.mp3>
   ```

## Profile Usage
To synthesize using Lancy Lough's markers, ensure the profile is loaded via the configuration:

```bash
# Set profile in environment or config
export EGREGOROS_PROFILE="profiles/lancy_lough.json"
./scripts/run_synthesis.sh "Proceed with the design." out.mp3
```
