# CloudPyPI

::: {#content dir="ltr" lang="en"}
# Cloud PyPI - Mirroring PyPI in the cloud {#Cloud_PyPI_-_Mirroring_PyPI_in_the_cloud}

*Update:* This project is now canceled, since PyPI is being on hosted on a fastly CDN and the PyPI server itself is hosted on a VM at OSL/OSU.

## Idea {#Idea}

We are setting up a PyPI mirror of the static content of PyPI in Amazon [CloudFront](./CloudFront.html){.nonexistent}.

## Proposal {#Proposal}

- [CloudPyPI/Proposal](./CloudPyPI(2f)Proposal.html)

The proposal was accepted by the PSF in their December 2010 board meeting.

Funding was limited to an initial USD 500 for Amazon costs to see whether the project would succeed.

## Resources {#Resources}

- [Amazon AWS Getting Started Guide](http://docs.amazonwebservices.com/AmazonCloudFront/2010-11-01/GettingStartedGuide/){.http}

- [Developer Intro to the PyPI code](CheeseShopDev)

- [PyPI RPC interface](PyPIXmlRpc) (which we likely won\'t use, but gives an idea of how the meta data is stored)

- [PyPI Code](https://bitbucket.org/loewis/pypi){.https}

## Example CDN {#Example_CDN}

We\'ve setup an example CDN which only provides caching services to the PyPI server and uses the pypi.python.org server as origin:

- [https://d1t66zoqn9vlte.cloudfront.net/simple/](https://d1t66zoqn9vlte.cloudfront.net/simple/){.https}

- For more details on the used setup, please see [CloudPyPI/ExampleCDN](./CloudPyPI(2f)ExampleCDN.html)

## Team {#Team}

Implementation:

- [Marc-André Lemburg](MarcAndreLemburg)

- [Grig Gheorghiu](GrigGheorghiu)

- [Neil Schemenauer](NeilSchemenauer)

- [Vern Ceder](VernCeder)

Helping with the PyPI code:

- Richard Jones
- Martin von Löwis

## Mailing List {#Mailing_List}

- [cloud-pypi@lists.egenix.com](mailto:cloud-pypi@lists.egenix.com){.mailto} (private to the project team)

## Amazon EC2: Project Development Server {#Amazon_EC2:_Project_Development_Server}

- [CloudPyPI/DevelopmentServer](./CloudPyPI(2f)DevelopmentServer.html)

## Amazon S3 {#Amazon_S3}

- [CloudPyPI/S3](./CloudPyPI(2f)S3.html)

## Access Control {#Access_Control}

- [CloudPyPIGroup](CloudPyPIGroup)

This is a public page. Please don\'t add any sensitive information to the page. Instead, create subpages that are only available to team members.

Please put the following ACL line at the top of subpages with sensitive information:

    #acl CloudPyPIGroup:read,write,revert,admin All:
:::
