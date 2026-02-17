# PSF Python Job Board

:::: {#content dir="ltr" lang="en"}
# PSF Python Job Board {#PSF_Python_Job_Board}

This page describes the PSF Python Job Board which is run by volunteers to provide the Python community with an important resource to find jobs where they can use Python.

::: table-of-contents
Contents

1.  [PSF Python Job Board](#PSF_Python_Job_Board)
    1.  [Job board process](#Job_board_process)
    2.  [Project organization](#Project_organization)
    3.  [Mailing list](#Mailing_list)
    4.  [Relaunch Project](#Relaunch_Project)
    5.  [Resources](#Resources)
        1.  [Production](#Production)
        2.  [Staging](#Staging)
        3.  [Web site administration](#Web_site_administration)
        4.  [Web site code base](#Web_site_code_base)
:::

## Job board process {#Job_board_process}

Job submissions are entered into a web form, the form creates a database record which is then used for review. After approval the Django site will then list the submissions automatically.

1.  Job submitters [log in to the website](https://www.python.org/accounts/login/?next=/jobs/create/){.https} (after having registered for an account)

2.  Submitters [create a job posting record](https://www.python.org/jobs/create/){.https}

3.  Submissions are checked against a list of quality criteria by the reviewers using the [review panel](https://www.python.org/jobs/review/){.https}; see the [/Reviewers](./PSF(20)Python(20)Job(20)Board(2f)Reviewers.html) page for details on the review process

4.  Submissions which need refinement are rejected together with a note mentioning the reason for rejection (using the \"review\" button on the review panel).

5.  Good submissions are approved and then automatically listed on the job board page in order of submission date (in most recent first order)

Job postings are automatically unlisted after 90 days. They can also be removed or archived manually using the Django database interface by setting the job listing status setting to *removed*.

Remarks:

- Submissions which have problems could also be refined directly in the system by the submitters, provided they created it while being logged in. The review page doesn\'t show this status, though, so it\'s probably better to go with the rejection procedures for the time being.
- Reviews by multiple persons would need to be coordinated, since the system does not provide this functionality. For the time being, it\'s better to have one person do the review.

## Project organization {#Project_organization}

The job board team has decreased a lot due to the long project run time. We will launch with a small team of reviewers:

- [/Reviewers](./PSF(20)Python(20)Job(20)Board(2f)Reviewers.html) - team members who review job postings The review process is also described on the above page.

Issues we find are posted to the [python.org site\'s issue tracker](https://github.com/python/pythondotorg/issues){.https}

- and tagged with \"job board\". The issues are then either worked on by the PSF contractors assigned to the python.org website project, or volunteers who want to help.

The job board team itself will not focus on the development anymore for the time being.

## Mailing list {#Mailing_list}

The volunteers use a mailing list to coordinate:

- [Python Jobs Mailing List](https://mail.python.org/mailman/listinfo/jobs){.https}

The list gets all email sent to [jobs@python.org](mailto:jobs@python.org){.mailto}. In the previous system, job postings were sent in via email. This is no longer necessary and new submissions should only be done via the [web interface](https://www.python.org/jobs/create/){.https}.

The jobs app will send notification about new postings to this list, so that reviewers get notified of new submissions.

If you want to help in the job board team, please write to [jobs@python.org](mailto:jobs@python.org){.mailto}.

Here\'s the mailing list archive:

- [Python Jobs List Archive](https://mail.python.org/mailman/private/jobs/){.https} (requires login)

## Relaunch Project {#Relaunch_Project}

In the years before the relaunch, the jobs board was run by single volunteers. Since the load had increased a lo and the last volunteer, Chris Withers, had left the project, the PSF wanted to replace the jobs board with a team of volunteers using a database driven integrated jobs app.

From 2014 to 2015, a team of volunteers worked to relaunch the job board using a jobs app on the new python.org website (which was launched in 2014).

The relaunch project page is still available: [/Relaunch Project](./PSF(20)Python(20)Job(20)Board(2f)Relaunch(20)Project.html)

## Resources {#Resources}

### Production {#Production}

*Note: The jobs app used to run under the temporary URL /newjobs/ during development. This has now been changed back to /jobs/.*

- [Job board jobs listing](http://www.python.org/jobs/){.http} on the production site.

- [Job board review panel](http://www.python.org/jobs/review/){.http} This allows reviewing new job postings.

### Staging {#Staging}

*Note: The jobs app used to run under the temporary URL /newjobs/ during development. This has now been changed back to /jobs/.*

The staging system can be used to check new developments.

- [Staging system implementation of the new job board](https://staging.python.org/jobs/){.https} This runs a copy of the production database on the master branch of the python.org repository and is updated frequently.

- [Staging system job board review panel](http://staging.python.org/jobs/review/){.http} on the staging site.

### Web site administration {#Web_site_administration}

- [Django admin interface of the python.org site](https://www.python.org/admin/){.https}

- [New site\'s issue trackers](https://github.com/python/pythondotorg/issues){.https} If you find problems with the job app, please open tickets on this tracker.

### Web site code base {#Web_site_code_base}

- [Github repository of the new site](https://github.com/python/pythondotorg){.https} (includes the jobs app)

- [Job app code](https://github.com/python/pythondotorg/tree/master/jobs){.https}
::::
