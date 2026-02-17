# InitialTestingPlan

::: {#content dir="ltr" lang="en"}
Initial Testing Plan for Plone

To come up with an initial testing plan, different approaches have been explored.

The first idea is to try to make Plone choke on some weird input in the forms or even by configuring Plone wrong on purpose.

It is also good to try to break stuff by simply removing it altogether to see how Plone reacts. This actually reveals what it is that the removed component is important for, and guides the writing of functional tests for it. As a side effect, a lot of thinking is provoked about how things are currently working, possibly revealing annoying hard-coded behaviour and pointing into directions for making the application more reliable or at least fail gracefully.

Unit tests are not sufficient in some use cases, and it sometimes even happens that we have to rewrite some unit tests as functional tests in order to have better coverage in face of Plone site customisations. In the best case these changes could always be fed back to customisation policies, but we have to test for the worst case, where in-depth changes for example to the permissions are made, and we need to ensure that there are functional tests that make problems directly evident.

Basic Content types tests

- These tests should best be placed in ATContentTypes, but to get started we can make adding and editing them part of our functional test suite:
- Document
- Event
- File
- Folder
- Image
- Folder
- Large Plone Folder
- Link
- News Item
- Topic Use cases:
  - Member adds one of the content types Member adds Favorite

  There are a few parts in Plone that treat specific content types in a special way, and these places should become evident in the functional tests. For example Links and Images, additional information is shown in plone_templates/folder_listing.pt We can take the test a step further and study what happens when you remove a content type altogether.

Portal Catalog

- The portal catalog contains indexes and metadata which would merit some special attention. Questions to address: What happens when the catalog is empty? What happens when you delete content in the ZMI find it through the catalog?

[MailHost](./MailHost.html){.nonexistent}

- The [MailHost](./MailHost.html){.nonexistent} is not a standard tool in the Plone sense, so it behaves just a bit differently. In addition, the [MailHost](./MailHost.html){.nonexistent} is also a place where we are relying on a external service, so we have to take some extra care. One use case would be that there is a temporary problem with sending mail,

  and the administrator has to have a way to switch off the [MailHost](./MailHost.html){.nonexistent}. He could remove it altogether, and once the problems are resolved, the [MailHost](./MailHost.html){.nonexistent} is added back in again. This opens a feature request allowing to being able to desactivate a [MailHost](./MailHost.html){.nonexistent} instead of having to delete it. Some questions we should address here:

  \- What happens when we remove the [MailHost](./MailHost.html){.nonexistent} altogether?

  - \- Should related buttons and interfaces still be active?
    - \- Can users still access the interface for sending mail? - Is prefs_mailhost_form still showing the configuration?

    \- Create functional tests showing what breaks in Plone after removing the
    - [MailHost](./MailHost.html){.nonexistent}, and then put it back in to see that the tests pass

  \- What happens when the Mailhost is not correctly configured?

  \- What happens when the [MailHost](./MailHost.html){.nonexistent} can not send Mail? - Is there something that could have broken while moving from [MailHost](./MailHost.html){.nonexistent}

  - to [SecureMailHost](./SecureMailHost.html){.nonexistent}?

Permissions

- Showing what effect the permission settings have is a great use of acceptance tests. It is nowhere documented what permissions are actually doing, and by coding this \"knowledge\" into functional tests, the practical meaning of permissions becomes evident. We should start with the permissions proper to Plone, and work our way down to permissions in CMF and Zope that are still relevant for Plone. As an example, we take the \"Manage portal\" permission of Plone. The following are all uses of this permission in Plone under the name \"Manage portal\". It does not take into account uses of the permission under the name

  CMFCorePermissions.[ManagePortal](./ManagePortal.html){.nonexistent}

  -\> Allows to see members that are not \"listed\" in the

  - portal_membership.searchForMembers()

  -\> Allows to \"Remove This Reply\" in plone_content/discussionitem_view.pt -\> Allows to search \"Role(s)\" in member_search_form.pt -\> Allows \"Remove This Discussion\" in plone_templates/viewThreadsAtBottom.pt \# General Zope permissions View = Permissions.view

  -\> Mostly important in the workflow. See there for further information. -\> Plays a role in the apis and on templates.

  [AccessContentsInformation](./AccessContentsInformation.html){.nonexistent} = Permissions.access_contents_information -\> Mostly important in the workflow. See there for further information.

  [DeleteObjects](./DeleteObjects.html){.nonexistent} = Permissions.delete_objects

  -\> Make sure deleting a content is only possible when you have the permission to delete the content itself, but also the permission to delete in the folder in general.

  [ViewManagementScreens](./ViewManagementScreens.html){.nonexistent} = Permissions.view_management_screens [ManageProperties](./ManageProperties.html){.nonexistent} = Permissions.manage_properties FTPAccess = Permissions.ftp_access \# CMF Base Permissions

  [ListFolderContents](./ListFolderContents.html){.nonexistent} = \'List folder contents\' setDefaultRoles( [ListFolderContents](./ListFolderContents.html){.nonexistent}, ( \'Manager\', \'Owner\' ) ) -\> Mostly important in the workflow. See there for further information.

  [ListUndoableChanges](./ListUndoableChanges.html){.nonexistent} = \'List undoable changes\' setDefaultRoles( [ListUndoableChanges](./ListUndoableChanges.html){.nonexistent}, (\'Manager\',) ) \# + Member

  [AccessInactivePortalContent](./AccessInactivePortalContent.html){.nonexistent} = \'Access inactive portal content\' setDefaultRoles([AccessInactivePortalContent](./AccessInactivePortalContent.html){.nonexistent}, (\'Manager\',))

  [ModifyCookieCrumblers](./ModifyCookieCrumblers.html){.nonexistent} = \'Modify Cookie Crumblers\' setDefaultRoles([ModifyCookieCrumblers](./ModifyCookieCrumblers.html){.nonexistent}, (\'Manager\',))

  [ReplyToItem](./ReplyToItem.html){.nonexistent} = \'Reply to item\' setDefaultRoles([ReplyToItem](./ReplyToItem.html){.nonexistent}, (\'Manager\',)) \# + Member

  [ManagePortal](./ManagePortal.html){.nonexistent} = \'Manage portal\' setDefaultRoles([ManagePortal](./ManagePortal.html){.nonexistent}, (\'Manager\',))

  [ModifyPortalContent](./ModifyPortalContent.html){.nonexistent} = \'Modify portal content\' setDefaultRoles([ModifyPortalContent](./ModifyPortalContent.html){.nonexistent}, (\'Manager\',))

  [ManageProperties](./ManageProperties.html){.nonexistent} = \'Manage properties\' setDefaultRoles([ManageProperties](./ManageProperties.html){.nonexistent}, (\'Owner\',\'Manager\',))

  [ListPortalMembers](./ListPortalMembers.html){.nonexistent} = \'List portal members\' setDefaultRoles( [ListPortalMembers](./ListPortalMembers.html){.nonexistent}, (\'Manager\',) ) \# + Member

  [AddPortalFolders](./AddPortalFolders.html){.nonexistent} = \'Add portal folders\' setDefaultRoles([AddPortalFolders](./AddPortalFolders.html){.nonexistent}, (\'Owner\',\'Manager\')) \# + Member

  [AddPortalContent](./AddPortalContent.html){.nonexistent} = \'Add portal content\' setDefaultRoles([AddPortalContent](./AddPortalContent.html){.nonexistent}, (\'Owner\',\'Manager\',)) \# + Member

  [AddPortalMember](./AddPortalMember.html){.nonexistent} = \'Add portal member\' setDefaultRoles([AddPortalMember](./AddPortalMember.html){.nonexistent}, (\'Anonymous\', \'Manager\',))

  [SetOwnPassword](./SetOwnPassword.html){.nonexistent} = \'Set own password\' setDefaultRoles([SetOwnPassword](./SetOwnPassword.html){.nonexistent}, (\'Manager\',)) \# + Member

  [SetOwnProperties](./SetOwnProperties.html){.nonexistent} = \'Set own properties\' setDefaultRoles([SetOwnProperties](./SetOwnProperties.html){.nonexistent}, (\'Manager\',)) \# + Member

  [MailForgottenPassword](./MailForgottenPassword.html){.nonexistent} = \'Mail forgotten password\' setDefaultRoles([MailForgottenPassword](./MailForgottenPassword.html){.nonexistent}, (\'Anonymous\', \'Manager\',)) \# Workflow Permissions

  [RequestReview](./RequestReview.html){.nonexistent} = \'Request review\' setDefaultRoles([RequestReview](./RequestReview.html){.nonexistent}, (\'Owner\', \'Manager\',))

  [ReviewPortalContent](./ReviewPortalContent.html){.nonexistent} = \'Review portal content\' setDefaultRoles([ReviewPortalContent](./ReviewPortalContent.html){.nonexistent}, (\'Manager\',)) \# + Reviewer

  [AccessFuturePortalContent](./AccessFuturePortalContent.html){.nonexistent} = \'Access future portal content\' setDefaultRoles([AccessFuturePortalContent](./AccessFuturePortalContent.html){.nonexistent}, (\'Manager\',)) \# + Reviewer

Plone Site Permission encapsulation

- There should be a way to encapsulate a Plone site so that it does not use acquisition at all. This would make Plone immune to Permission changes outside of its scope. This does not cover the case where permissions are actually added to Plone. It also does not cover the case where a product changes permissions during installation or uninstallation. This is also a way to clearly state in one place what the permissions in Plone should be instead of having to take into account acquisition. A fun way to test this is to look for what switching off acquisition breaks, writing tests for that, and then fixing the permissions in Plone until the resulting permissions are the same as they would be by acquisition.

Workflow

- We need basic tests for workflows. This work has already started in the

  [PloneSelenium](./PloneSelenium.html){.nonexistent} product. The idea is to add folders in the different workflow states and to verify whether users with certains roles should have access. The access to a folder can mean different things. The view changes in depending on the \"View\", \"Access Contents\", \"Modify portal contents\" and \"List folder contents\" permissions and possibly some others as well. This is all very important to have documented by some functional tests. The next part is the plone_workflow, where we have to create a content and make sure that actions and views on the content are respecting permissions. Workflow transitions in plone_workflow

  - pending Waiting for reviewer
    - hide (Member makes content private) publish (Reviewer publishes content)
      - reject (Reviewer rejects submission) retract (Member retracts submission)

    private Visible and editable only by owner
    - show (Member makes content visible)

    published Public
    - reject (Reviewer rejects submission) retract (Member retracts submission)
  - visible Visible but not published
    - hide (Member makes content private) publish (Reviewer publishes content) submit (Member requests publishing)

  Workflow transitions in folder_workflow

  - private Visible and editable only by owner
    - publish (Reviewer publishes content) show (Member makes content visible)

    published Public
    - hide (Member makes content private) retract (Member retracts submission)
  - visible Visible but not published
    - hide (Member makes content private) publish (Reviewer publishes content)

  Workflow Security on plone_workflow

  - View private document View submitted document View visible document View published document

  Workflow Security on folder_workflow

  - View private folder View published folder View visible folder

[RegistrationTool](./RegistrationTool.html){.nonexistent}

- Anonymous joins

  -\> Look at CMFMember ftests

[MembershipTool](./MembershipTool.html){.nonexistent}

- Member logs in Member forgot his password Member logs out Member wants Plone to remember his name Member does not want Plone to remember his name

[MemberDataTool](./MemberDataTool.html){.nonexistent}

- Member edits Preferences Anonymous searches Members

[SkinsTool](./SkinsTool.html){.nonexistent}

- Anonymous access Change default skin Change REQUEST variable name Allow arbitrary skins to be selected Disallow arbitrary skins to be selected Activate Skin Cookie persistence Desactivate Skin Cookie persistence

[CatalogTool](./CatalogTool.html){.nonexistent}

- Anonymous searches

Configlets

- Admin accesses configlet

[QuickInstallerTool](./QuickInstallerTool.html){.nonexistent}

- Admin installs a product Admin uninstalls a product
:::
