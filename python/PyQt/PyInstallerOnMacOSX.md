# PyQt/PyInstallerOnMacOSX

::: {#content dir="ltr" lang="en"}
# Using PyInstaller with PyQt on Mac OS-X {#Using_PyInstaller_with_PyQt_on_Mac_OS-X}

PyInstaller has only preliminary support for Mac OS-X and currently (Feb. 2010) needs some workarounds and modifications to work properly with PyQt. Therefore this short how-to will show the steps to make the QtWebKit based \'Minibrowser\' sample app from [here](http://eric-ide.python-projects.org/tutorials/MiniBrowser/index.html){.http} into an OS-X application bundle.

## Prerequisites {#Prerequisites}

- Recent versions of Qt and PyQt need to be installed.

I installed PyQt and Eric4 according to [this](http://works13.com/blog/mac/installing-eric4-on-mac-os-x-leopard.htm){.http} guide. The following versions were used: OS-X 10.6.2, Python 2.6.1, Qt 4.6.2., PyQt 4.7, sip 4.10, QScintilla 2.4.2. Eric4 is obviously optional for the purpose of this how-to.

## Installing and patching PyInstaller {#Installing_and_patching_PyInstaller}

- Create a working folder, for example:
  - /Users/username/pywork
  - Open a Terminal window and
    -       $ mkdir pywork
                $ cd pywork
- Download the current pyinstaller source:
  -       $ svn co http://svn.pyinstaller.org/trunk pyinstaller

    \> Checked out revision 771
- Modify pyinstaller/source/linux/main.c by commenting out the following \'wait()\' section at the end of the file:
  -         wait(&rc);
                rc = WEXITSTATUS(rc);

                VS("Back to parent...\n");
                if (strcmp(workpath, homepath) != 0)
                    clear(workpath);

    This deals with the problem \"Icon and Menu is missing from PyQt apps, when running an OS-X App Bundle\". The patch is described and can be downloaded [here](http://www.pyinstaller.org/ticket/156){.http}.

           $ cd pyinstaller/source/linux
           $ patch --verbose main.c main.patch
- Setup pyinstaller:
  -       $ cd pyinstaller/source/linux
              $ python ./Make.py
              $ make
              $ cd ../..
              $ python Configure.py
- Patch Build.py, otherwise we get a \'Python image not found error\'
  - Browse to Ticket #152 [\"pyinstaller onefile fails to bundle Python framework shared lib on osx\"](http://www.pyinstaller.org/ticket/152){.http}

  - Download [pyinstaller.patch](http://www.pyinstaller.org/raw-attachment/ticket/152/pyinstaller.patch){.http} and copy it into pywork/pyinstaller

    -     $ patch --verbose Build.py pyinstaller.patch

## Making the Application into an App Bundle {#Making_the_Application_into_an_App_Bundle}

- Download a the Minibrowser sample project:
  - From [here](http://eric-ide.python-projects.org/tutorials/MiniBrowser/resources/minibrowser.zip){.http} into the pywork directory and unzip

- In the main loop add window.raise\_():
  - this deals with the PyQt specific problem in OS-X, that an application window is not automatically brought to the front on launch as expected. [link](http://www.pyinstaller.org/ticket/158){.http}

  - for example in pywork/minibrowser/minibrowser.py modify as follows

  <!-- -->

  - :::: {.highlight .python}
    ::: {.codearea dir="ltr" lang="en"}
    ``` {#CA-1c02cdea9a3c8e5b5c0d056cb338fe88c2777dc1 dir="ltr" lang="en"}
       1     ui = MainWindow()
       2     ui.show()
       3     ui.raise_()
    ```
    :::
    ::::

- Change to the pywork directory & make the spec file:

  -    $ cd ..
           $ python pyinstaller/Makespec.py --out=MinibrowserTmp minibrowser/minibrowser.py

- Add the following to the bottom of your spec file:
  -     import sys 
            if sys.platform.startswith("darwin"): 
                app = BUNDLE(exe, 
                          appname='Minibrowser', 
                          version='1.0')

- Build the Application Bundle:
  -    $ python pyinstaller/Build.py MinibrowserTmp/minibrowser.spec

- Fix the Bundle:
  - Change the key in pywork/Minibrowser.app/Contents/Info.plist to
    -          <key>LSBackgroundOnly</key>
                   <false/>

- To deal with the issue \'OS-X App Bundle is missing most files\' described [here](http://www.pyinstaller.org/ticket/155){.http}

  - Copy the missing app files into pywork/Minibrowser.app/Contents/MacOS:
    -       $ cp -rv MinibrowserTmp/dist/minibrowser/* Minibrowser.app/Contents/MacOS

- To prevent the Error: \'qt_menu.nib could not be loaded\' described [here](http://www.pyinstaller.org/ticket/157){.http}

  - Into the pywork/Minibrowser.app/Contents/Resources folder copy qt_menu.nib from /Library/Frameworks/QtGui.framework/Versions/4/Resources/qt_menu.nib
    -       $ cp -rv /Library/Frameworks/QtGui.framework/Versions/4/Resources/qt_menu.nib Minibrowser.app/Contents/Resources

## Test and Compress the App {#Test_and_Compress_the_App}

- You should now be able to run the application bundle just like any native OS-X application by double clicking on it.

- Minibrowser usage: Enter a url and *click* the Navigate button

- Package the app in a compressed dmg for distribution, this reduces the size to about one third.

Check the linked issue tickets and PyInstaller [tracker](http://www.pyinstaller.org/report/1){.http} and release notes, as these issues will be resolved sometime and the steps with workarounds will hopefully not be needed any more.
:::
