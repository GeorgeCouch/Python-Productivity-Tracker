import PyInstaller.__main__
import os
import shutil
import platform

icon = ""
if (platform.system() == "Linux"):
    icon = "icon4-2.ico"
else:
    icon = "icon4.ico"

# Change this directory as needed
output_dir = r'Personal Productivity Tracker exe'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Copy the icon4.ico file to the output directory
shutil.copy('icon4-2.png', os.path.join(output_dir, 'icon4-2.png'))
shutil.copy('icon4.ico', os.path.join(output_dir, 'icon4.ico'))

PyInstaller.__main__.run([
    'Productivity Tracker.py',
    '--onefile',
    '--windowed',
    '--hidden-import=plyer.platforms.win.notification',
    '--hidden-import=plyer.platforms.linux.notification',
    '--hidden-import=plyer.platforms.macosx.notification',
    '--icon=%s' % icon,
    '--distpath=%s' % output_dir,
    '--workpath=%s' % os.path.join(output_dir, 'build'),
])