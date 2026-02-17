# MacPython/CarbonDocumentation

::: {#content dir="ltr" lang="en"}
# General Tips {#General_Tips}

Try some or all:

- Read Apple Carbon documentation

- Use `dir()`{.backtick} and `help()`{.backtick}

- Look into [MacPython](MacPython) IDE code, or in the few Mac Python modules like `macostools`{.backtick}, `findertools`{.backtick} or other modules in `plat-mac`{.backtick}

- Look into the C modules that implement the glue between Python and Carbon.

- Ask the good people at `#macpython`{.backtick} in `irc.freenode.org`{.backtick}

# Recipes {#Recipes}

## Getting file and folder information {#Getting_file_and_folder_information}

You want to know the file type or creator of a file.

    >>> from Carbon import File
    >>> info = File.FSSpec('Todo').FSpGetFInfo()     
    >>> info.Type
    '****'
    >>> info.Creator
    'Hdra'
    >>> 

Note that FSSpecs have some issues, see [http://developer.apple.com/technotes/tn2002/tn2078.html](http://developer.apple.com/technotes/tn2002/tn2078.html){.http}

Here is another simpler way (from [MacPython](MacPython) IDE):

    >>>import MacOS
    >>> MacOS.GetCreatorAndType('Todo')
    ('Hdra', '****')

# Carbon Reference {#Carbon_Reference}

Python 2.3 Carbon Modules:

- [../AE](./MacPython(2f)AE.html){.nonexistent}

- [../AH](./MacPython(2f)AH.html){.nonexistent}

- [../Aliases](./MacPython(2f)Aliases.html){.nonexistent}

- [../App](./MacPython(2f)App.html){.nonexistent}

- [../Appearance](./MacPython(2f)Appearance.html){.nonexistent}

- [../AppleEvents](./MacPython(2f)AppleEvents.html)

- [../AppleHelp](./MacPython(2f)AppleHelp.html){.nonexistent}

- [../CF](./MacPython(2f)CF.html){.nonexistent}

- [../CG](./MacPython(2f)CG.html){.nonexistent}

- [../CarbonEvents](./MacPython(2f)CarbonEvents.html){.nonexistent}

- [../CarbonEvt](./MacPython(2f)CarbonEvt.html){.nonexistent}

- [../Cm](./MacPython(2f)Cm.html){.nonexistent}

- [../Components](./MacPython(2f)Components.html){.nonexistent}

- [../ControlAccessor](./MacPython(2f)ControlAccessor.html){.nonexistent}

- [../Controls](./MacPython(2f)Controls.html){.nonexistent}

- [../CoreFoundation](./MacPython(2f)CoreFoundation.html){.nonexistent}

- [../CoreGraphics](./MacPython(2f)CoreGraphics.html){.nonexistent}

- [../Ctl](./MacPython(2f)Ctl.html){.nonexistent}

- [../Dialogs](./MacPython(2f)Dialogs.html){.nonexistent}

- [../Dlg](./MacPython(2f)Dlg.html){.nonexistent}

- [../Drag](./MacPython(2f)Drag.html){.nonexistent}

- [../Dragconst](./MacPython(2f)Dragconst.html){.nonexistent}

- [../Events](./MacPython(2f)Events.html){.nonexistent}

- [../Evt](./MacPython(2f)Evt.html){.nonexistent}

- [../File](./MacPython(2f)File.html){.nonexistent}

- [../Files](./MacPython(2f)Files.html){.nonexistent}

- [../Fm](./MacPython(2f)Fm.html){.nonexistent}

- [../Folder](./MacPython(2f)Folder.html){.nonexistent}

- [../Folders](./MacPython(2f)Folders.html){.nonexistent}

- [../Fonts](./MacPython(2f)Fonts.html){.nonexistent}

- [../Help](./MacPython(2f)Help.html){.nonexistent}

- [../IBCarbon](./MacPython(2f)IBCarbon.html){.nonexistent}

- [../IBCarbonRuntime](./MacPython(2f)IBCarbonRuntime.html){.nonexistent}

- [../Icn](./MacPython(2f)Icn.html){.nonexistent}

- [../Icons](./MacPython(2f)Icons.html){.nonexistent}

- [../List](./MacPython(2f)List.html){.nonexistent}

- [../Lists](./MacPython(2f)Lists.html){.nonexistent}

- [../MacHelp](./MacPython(2f)MacHelp.html){.nonexistent}

- [../MacTextEditor](./MacPython(2f)MacTextEditor.html){.nonexistent}

- [../MediaDescr](./MacPython(2f)MediaDescr.html){.nonexistent}

- [../Menu](./MacPython(2f)Menu.html){.nonexistent}

- [../Menus](./MacPython(2f)Menus.html){.nonexistent}

- [../Mlte](./MacPython(2f)Mlte.html){.nonexistent}

- [../QDOffscreen](./MacPython(2f)QDOffscreen.html){.nonexistent}

- [../Qd](./MacPython(2f)Qd.html){.nonexistent}

- [../Qdoffs](./MacPython(2f)Qdoffs.html){.nonexistent}

- [../Qt](./MacPython(2f)Qt.html){.nonexistent}

- [../QuickDraw](./MacPython(2f)QuickDraw.html){.nonexistent}

- [../QuickTime](./MacPython(2f)QuickTime.html){.nonexistent}

- [../Res](./MacPython(2f)Res.html){.nonexistent}

- [../Resources](./MacPython(2f)Resources.html){.nonexistent}

- [../Scrap](./MacPython(2f)Scrap.html){.nonexistent}

- [../Snd](./MacPython(2f)Snd.html){.nonexistent}

- [../Sound](./MacPython(2f)Sound.html){.nonexistent}

- [../TE](./MacPython(2f)TE.html){.nonexistent}

- [../TextEdit](./MacPython(2f)TextEdit.html)

- [../WASTEconst](./MacPython(2f)WASTEconst.html){.nonexistent}

- [../Win](./MacPython(2f)Win.html){.nonexistent}

- [../Windows](./MacPython(2f)Windows.html){.nonexistent}
:::
