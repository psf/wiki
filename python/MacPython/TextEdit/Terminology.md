# MacPython/TextEdit/Terminology

:::: {#content dir="ltr" lang="en"}
*([TextEdit](./TextEdit.html){.nonexistent}.app terminology, generated from /Applications/TextEdit.app)*

::: {}
  -------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Suites**     [Standard Suite](./MacPython(2f)TextEdit(2f)Terminology.html#suite_Standard_Suite) [Text Suite](./MacPython(2f)TextEdit(2f)Terminology.html#suite_Text_Suite)
  **Commands**   [close](./MacPython(2f)TextEdit(2f)Terminology.html#command_close) [count](./MacPython(2f)TextEdit(2f)Terminology.html#command_count) [delete](./MacPython(2f)TextEdit(2f)Terminology.html#command_delete) [duplicate](./MacPython(2f)TextEdit(2f)Terminology.html#command_duplicate) [exists](./MacPython(2f)TextEdit(2f)Terminology.html#command_exists) [get](./MacPython(2f)TextEdit(2f)Terminology.html#command_get) [make](./MacPython(2f)TextEdit(2f)Terminology.html#command_make) [move](./MacPython(2f)TextEdit(2f)Terminology.html#command_move) [open](./MacPython(2f)TextEdit(2f)Terminology.html#command_open) [print\_](./MacPython(2f)TextEdit(2f)Terminology.html#command_print_) [quit](./MacPython(2f)TextEdit(2f)Terminology.html#command_quit) [save](./MacPython(2f)TextEdit(2f)Terminology.html#command_save) [set](./MacPython(2f)TextEdit(2f)Terminology.html#command_set)
  **Classes**    [application](./MacPython(2f)TextEdit(2f)Terminology.html#class_application) [attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment) [attribute_run](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run) [character](./MacPython(2f)TextEdit(2f)Terminology.html#class_character) [color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color) [document](./MacPython(2f)TextEdit(2f)Terminology.html#class_document) [item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item) [paragraph](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph) [text](./MacPython(2f)TextEdit(2f)Terminology.html#class_text) [window](./MacPython(2f)TextEdit(2f)Terminology.html#class_window) [word](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)
  -------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

## Standard Suite {#Standard_Suite}

Common classes and commands for most applications.

### Commands {#Commands}

- **reference.get()** \-- Get the data for an object.\

  - Result: *Anything* \-- the reply for the command

  **reference.save(\...)** \-- Save an object.\

  - \[**as**=*[UnicodeText](./UnicodeText.html){.nonexistent}*\] \-- The file type in which to save the data.\
    \[**in\_**=*Alias*\] \-- The file in which to save the object.\
    Result: *None*

  **reference.set(\...)** \-- Set an object\'s data.\

  - **to**=*Anything* \-- The new value.\
    Result: *None*

  **application.print\_(\...)** \-- Print an object.\

  - \[*Alias*\] \-- The file(s) or document(s) to be printed.\
    Result: *None*

  **reference.duplicate(\...)** \-- Copy object(s) and put the copies at a new location.\

  - **to**=*[InsertionLoc](./InsertionLoc.html){.nonexistent}* \-- The location for the new object(s).\
    \[**with_properties**=*AERecord*\] \-- Properties to be set in the new duplicated object(s).\
    Result: *None*

  **reference.exists()** \-- Verify if an object exists.\

  - Result: *Boolean* \-- the reply for the command

  **reference.delete()** \-- Delete an object.\

  - Result: *None*

  **application.make(\...)** \-- Make a new object.\

  - \[**with_properties**=*AERecord*\] \-- The initial values for properties of the object.\
    **new**=*Type* \-- The class of the new object.\
    \[**with_data**=*Anything*\] \-- The initial data for the object.\
    \[**at**=*[InsertionLoc](./InsertionLoc.html){.nonexistent}*\] \-- The location at which to insert the object.\
    Result: *[ObjectSpecifier](./ObjectSpecifier.html){.nonexistent}* \-- the reply for the command

  **application.open(\...)** \-- Open an object.\

  - \[*Alias*\] \-- The file(s) to be opened.\
    Result: *None*

  **reference.close(\...)** \-- Close an object.\

  - \[**saving**=*k.yes \| k.no \| k.ask*\] \-- Specifies whether changes should be saved before closing.\
    \[**saving_in**=*Alias*\] \-- The file in which to save the object.\
    Result: *None*

  **reference.count(\...)** \-- Return the number of elements of a particular class within an object.\

  - \[**each**=*Type*\] \-- The class of objects to be counted.\
    Result: *SInt32* \-- the reply for the command

  **reference.move(\...)** \-- Move object(s) to a new location.\

  - **to**=*[InsertionLoc](./InsertionLoc.html){.nonexistent}* \-- The new location for the object(s).\
    Result: *None*

  **reference.quit(\...)** \-- Quit an application.\

  - \[**saving**=*k.yes \| k.no \| k.ask*\] \-- Specifies whether changes should be saved before quitting.\
    Result: *None*

### Classes {#Classes}

- **document** \-- A [/TextEdit](./MacPython(2f)TextEdit(2f)Terminology(2f)TextEdit.html){.nonexistent} document.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **modified** (r/o) *Boolean* \-- Has the document been modified since the last save?\
      **path** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The document\'s path.\
      **name** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The document\'s name.\
      **text** *[k.text](./MacPython(2f)TextEdit(2f)Terminology.html#class_text)* \-- The text of the document.\

  **item** \-- A scriptable object.

  - Children:
    - *[character](./MacPython(2f)TextEdit(2f)Terminology.html#class_character)* *[paragraph](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph)* *[application](./MacPython(2f)TextEdit(2f)Terminology.html#class_application)* *[color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color)* *[document](./MacPython(2f)TextEdit(2f)Terminology.html#class_document)* *[attribute_run](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run)* *[window](./MacPython(2f)TextEdit(2f)Terminology.html#class_window)* *[word](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)* *[text](./MacPython(2f)TextEdit(2f)Terminology.html#class_text)*

    Properties:
    - **class\_** (r/o) *Type* \-- The class of the object.\
      **properties** *AERecord* \-- All of the object\'s properties.\

  **window** \-- A window.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **zoomed** *Boolean* \-- Whether the window is currently zoomed.\
      **miniaturized** *Boolean* \-- Whether the window is currently miniaturized.\
      **name** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The full title of the window.\
      **floating** (r/o) *Boolean* \-- Whether the window floats.\
      **modal** (r/o) *Boolean* \-- Whether the window is the application\'s current modal window.\
      **miniaturizable** (r/o) *Boolean* \-- Whether the window can be miniaturized.\
      **visible** *Boolean* \-- Whether the window is currently visible.\
      **closeable** (r/o) *Boolean* \-- Whether the window has a close box.\
      **resizable** (r/o) *Boolean* \-- Whether the window can be resized.\
      **zoomable** (r/o) *Boolean* \-- Whether the window can be zoomed.\
      **id** (r/o) *SInt32* \-- The unique identifier of the window.\
      **bounds** *QDRectangle* \-- The bounding rectangle of the window.\
      **titled** (r/o) *Boolean* \-- Whether the window has a title bar.\
      **index** *SInt32* \-- The index of the window in the back-to-front window ordering.\
      **document** (r/o) *[k.document](./MacPython(2f)TextEdit(2f)Terminology.html#class_document)* \-- The document whose contents are being displayed in the window.\

  **application** \-- [TextEdit](./TextEdit.html){.nonexistent}\'s top level scripting object.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **version** (r/o) *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The version of the application.\
      **frontmost** (r/o) *Boolean* \-- Is this the frontmost (active) application?\
      **name** (r/o) *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The name of the application.\

    Elements:
    - **[windows](./MacPython(2f)TextEdit(2f)Terminology.html#class_window)** \-- *name \| index \| relative \| range \| test \| id*\
      **[documents](./MacPython(2f)TextEdit(2f)Terminology.html#class_document)** \-- *name \| index \| relative \| range \| test*\

  **color** \-- A color.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

## Text Suite {#Text_Suite}

A set of basic classes for text processing.

### Classes {#Classes-1}

- **attachment** \-- Represents an inline text attachment. This class is used mainly for make commands.

  - Parent:
    - *[text](./MacPython(2f)TextEdit(2f)Terminology.html#class_text)*

    Properties:
    - **file_name** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The path to the file for the attachment\

  **text** \-- Rich (styled) text

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Children:
    - *[attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment)*

    Properties:
    - **size** *SInt32* \-- The size in points of the first character.\
      **font** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The name of the font of the first character.\
      **color** *[k.color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color)* \-- The color of the first character.\

    Elements:
    - **[characters](./MacPython(2f)TextEdit(2f)Terminology.html#class_character)** \-- *index \| relative \| range \| test*\
      **[attribute_runs](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run)** \-- *index \| relative \| range \| test*\
      **[attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment)** \-- *index \| relative \| range \| test*\
      **[words](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)** \-- *index \| relative \| range \| test*\
      **[paragraphs](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph)** \-- *index \| relative \| range \| test*\

  **attribute_run** \-- This subdivides the text into chunks that all have the same attributes.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **size** *SInt32* \-- The size in points of the first character.\
      **font** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The name of the font of the first character.\
      **color** *[k.color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color)* \-- The color of the first character.\

    Elements:
    - **[characters](./MacPython(2f)TextEdit(2f)Terminology.html#class_character)** \-- *index \| relative \| range \| test*\
      **[attribute_runs](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run)** \-- *index \| relative \| range \| test*\
      **[attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment)** \-- *index \| relative \| range \| test*\
      **[words](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)** \-- *index \| relative \| range \| test*\
      **[paragraphs](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph)** \-- *index \| relative \| range \| test*\

  **character** \-- This subdivides the text into characters.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **size** *SInt32* \-- The size in points of the first character.\
      **font** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The name of the font of the first character.\
      **color** *[k.color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color)* \-- The color of the first character.\

    Elements:
    - **[characters](./MacPython(2f)TextEdit(2f)Terminology.html#class_character)** \-- *index \| relative \| range \| test*\
      **[attribute_runs](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run)** \-- *index \| relative \| range \| test*\
      **[attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment)** \-- *index \| relative \| range \| test*\
      **[words](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)** \-- *index \| relative \| range \| test*\
      **[paragraphs](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph)** \-- *index \| relative \| range \| test*\

  **word** \-- This subdivides the text into words.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **size** *SInt32* \-- The size in points of the first character.\
      **font** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The name of the font of the first character.\
      **color** *[k.color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color)* \-- The color of the first character.\

    Elements:
    - **[characters](./MacPython(2f)TextEdit(2f)Terminology.html#class_character)** \-- *index \| relative \| range \| test*\
      **[attribute_runs](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run)** \-- *index \| relative \| range \| test*\
      **[attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment)** \-- *index \| relative \| range \| test*\
      **[words](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)** \-- *index \| relative \| range \| test*\
      **[paragraphs](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph)** \-- *index \| relative \| range \| test*\

  **paragraph** \-- This subdivides the text into paragraphs.

  - Parent:
    - *[item](./MacPython(2f)TextEdit(2f)Terminology.html#class_item)*

    Properties:
    - **size** *SInt32* \-- The size in points of the first character.\
      **font** *[UnicodeText](./UnicodeText.html){.nonexistent}* \-- The name of the font of the first character.\
      **color** *[k.color](./MacPython(2f)TextEdit(2f)Terminology.html#class_color)* \-- The color of the first character.\

    Elements:
    - **[characters](./MacPython(2f)TextEdit(2f)Terminology.html#class_character)** \-- *index \| relative \| range \| test*\
      **[attribute_runs](./MacPython(2f)TextEdit(2f)Terminology.html#class_attribute_run)** \-- *index \| relative \| range \| test*\
      **[attachment](./MacPython(2f)TextEdit(2f)Terminology.html#class_attachment)** \-- *index \| relative \| range \| test*\
      **[words](./MacPython(2f)TextEdit(2f)Terminology.html#class_word)** \-- *index \| relative \| range \| test*\
      **[paragraphs](./MacPython(2f)TextEdit(2f)Terminology.html#class_paragraph)** \-- *index \| relative \| range \| test*\
::::
