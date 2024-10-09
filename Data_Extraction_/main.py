import subprocess
import sys


subprocess.run([sys.executable, "data_extraction.py"])

subprocess.run([sys.executable, "data_analysis.py"])
