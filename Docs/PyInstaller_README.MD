## PYINSTALLER for standalone Python creations

*Did I ever mention how amazing Python is? Well it is, and here is another guide on something I didnt even know was possible before now.*

This is a guide for anyone creating their own python scripts.

* [Compile pre-reqs](#compile-pre-reqs)
* [Compiling](#compiling)
* [Troubleshooting](#troubleshooting)

&NewLine;
&nbsp;  &nbsp;
&NewLine;
&nbsp;
&NewLine;

## Compile pre-reqs

There are some things you need to consider when building your target app. For customisations yuou will need to have a .ico file, so it doesn't have the standard Python icon. 

This is a sample main.spec file that gets created when you run pyinstaller


```bash
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/abjourney.jpg', 'assets')],
    hiddenimports=['PIL'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/abjourney.ico'],
)
app = BUNDLE(
    exe,
    name='main.app',
    icon='assets/abjourney.ico',
    bundle_identifier=None,
)

```

&NewLine;
&nbsp;  &nbsp;
&NewLine;
&nbsp;
&NewLine;

## Compiling

There are some things to bear in mind when compiling your python file to a standalone app.

Here is an example command to run:

```bash

 pyinstaller --onefile --windowed --add-data "assets/abjourney.jpg:assets" --icon "assets/abjourney.ico" main.py

```
You one thing to note is that when you are adding the data (asset file), it has to be in the form of source:destination. So the example above is in the assets folder and you are making sure it is in the assets folder for the destination app to pick up.

&NewLine;
&nbsp;  &nbsp;
&NewLine;
&nbsp;
&NewLine;


## Troubleshooting

In getting to this point, you can imagine I have stumbled across a few issues that I thought would have been a complete blocker. However, with the power of Google and tenacity, I have been able to resolve them. Hopefulyy this will help you also.

### Architecture

I work on MacOS, however, I do have and Intel based laptop and ARM. I thought that you could simply add a compilation flag to target the operating system (as I will be looking to export to Windows at some point). Unfortunately, at the time of writing, the ability to export to an Intel based Mac from a M2 Mac was not supported.

### Missing modules

This was a weird one.....I use virtual environments to import libraries in python, as I dont want to clog up the main system with all sorts and good, bad and indifferent experiments. Anyway, running the app in Visual Studio code has been successful, however, when running the compiled app, it crashes out. It appears that it was not able to pick up the imported libraries. This is resolved by adding the flag, --hidden-imports and including the library folders you imported. In this example, it was CTkinter and PIL. I tried to compile this outside outside of the virtual environment and it worked for CTkinter, but not PIL. I sorted this out by copying the PIL site-lib folder from the virtual environment and putting it in the same foilder I am running PyInstaller from. No doubt just thinking about it I could have used the mainspec file and put in the path to the library folder.

*The site packages folder in the virtual environment can be found at lib/&lt;python version&gt;/site-packages/&lt;library name&gt;*

### Missing assets

This is similar to the missing modules, for some reason it just doesn't seem to be able to see the assets. The quick way I found was to use the --add-data flag and point to the file. This works for a couple of files, but I would recommend the mainspec file for more that that. I'm not sure if you can use wildcards, but I will be trying that next when I need to reference a larger number of assets.

### Default python icon

I have already mentioned this, but I thought it would be good to reference it here also. Icons make the app look cool and finished, so you will want to add one. Here I am talking about two icons. The system tray icon and the standalone .app file icon, both have default python icons. The former is a .ico file and the latter being a .icns file. The free way is to use an online converters of these image format files.


&NewLine;
&nbsp;  &nbsp;
&NewLine;
&nbsp;
&NewLine;

That pretty much wraps it up, so far with everything tht I have learned about using PyInstaller to create standalone python apps.

Have fun and hope this will help you to create amazing apps of your own.


## References

[AB Website](https://anthony-barrett.uk) - This is where you will find othe things I am working on.

&NewLine;
&nbsp;  &nbsp;
&NewLine;
&nbsp;
&NewLine;
---
(C) 2025 Anthony Barrett - All rights reserved.