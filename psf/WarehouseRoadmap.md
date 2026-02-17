# WarehouseRoadmap

::: {#content dir="ltr" lang="en"}
# Warehouse roadmap {#Warehouse_roadmap}

## Current {#Current}

See [https://warehouse.readthedocs.io/roadmap/](https://warehouse.readthedocs.io/roadmap/){.https} .

## Complete & archived {#Complete_.26_archived}

We completed these milestones between December 2017 and May 2018. See PackagingWG for details.

### 1. Maintainer Minimum Viable Product milestone \-- COMPLETE {#A1._Maintainer_Minimum_Viable_Product_milestone_--_COMPLETE}

[On GitHub.](https://github.com/pypa/warehouse/milestone/8){.https}

The point of this first milestone is to give package maintainers a solid chance to try out Warehouse and report critical bugs early. This milestone is for necessary features so we can [ask package maintainers to try, test, and report bugs against Warehouse](WarehousePackageMaintainerTesting).

We completed this milestone on **Feb. 20th, 2018**.

### 2. End User MVP \-- COMPLETE {#A2._End_User_MVP_--_COMPLETE}

[On GitHub.](https://github.com/pypa/warehouse/milestone/9){.https}

Necessary features for Python users (other than package maintainers) to try, test, and report bugs against Warehouse. Including infrastructure improvements tracked in [the PyPI infrastructure repository](https://github.com/python/pypi-infra){.https}.

We completed this milestone on **Feb. 23rd, 2018**.

### 3: Publicize beta \-- COMPLETE {#A3:_Publicize_beta_--_COMPLETE}

[On GitHub.](https://github.com/pypa/warehouse/milestone/10){.https}

Prepare to [blog](https://pyfound.blogspot.com/2018/03/warehouse-all-new-pypi-is-now-in-beta.html){.https}, email, etc. to [invite Python community to test Warehouse](./PackagingWG(2f)PyPIBetaAnnouncement.html). Redirect an increasing portion of *pip install* traffic to Warehouse, [as we did during a load test in mid-March](https://status.python.org/incidents/0gmdf90kkt8n){.https}. This thus requires an infrastructure changeover.

We [completed this milestone](https://pyfound.blogspot.com/2018/03/warehouse-all-new-pypi-is-now-in-beta.html){.https} on **March 26th, 2018**.

### 4: Launch: redirect pypi.python.org to pypi.org \-- COMPLETE {#A4:_Launch:_redirect_pypi.python.org_to_pypi.org__--_COMPLETE}

[On GitHub.](https://github.com/pypa/warehouse/milestone/1){.https}

Replace the legacy code base powering PyPI with Warehouse, e.g., redirect web browser and API requests for *pypi.python.org* to *pypi.org*. Warehouse (as instantiated at PyPI.org) at this milestone is good enough to be the main entryway to Python packages. We [have announced this](https://mail.python.org/mm3/archives/list/pypi-announce@python.org/thread/JCNO7SWQTKY54MKOZQ22PV3TUJGRM3GR/){.https} on [the pypi-announce mailing list](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/){.https}.

This is *not necessarily at feature parity* with [the old PyPI system](https://github.com/pypa/pypi-legacy){.https}. We already auto deploy the *master* branch to both pypi.org and test.pypi.org, and pypi.org and pypi.python.org share data stores (so they\'re really just two different views over the same data) (and test.pypi.org and testpypi.python.org also share data store), so this is all live and able to be used *right now*. Thus, launching is really just flipping the switch to make people go to the new site by default.

We are temporarily keeping the legacy code base running [at legacy.pypi.org](http://legacy.pypi.org/){.http} for people to be able to access it until we maintain feature parity, so that people depending on something that hasn\'t yet been implemented have a mechanism to continue to do that.

We [completed](https://blog.python.org/2018/04/new-pypi-launched-legacy-pypi-shutting.html){.https} this milestone on Monday, **16 April 2018**.

### 5: Shut Down Legacy PyPI \-- COMPLETE {#A5:_Shut_Down_Legacy_PyPI_--_COMPLETE}

[Issues in this milestone, on GitHub.](https://github.com/pypa/warehouse/milestone/7){.https}

Prerequisites to shut down [legacy PyPI](http://legacy.pypi.org/){.http}. In general, we aimied to do this once we reach feature parity, but some existing features were acceptable to complete later. The URL pypi.python.org will continue to redirect to Warehouse.

We announced this on [the pypi-announce mailing list](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/){.https}.

We did this on Monday, **30 April 2018**.
:::
