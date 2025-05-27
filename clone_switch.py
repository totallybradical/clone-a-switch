
import datetime
import json
import meraki
from pathlib import Path

# API_KEY = 'YOUR_API_KEY_HERE'
dashboard = meraki.DashboardAPI()

# Ask User for Source / Destination Switch
source_switch_serial = input("Enter source switch serial: ")
destination_switch_serial = input("Enter destination switch serial: ")

# Create Config Backup Folder (Today's Date)
backup_folder = f"./config_backups/{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
Path(backup_folder).mkdir(parents=True, exist_ok=True)

# Backup Current Configs
source_switch_current_config_switchports = dashboard.switch.getDeviceSwitchPorts(source_switch_serial)
# Write source switch config backup
with open(f'{backup_folder}/{source_switch_serial}.json', 'w', encoding='utf-8') as f:
    json.dump(source_switch_current_config_switchports, f, ensure_ascii=False, indent=4)
destination_switch_current_config_switchports = dashboard.switch.getDeviceSwitchPorts(destination_switch_serial)
# Write destination switch config backup
with open(f'{backup_folder}/{destination_switch_serial}.json', 'w', encoding='utf-8') as f:
    json.dump(destination_switch_current_config_switchports, f, ensure_ascii=False, indent=4)

# Perform clone
for source_port in source_switch_current_config_switchports: # Loop through each port
    if source_port['type'] == 'trunk': # If trunk type... 
        # Clone only trunk-related configs
        dashboard.switch.updateDeviceSwitchPort(
            serial=destination_switch_serial,
            portId=source_port['portId'],
            name=source_port['name'],
            tags=source_port['tags'],
            enabled=source_port['enabled'],
            poeEnabled=source_port['poeEnabled'],
            type=source_port['type'],
            vlan=source_port['vlan'],
            allowedVlans=source_port['allowedVlans'],
            isolationEnabled=source_port['isolationEnabled'],
            rstpEnabled=source_port['rstpEnabled'],
            stpGuard=source_port['stpGuard'],
            linkNegotiation=source_port['linkNegotiation'],
            portScheduleId=source_port['portScheduleId'],
            udld=source_port['udld']
        )
    elif source_port['type'] == 'access': # If access type...
        if source_port['accessPolicyType'] == 'Open': # If 'Open' access type..
            # Clone 'Open' access-related configs
            dashboard.switch.updateDeviceSwitchPort(
                serial=destination_switch_serial,
                portId=source_port['portId'],
                name=source_port['name'],
                tags=source_port['tags'],
                enabled=source_port['enabled'],
                poeEnabled=source_port['poeEnabled'],
                type=source_port['type'],
                vlan=source_port['vlan'],
                voiceVlan=source_port['voiceVlan'],
                isolationEnabled=source_port['isolationEnabled'],
                rstpEnabled=source_port['rstpEnabled'],
                stpGuard=source_port['stpGuard'],
                linkNegotiation=source_port['linkNegotiation'],
                portScheduleId=source_port['portScheduleId'],
                udld=source_port['udld'],
                accessPolicyType=source_port['accessPolicyType']
            )
        elif source_port['accessPolicyType'] == 'Custom access policy': # If 'Custom access policy' type...
            # Clone 'Custom access policy' access-related configs
            dashboard.switch.updateDeviceSwitchPort(
                serial=destination_switch_serial,
                portId=source_port['portId'],
                name=source_port['name'],
                tags=source_port['tags'],
                enabled=source_port['enabled'],
                poeEnabled=source_port['poeEnabled'],
                type=source_port['type'],
                vlan=source_port['vlan'],
                voiceVlan=source_port['voiceVlan'],
                isolationEnabled=source_port['isolationEnabled'],
                rstpEnabled=source_port['rstpEnabled'],
                stpGuard=source_port['stpGuard'],
                linkNegotiation=source_port['linkNegotiation'],
                portScheduleId=source_port['portScheduleId'],
                udld=source_port['udld'],
                accessPolicyType=source_port['accessPolicyType'],
                accessPolicyNumber=source_port['accessPolicyNumber']
            )
        elif source_port['accessPolicyType'] == 'MAC allow list': # If 'MAC allow list' type...
            # Clone 'MAC allow list' access-related configs
            dashboard.switch.updateDeviceSwitchPort(
                serial=destination_switch_serial,
                portId=source_port['portId'],
                name=source_port['name'],
                tags=source_port['tags'],
                enabled=source_port['enabled'],
                poeEnabled=source_port['poeEnabled'],
                type=source_port['type'],
                vlan=source_port['vlan'],
                voiceVlan=source_port['voiceVlan'],
                isolationEnabled=source_port['isolationEnabled'],
                rstpEnabled=source_port['rstpEnabled'],
                stpGuard=source_port['stpGuard'],
                linkNegotiation=source_port['linkNegotiation'],
                portScheduleId=source_port['portScheduleId'],
                udld=source_port['udld'],
                accessPolicyType=source_port['accessPolicyType'],
                macAllowList=source_port['macAllowList']
            ) 
        elif source_port['accessPolicyType'] == 'Sticky MAC allow list': # If 'Sticky MAC allow list' type...
            # Clone 'Sticky MAC allow list' access-related configs
            dashboard.switch.updateDeviceSwitchPort(
                serial=destination_switch_serial,
                portId=source_port['portId'],
                name=source_port['name'],
                tags=source_port['tags'],
                enabled=source_port['enabled'],
                poeEnabled=source_port['poeEnabled'],
                type=source_port['type'],
                vlan=source_port['vlan'],
                voiceVlan=source_port['voiceVlan'],
                isolationEnabled=source_port['isolationEnabled'],
                rstpEnabled=source_port['rstpEnabled'],
                stpGuard=source_port['stpGuard'],
                linkNegotiation=source_port['linkNegotiation'],
                portScheduleId=source_port['portScheduleId'],
                udld=source_port['udld'],
                accessPolicyType=source_port['accessPolicyType'],
                stickyMacAllowList=source_port['stickyMacAllowList'],
                stickyMacAllowListLimit=source_port['stickyMacAllowListLimit']
            )