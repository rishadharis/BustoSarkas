import sys
import os

# Ensure current directory is in path
sys.path.append(os.getcwd())

print("Verifying imports...")

try:
    print("Importing utils...")
    import utils
    print("utils imported successfully.")
except Exception as e:
    print(f"Failed to import utils: {e}")
    sys.exit(1)

try:
    print("Importing Tools.tools...")
    from Tools import tools
    print("Tools.tools imported successfully.")
except Exception as e:
    print(f"Failed to import Tools.tools: {e}")
    sys.exit(1)

try:
    print("Importing Agents.linkedin_lookup_agent...")
    from Agents import linkedin_lookup_agent
    print("Agents.linkedin_lookup_agent imported successfully.")
except Exception as e:
    print(f"Failed to import Agents.linkedin_lookup_agent: {e}")
    sys.exit(1)

try:
    print("Importing sarkas...")
    import sarkas
    print("sarkas imported successfully.")
except Exception as e:
    print(f"Failed to import sarkas: {e}")
    sys.exit(1)

# app.py is a streamlit app, might have issues with direct import if it runs code on import, 
# but let's try importing it to check for syntax errors. 
# It has `if __name__ == "__main__": main()` so it should be safe to import.
try:
    print("Importing app...")
    import app
    print("app imported successfully.")
except Exception as e:
    print(f"Failed to import app: {e}")
    sys.exit(1)

print("\nAll imports successful! Code syntax and structural integrity appear correct.")
