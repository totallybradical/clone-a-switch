# clone-a-switch

## Setup
1. Start by cloning the git repo or downloading the zip
```
git clone https://github.com/totallybradical/clone-a-switch.git
```

2. Navigate into the directory
```
cd clone-a-switch/
```

3. OPTIONAL: I'd recommend creating a virtual python environment for this script
```
python3 -m venv venv
source venv/bin/activate
```

4. Install the necessary libraries
```
pip install -r requirements.txt
```

5. Edit line 7 in **clone_switch.py** to include your Meraki API key
``` python
API_KEY = 'YOUR_API_KEY_HERE'
```

## Execution
1. Run the script
```
python clone_switch.py
```

2. During execution you will be prompted for the source switch serial and the destination switch serial (example below)
```
Enter source switch serial: AAAA-BBBB-CCCC
Enter destination switch serial: DDDD-EEEE-FFFF
```

## Other Info
When executed this script will create a backup of the switchports config for both the source and destination switches. These will be placed in the **config_backups** folder