"""
Remappings.

   - Read in YAML remappings file formatting as dictionary pairs
   - Convert dictionary to list so it can be passed into the remappings argument of a launch Node command
"""

import os
import yaml

def get_remappings(config_dir):
    remapping_yaml = os.path.join(config_dir, 'remappings.yaml')
    with open(remapping_yaml, "r") as remapping_file:
        remappings = yaml.safe_load(remapping_file)
        return list(remappings.items())
