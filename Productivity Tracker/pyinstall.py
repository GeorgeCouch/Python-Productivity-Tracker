import PyInstaller.__main__
import os
import shutil

# Change this directory as needed
output_dir = r'/home/george/Documents/Personal Productivity Tracker exe'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Copy the icon4.ico file to the output directory
shutil.copy('icon4-2.png', os.path.join(output_dir, 'icon4-2.png'))

PyInstaller.__main__.run([
    'Productivity Tracker.py',
    '--onefile',
    '--windowed',
    '--hidden-import=plyer.platforms.win.notification',
    '--hidden-import=plyer.platforms.linux.notification',
    '--hidden-import=plyer.platforms.macosx.notification',
    #'--add-data=icon4.ico:.',  # This line includes the icon in the bundle
    #'--add-data=%s:.' % os.path.join(output_dir, 'icon4.ico'),  # This line includes the icon in the distpath
    #'--icon=icon4.png',
    '--distpath=%s' % output_dir,
    '--workpath=%s' % os.path.join(output_dir, 'build'),
])