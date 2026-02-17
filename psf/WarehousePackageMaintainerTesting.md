# WarehousePackageMaintainerTesting

:::: {#content dir="ltr" lang="en"}
# Help us test PyPI\'s authentication improvements! {#Help_us_test_PyPI.27s_authentication_improvements.21}

Warehouse is the code behind the Python Package Repository ([PyPI](https://pypi.org/){.https}). We are seeking maintainers of Projects on PyPI to test our new security improvements while they\'re in beta and send us bug reports. Please help us shake the bugs out!

Feedback on user experience, accessibility, and overall ease of use are welcome; we want to support your workflows for account management and package maintainership. Go to [your account settings](https://pypi.org/manage/account/#two-factor){.https} and try it out!

::: table-of-contents
Contents

1.  [Help us test PyPI\'s authentication improvements!](#Help_us_test_PyPI.27s_authentication_improvements.21)
    1.  [Guidelines for Particpation](#Guidelines_for_Particpation)
    2.  [Changes we\'re making](#Changes_we.27re_making)
        1.  [Two-factor authentication](#Two-factor_authentication)
        2.  [Upload API tokens](#Upload_API_tokens)
        3.  [Audit log](#Audit_log)
    3.  [Things to test](#Things_to_test)
        1.  [Caution (before you test)](#Caution_.28before_you_test.29)
        2.  [Workflows](#Workflows)
        3.  [Testers we need](#Testers_we_need)
        4.  [Setting up a TOTP application](#Setting_up_a_TOTP_application)
        5.  [Setting up a U2F security key](#Setting_up_a_U2F_security_key)
        6.  [Provisioning and using API Tokens](#Provisioning_and_using_API_Tokens)
    4.  [Security bugs](#Security_bugs)
    5.  [Our next steps](#Our_next_steps)
    6.  [Contact us](#Contact_us)
:::

## Guidelines for Particpation {#Guidelines_for_Particpation}

- By participating, you agree to abide by the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/){.https}.

- You must verify your primary email address on your Test PyPI and PyPI accounts before setting up 2FA or an API token.

- You should sign up for the [PyPI Announcement Mailing List](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/){.https} for updates.

## Changes we\'re making {#Changes_we.27re_making}

To increase the security of PyPI downloads, we\'re introducing a few improvements:

### Two-factor authentication {#Two-factor_authentication}

[two-factor authentication (2FA)](https://pypi.org/help/#twofa){.https} is a new login security option.

You can use 2FA right now on [Test PyPI](http://test.pypi.org/){.http} and on [official PyPI](https://pypi.org){.https}. PyPI currently supports two 2FA methods. One is generating a code through a Time-based One-time Password (TOTP) application. After you set up 2FA on your PyPI account, then you must provide a TOTP (along with your username and password) to log in. Therefore, to use 2FA on PyPI, you\'ll need to provision an application (usually a mobile phone app) in order to generate authentication codes; see below for suggestions and pointers. This feature is fully deployed and out of beta.

**In beta:** We support WebAuthn and thus \"security keys\". A security key (also known as a universal second factor, or U2F key) is hardware device that communicates via USB, NFC, or Bluetooth. Popular keys include Yubikey, Google Titan and Thetis. PyPI supports any [FIDO U2F compatible key](https://fidoalliance.org/specifications/download/){.https} and follows the [!WebAuthn standard](https://www.w3.org/TR/webauthn/){.https}. Users who have set up this second factor will be prompted to use their key (usually by inserting it into a USB port and pressing a button) when logging in. The WebAuthn support is **in beta** so check the \"caution\" warning below.

Two-factor authentication currently only applies to the login step, not package uploads.

### Upload API tokens {#Upload_API_tokens}

We\'re adding scoped API tokens so you can upload a package using a token instead of a username and password.

**In beta:** You can create and use API tokens to upload packages. API tokens provide an alternative way (instead of username and password) to authenticate when uploading packages to PyPI or Test PyPI. You can create a token for an entire PyPI account, in which case, the token will work for all projects associated with that account. Alternatively, you can limit a token\'s scope to a specific project. And then, manually or in your configuration file, when you upload, use `@token`{.backtick} for the username and the token string for the password. API token support is **in beta** so check the \"caution\" warning below.

### Audit log {#Audit_log}

We\'re adding a display so you can look at things that have happened in your user account or project, and check for signs someone\'s stolen your credentials.

You can view a log of sensitive actions from the last two weeks that are relevant to your user account, and if you are an Owner at least one project on PyPI, you can view a log of sensitive actions (performed by ANY user) relevant to projects you\'re an Owner for. (And PyPI administrators are able to view the full audit log.)

**In beta:** We\'re still refining this, so check the \"caution\" warning below. And the sensitive event logging and display starting on 16 August 2019, so you won\'t see sensitive events from before that date.

## Things to test {#Things_to_test}

Most of these you can test [on pypi.org](https://pypi.org/manage/account/#two-factor){.https}. For testing destructive actions, like removing an owner or deleting a project, please use [test.pypi.org](https://test.pypi.org/manage/account/#two-factor){.https}.

### Caution (before you test) {#Caution_.28before_you_test.29}

During this beta testing period, if things go awry, there\'s a chance we will need to wipe WebAuthn and API tokens from users\' accounts, so if you choose to try it, please be forewarned. That\'s why you need a PyPI-verified email address on [your user account](https://pypi.org/manage/account/){.https} before adding a second login auth factor, to make potential account recovery smoother.

We may also fail to log, or to properly display, events in the audit log.

Reminder! Sign up for the [PyPI Announcement Mailing List](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/){.https} to be kept in the loop as we continue this process!

### Workflows {#Workflows}

- Verify primary email address: check that the user log lists the event

- Add, disable, and remove 2FA token using TOTP: check that the user log lists the events

- Add, disable, and remove 2FA token using U2F (WebAuthn): check that the user log lists the events

- Login/Logout

- Set multiple 2FA tokens and login: check that the user log lists the events

- Add and remove project-scoped API token, and verify that you see this in the user log

- Add and remove user-scoped API token, and verify that you see this in the user log

- Upload a package using API token, and verify that you see this in the project log

- Remove a user from owner/maintainer status for a project, and verify that their API token for that project stops working and that the project log lists the event

- Delete a release from a project: verify that the project log lists the event

- Delete a project, and verify that an API token scoped for that project stops working

- User Registration and Confirmation

- Password Reset: check that the user log lists the event

### Testers we need {#Testers_we_need}

In particular, please help us test this if any of these apply to you:

- automate uploads using continuous integration

- save your PyPI credentials in [a \`.pypirc\` file](https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account){.https}

- use Windows

- usually visit PyPI on a mobile device

- are an organization where users share an auth token within a group

- have 4+ maintainers or owners for one project

- use an unusual TOTP app or U2F token

- have a slow Internet connection

- usually block cookies and JavaScript (note that you can\'t set up a U2F key without JavaScript)

- maintain 20+ projects

- created your PyPI account 6+ years ago

### Setting up a TOTP application {#Setting_up_a_TOTP_application}

See [our help docs](https://pypi.org/help/#totp){.https} for guidance on choosing a TOTP app for desktop or mobile.

### Setting up a U2F security key {#Setting_up_a_U2F_security_key}

See [our help docs](https://pypi.org/help/#utfkey){.https} for guidance on setting up your U2F security key. Please note that you cannot set up or use U2F for a second factor without turning on JavaScript, and that [right now we only support Chrome, Edge, and Firefox](https://github.com/pypa/warehouse/issues/6034){.https}.

### Provisioning and using API Tokens {#Provisioning_and_using_API_Tokens}

See [our help docs](https://pypi.org/help/#apitoken){.https} for guidance on provisioning and using API Tokens. You can create a token that allows uploads for all projects your user account has Maintainer or Owner access to, or scope it to a specific project.

## Security bugs {#Security_bugs}

If you find any potential security vulnerabilities, please [follow our published security policy](https://pypi.org/security/){.https}. Please don\'t report security issues in Warehouse via GitHub, IRC, or mailing lists. Instead, please directly email one or more of our maintainers.

## Our next steps {#Our_next_steps}

Once we fix all the urgent bugs we find, we\'ll remove the \"beta\" badge for each feature. Then we expect to move on to working on further security, accessibility, and internationalization tasks per [the Warehouse roadmap](https://wiki.python.org/psf/WarehouseRoadmap){.https}). Thanks to the Open Technology Fund for funding this work. More progress reports at [the Packaging Working Group\'s wiki page](https://wiki.python.org/psf/PackagingWG){.https}.

## Contact us {#Contact_us}

Security issues: [email security @ python dot org](https://pypi.org/security/){.https}

GitHub for all other bug reports & feature requests:[https://github.com/pypa/warehouse/issues/new](https://github.com/pypa/warehouse/issues/new){.https}

IRC: [#pypa-dev on Freenode](https://webchat.freenode.net/?channels=#pypa-dev){.https} (someone\'s usually there 10am-5pm Central Time on weekdays)

Email: [distutils-sig mailing list](https://mail.python.org/mailman3/lists/distutils-sig.python.org/){.https}

Thank you for testing Warehouse! You\'re helping us secure this ecosystem, and future users of PyPI will appreciate it. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}
::::
