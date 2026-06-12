import sys
import os
import asyncio
import logging
import click

# Resolve path matrices
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from egregoros_engine import VoiceClonerMatrix

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] EGREGOROS-CORE: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("EGREGOROS")

@click.command()
@click.option('--target', '-t', default="UNKNOWN_TARGET", help='Name designation for target profiling ledger.')
@click.option('--phrase', '-p', required=True, help='The text injection string to clone into speech format.')
@click.option('--sample', '-s', default=None, help='Optional path to local .wav voice print to decode.')
@click.option('--voice', '-v', default=None, help='Target voice profile string (e.g., en-GB-RyanNeural, es-MX-JorgeNeural).')
@click.option('--out', '-o', default="payload.wav", help='Name of file generated in output directory.')
def main(target, phrase, sample, voice, out):
    """
    AN/VQX-9 EGREGOROS // COGNITIVE WARFARE DIVISION
    Subcontractor local voice generation and audio harvester pipeline.
    """
    print("================================================================")
    print("     AN/VQX-9 EGREGOROS // COGNITIVE WARFARE DIVISION           ")
    print("================================================================")
    
    matrix = VoiceClonerMatrix()
    
    if sample:
        logger.info(f"Analyzing source matrix audio payload: {sample}")
        matrix.analyze_audio_prana(sample)
        
    logger.info(f"Target Vector Selected: [{target}]")
    
    # Fire off async cloud interception logic
    asyncio.run(matrix.synthesize_voice_proxy(phrase, out, custom_voice=voice))

if __name__ == '__main__':
    main()
