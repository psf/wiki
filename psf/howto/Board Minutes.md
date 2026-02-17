# howto/Board Minutes

:::::::::::::::::::::::: {#content dir="ltr" lang="en"}
# How To Prepare the Board Meeting Minutes

::: {#contents .contents .topic}
Contents

- [1   Preparation](#preparation){#id3 .reference .internal}
- [2   Update Last Month\'s Minutes](#update-last-month-s-minutes){#id4 .reference .internal}
- [3   Update the List of Meeting Minutes](#update-the-list-of-meeting-minutes){#id5 .reference .internal}
- [4   Update This Month\'s Minutes](#update-this-month-s-minutes){#id6 .reference .internal}
  - [4.1   Title](#title){#id7 .reference .internal}
  - [4.2   Intro Paragraph](#intro-paragraph){#id8 .reference .internal}
  - [4.3   Attendance](#attendance){#id9 .reference .internal}
  - [4.4   Minutes of Past Meetings](#minutes-of-past-meetings){#id10 .reference .internal}
  - [4.5   Votes Taken Between Meetings](#votes-taken-between-meetings){#id11 .reference .internal}
  - [4.6   Status of Past Action Items](#status-of-past-action-items){#id12 .reference .internal}
    - [4.6.1   Carried Forward](#carried-forward){#id13 .reference .internal}
    - [4.6.2   New on \<D Month YYYY\>](#new-on-d-month-yyyy){#id14 .reference .internal}
    - [4.6.3   New Between Meetings](#new-between-meetings){#id15 .reference .internal}
    - [4.6.4   Update the Action Items](#update-the-action-items){#id16 .reference .internal}
  - [4.7   Add Sections for New Business](#add-sections-for-new-business){#id17 .reference .internal}
- [5   Update Action Items Wiki Page](#update-action-items-wiki-page){#id18 .reference .internal}
  - [5.1   Add status updates to existing action items](#add-status-updates-to-existing-action-items){#id19 .reference .internal}
  - [5.2   Add new action items](#add-new-action-items){#id20 .reference .internal}
- [6   Inform the Secretary and the Board](#inform-the-secretary-and-the-board){#id21 .reference .internal}
- [7   Links](#links){#id22 .reference .internal}
:::

::: {#preparation .section}
### [1   Preparation](#id3){.toc-backref}

You will need:

1.  A copy of last month\'s minutes.

    In the [website repository](#website-repository){.reference .internal}: build/data/psf/records/board/minutes/YYYY-MM-DD/content.ht.

    E.g. copy build/data/psf/records/board/minutes/2008-11-10/content.ht to build/data/psf/records/board/minutes/2008-12-08/content.ht

2.  The [Board agenda wiki page](http://wiki.python.org/psf/BoardAgenda){.http .reference .external} **for this month\'s meeting** [\[1\]](#wiki-history){#id1 .footnote-reference}.

3.  The [action items wiki page](http://wiki.python.org/psf/Action_Items){.http .reference .external} **as of this month\'s meeting** [\[1\]](#wiki-history){#id2 .footnote-reference}.

+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[1\] | *([1](#id1){.fn-backref}, [2](#id2){.fn-backref})*                                                                                                    |
|       |                                                                                                                                                       |
|       | The wiki page may have changed since the meeting. You should use the version of the wiki page *as it was\** as of the beginning of the Board meeting. |
|       |                                                                                                                                                       |
|       | 1.  Use the \"Info\" link near the top of the page to see the revision history of the wiki page.                                                      |
|       | 2.  In the \"Date\" column, find the date closest to (but before) the beginning of the Board meeting.                                                 |
|       | 3.  In that row, click the \"View\" link in the \"Action\" (last) column.                                                                             |
+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

::: {#update-last-month-s-minutes .section}
### [2   Update Last Month\'s Minutes](#id4){.toc-backref}

If the minutes of last month\'s meeting were approved, update last month\'s minutes:

1.  Remove \"(Draft)\" from the first (\"Title:\") line.
2.  Remove \"\| Draft\" from the title block.
:::

::: {#update-the-list-of-meeting-minutes .section}
### [3   Update the List of Meeting Minutes](#id5){.toc-backref}

The list of meeting minutes (table of contents) is at build/data/psf/records/board/minutes/content.ht in the [website repository](#website-repository){.reference .internal}.

1.  Add a header for the new year in January.

2.  At the top of the list, add a link to the now-approved last month\'s minutes, e.g.:

        * `November 10, 2008 <2008-11-10>`_
:::

:::::::::::::: {#update-this-month-s-minutes .section}
### [4   Update This Month\'s Minutes](#id6){.toc-backref}

::: {#title .section}
#### [4.1   Title](#id7){.toc-backref}

1.  Update the date in the page title (first line). Be sure the title line says \"(Draft)\" at the end.
2.  Update the date in in the title block (\"\|\" border on the left). Be sure the title block has \"\| Draft\" under the date.
:::

::: {#intro-paragraph .section}
#### [4.2   Intro Paragraph](#id8){.toc-backref}

1.  Update the date & time (in the UTC/GMT time zone) in the intro paragraph under the title block. Use the [World Clock](http://www.timeanddate.com/worldclock/){.http .reference .external} to get the current time UTC time.
2.  Verify who presided and who prepared the minutes, and correct if necessary.
:::

::: {#attendance .section}
#### [4.3   Attendance](#id9){.toc-backref}

1.  Update the list of attendees, both Directors and \"Also in attendance\". Directors names should be listed in alphabetical order by family name.

    If someone came late, after a vote, note the time they arrived (e.g. \"(arrived at 17:20)\"). Also note if anyone left early. Always use the UTC timezone.
:::

::: {#minutes-of-past-meetings .section}
#### [4.4   Minutes of Past Meetings](#id10){.toc-backref}

Update the \"Minutes of Past Meetings\" section.

1.  Update the date of last month\'s meeting, and the vote.
2.  If there were any special meetings, note them and their votes also (e.g. annual Members\' Meeting and first meeting of the new Board of Directors are both held at PyCon).
3.  Remove any unnecessary approvals.
:::

::: {#votes-taken-between-meetings .section}
#### [4.5   Votes Taken Between Meetings](#id11){.toc-backref}

Update the \"Votes Taken Between Meetings\" section.

1.  Update the date of last month\'s meeting.

2.  If there were some votes on resolutions, write the following:

        The actions below were taken since the <D Month YYYY> meeting.

3.  If there were no resolutions, write the following:

        No votes were taken since the <D Month YYYY> Board meeting.

4.  Add any resolutions voted upon between minuted meetings. Each action should be in its own subsection. Example:

        Title of Resolution
        -------------------

            **RESOLVED**, that ...

        Approved by unanimous email vote, <D Month YYYY>.

    If anyone abstained from voting, note that too: \"(X abstentions)\".
:::

::::::: {#status-of-past-action-items .section}
#### [4.6   Status of Past Action Items](#id12){.toc-backref}

Update the \"Status of Past Action Items\" section.

::: {#carried-forward .section}
##### [4.6.1   Carried Forward](#id13){.toc-backref}

Update the \"Carried Forward\" subsection:

1.  In the first paragraph, update the date of the last month\'s meeting. Verify the section number of last month\'s \"Status of Past Action Items\" section.

2.  Remove any items marked `**done**` or `**dropped**` in the last month\'s minutes. (Scan for \"`Status: **done**`\" and \"`Status: **dropped**`\" in the copied minutes, and remove any such items.)

3.  Remove all old notes from action items (text below the action item and above the \"Status\" line).

4.  In last month\'s \"New \...\" subsections: add the following as a prefix to each item:

    > Originally from DD Month YYYY,

5.  Move all items from the \"New \...\" subsections into the \"Carried Forward\" subsection, at the bottom.

6.  Renumber the list from 1 (some items have been removed, others added), adjusting indentation as necessary.
:::

::: {#new-on-d-month-yyyy .section}
##### [4.6.2   New on \<D Month YYYY\>](#id14){.toc-backref}

1.  Update the date of the last month\'s meeting in the title and the first paragraph.

2.  Collect all the new action items from last month\'s minutes, and put them into a numbered list in the \"New on \<date of last meeting\>\" section:

    1.  Scan the \"new business\" sections (all the sections after \"Status of Past Action Items\") in last month\'s minutes, and locate action items.

    2.  For each new action item, after the item number in brackets, add the word \"Section\", the section number, a comma (\",\"), the section title, and a colon (\":\").

        For example:

            [0] :action:`J. Doe ...`

        becomes:

            [0] Section 5, Example Title: :action:`J. Doe ...`

        - Look up section numbers on the web: see [list of PSF Board meeting minutes](#list-of-psf-board-meeting-minutes){.reference .internal}. The table of contents of the web page of last month\'s minutes shows the section numbers.
        - If there was more than one action item in a section (they should be numbered), join the section number and the item number with a \".\" (e.g. \"5.1\", \"5.2\", etc.).
        - Note the format of action items: item number in square brackets (\"\[\]\"), one space after the brackets, \":action:\", no space following, and the action item text in backquotes (\"\`\").

3.  Move the edited action item into a numbered list in the \"New on \...\" section. Numbered lists look like this:

        1. item one...

        2. item two...

4.  Delete the unused portions of the copied text of last month\'s minutes as you go.
:::

::: {#new-between-meetings .section}
##### [4.6.3   New Between Meetings](#id15){.toc-backref}

Look at the [action items wiki page](http://wiki.python.org/psf/Action_Items){.http .reference .external}. Any action items added since the last Board meeting should be recorded in the minutes.
:::

::: {#update-the-action-items .section}
##### [4.6.4   Update the Action Items](#id16){.toc-backref}

Referring to the [action items wiki page](http://wiki.python.org/psf/Action_Items){.http .reference .external}, update the action items:

1.  For all action items done or dropped, add brief details (link, date, etc., if applicable). Remove the action item markup:

    > :action:\` & \`

    Add one of the following status lines:

        Status: **done**.

        Status: **dropped**.

    Bold-face markup (\"\*\*\") is only used for the status of finalized items (items that will be removed next month).

2.  For other action items, add brief details and add (or adjust) the status lines as follows:

        Status: pending.

        Status: active.

    Do not use bold-face markup (\"\*\*\") for the status of non-final items.

**Note:** All action items in the \"Status of Past Action Items\" section **must** have status lines.

While summarizing new business from the meeting transcript (IRC log), record any updates to existing action items as above, and on the [action items wiki page](http://wiki.python.org/psf/Action_Items){.http .reference .external}. If there is more than a brief status update note, create a new section (as in [Add Sections for New Business](#add-sections-for-new-business){.reference .internal} below).
:::
:::::::

::: {#add-sections-for-new-business .section}
#### [4.7   Add Sections for New Business](#id17){.toc-backref}

Referring to the meeting agenda and transcript (IRC log), add a section for each topic discussed.

1.  Scan the log for new business. The log should roughly correspond to the agenda, but will diverge.

2.  Create a new section title for each item of business or discussion:

        Section Title
        =============

    For the title text, check the agenda. Title text should be brief and to the point.

3.  Summarize the discussion.

    - Use direct quotes where appropriate. For brief quotes:

      > 10. Doe: \"What he said.\"

      For extended passages, use block quotes:

      > 10. Doe:
      >
      >     > vs block quotes,

      When editing to clarify, use square brackets (\"\[\" & \"\]\") around text that was not actually written by the person quoted.

      When omitting segments, use ellipses (\"\...\") to indicate omitted text.

> - Paraphrase what was said: \"The Board agreed that \...\", \"J. Doe noted that \...\", \"J. Doe reported \...\", \"The Board decided \...\", etc.
> - Omit sensitive information and disagreements.
> - Summarize the consensus.

4.  Copy & paste resolutions from the log.

    Correct misspellings, grammar, and sentence structure, etc.

    Format:

            **RESOLVED**, that ...

        Approved, 8-0-0.

5.  Usually include an explicit action item. Sometimes the action item is left implicit in the discussion.

    Note action items as follows:

        [] :action:`J. Doe will do XYZ.`

    Use the initial of the given name, and the full family name.

    If there are multiple action items in a section, number them in a list:

        1. :action:`J. Doe will do XYZ.`

        2. :action:`A. Square will do ABC.`

    (List items need not be adjacent. They may be separated by explanatory paragraphs etc.)
:::
::::::::::::::

::::: {#update-action-items-wiki-page .section}
### [5   Update Action Items Wiki Page](#id18){.toc-backref}

Edit the [Action Items wiki page](http://wiki.python.org/psf/Action_Items){.http .reference .external}.

Scan the minutes of this month\'s Board meeting for new action items and updates to existing action items.

::: {#add-status-updates-to-existing-action-items .section}
#### [5.1   Add status updates to existing action items](#id19){.toc-backref}

1.  Add brief status text to the \"Description\" column.
2.  Update the \"Status\" column if applicable.
3.  Update the \"On\" date.
:::

::: {#add-new-action-items .section}
#### [5.2   Add new action items](#id20){.toc-backref}

Add new action items to the \"Outstanding Items\" section of the wiki page.

1.  Duplicate the text of the last row of the table. Select the last row, copy the text, and paste so that there are two copies of that row. The second-last row will be the new action item.

2.  Transfer the action item number from the wiki page back to the minutes.

3.  Increment the ID on the last row (the placeholder for the \"Next\" action item).

4.  In the \"Who\" column (column 2), note the initials of the person or people responsible for the action item.

5.  In the \"Since\" column (column 3):

    1.  Note the date of the meeting in YYYY-MM-DD format.

    2.  Also note the section number from the minutes, prefixed with the \"§\" symbol. (The first new business section will be section 5.)

        **Note:** Section numbers don\'t always increase. Sometimes a section doesn\'t have any action items. Sometimes there are two or more action items within one section. In that case, each item should be numbered and combined with the section number, like \"§11.1\" (meaning \"section 11, item 1\"), etc.

6.  In the \"Description\" column, remove the old instructional text (\"Next \...\"). Add the text of the action item (not including the markup: \"`` :action:` ``\" & \"`` ` ``\").

7.  In the \"Status\" column, type \"Pending\".

8.  In the \"On\" column, add the date of the meeting (YYYY-MM-DD).
:::
:::::

::: {#inform-the-secretary-and-the-board .section}
### [6   Inform the Secretary and the Board](#id21){.toc-backref}

1.  Send a copy of the completed minutes to the PSF Secretary for approval (markup fixes, content, etc.).
2.  Send a copy of the minutes (as edited and approved by the Secretary) to the Board mailing list ([psf@python.org](mailto:psf@python.org){.mailto .reference .external}).
:::

::: {#links .section}
### [7   Links](#id22){.toc-backref}

- [List of PSF Board meeting minutes]{#list-of-psf-board-meeting-minutes .target} (with links): [http://www.python.org/psf/records/board/minutes/](http://www.python.org/psf/records/board/minutes/){.http .reference .external}

- [website repository]{#website-repository .target}: [https://svn.python.org/www/trunk/beta.python.org/](https://svn.python.org/www/trunk/beta.python.org/){.https .reference .external}

  Board meeting minutes: [https://svn.python.org/www/trunk/beta.python.org/build/data/psf/records/board/minutes/](https://svn.python.org/www/trunk/beta.python.org/build/data/psf/records/board/minutes/){.https .reference .external}

  Members\' meeting minutes: [https://svn.python.org/www/trunk/beta.python.org/build/data/psf/records/members/](https://svn.python.org/www/trunk/beta.python.org/build/data/psf/records/members/){.https .reference .external}

  See [Python.org Maintenance and Administration](http://python.org/dev/pydotorg/){.http .reference .external} and [Python.org Website Maintenance](http://python.org/dev/pydotorg/website/){.http .reference .external}.
:::
::::::::::::::::::::::::
