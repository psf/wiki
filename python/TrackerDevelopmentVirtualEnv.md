# TrackerDevelopmentVirtualEnv

:::: {#content dir="ltr" lang="en"}
This page is derived from [TrackerDevelopment](TrackerDevelopment).

Not only does this cover installing under a virtualenv, but it also covers installing Rietveld. That part is not entirely finished, however.

::: table-of-contents
Contents

1.  [Before You Get Started](#Before_You_Get_Started)
    1.  [Prerequisites](#Prerequisites)
    2.  [Will be Installed](#Will_be_Installed)
    3.  [Environment Variables](#Environment_Variables)
    4.  [virtualenvwrapper Initial Setup](#virtualenvwrapper_Initial_Setup)
2.  [The Main Course](#The_Main_Course)
    1.  [Initial Preparation](#Initial_Preparation)
    2.  [Set Up Postgresql](#Set_Up_Postgresql)
    3.  [Install Roundup](#Install_Roundup)
    4.  [Configure the Python-Dev Instance](#Configure_the_Python-Dev_Instance)
    5.  [Fire It Up](#Fire_It_Up)
    6.  [Install Rietveld](#Install_Rietveld)
:::

# Before You Get Started {#Before_You_Get_Started}

## Prerequisites {#Prerequisites}

1.  Python 2.7 (or 3?)
2.  pip (under same Python)
3.  svn
4.  postgresql 9 server (devel)
5.  openssl (devel)
6.  swig
7.  patch
8.  virtualenvwrapper (pip install virtualenvwrapper)

## Will be Installed {#Will_be_Installed}

1.  psycopg2
2.  beautifulsoup
3.  m2crypto

## Environment Variables {#Environment_Variables}

Set them however you like!

    export WORKON_HOME=~/.envs
    export PROJECT_DIR=~/projects
    export MAIL_DOMAIN=spam.eggs
    export TRACKER_HOST=localhost
    export TRACKER_PORT=9999

## virtualenvwrapper Initial Setup {#virtualenvwrapper_Initial_Setup}

    echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc
    mkdir -p $WORKON_HOME
    source `which virtualenvwrapper.sh`

# The Main Course {#The_Main_Course}

## Initial Preparation {#Initial_Preparation}

    mkvirtualenv tracker  # leaves you in the virtual environment
    pip install psycopg2
    pip install beautifulsoup
    pip install m2crypto  # http://stackoverflow.com/questions/7772965/
    cd $VIRTUAL_ENV/build/m2crypto 
    chmod u+x fedora_setup.sh
    ./fedora_setup.sh build
    ./fedora_setup.sh install
    echo 'export PGDATA=$VIRTUAL_ENV/pg_data' >> $VIRTUAL_ENV/bin/postactivate

## Set Up Postgresql {#Set_Up_Postgresql}

    workon tracker
    mkdir $PGDATA
    pg_ctl initdb
    # if needed, fix auth in $VIRTUAL_ENV/pg_data/pg_hba.conf
    pg_ctl start
    psql -c 'create user roundup' postgresql
    psql -c 'alter user roundup with createdb' postgresql

## Install Roundup {#Install_Roundup}

    workon tracker
    cd $PROJECT_DIR
    svn co http://svn.python.org/projects/tracker
    cd tracker/roundup-src
    python setup.py install

## Configure the Python-Dev Instance {#Configure_the_Python-Dev_Instance}

    workon tracker
    cd $PROJECT_DIR/tracker/instances/python-dev
    mkdir db
    echo postgresql > db/backend_name
    cp config.ini.template config.ini # and adjust settings
    sed -i "s/localhost:9999/$TRACKER_HOST:$TRACKER_PORT/" config.ini
    sed -i "s/#domain = NO DEFAULT/domain = $MAIL_DOMAIN/"
    sed -i 's/\(def init(db):.*\)$/\1\n    return/' detectors/rietveldreactor.py
    $VIRTUAL_ENV/bin/roundup-admin -i `pwd` init

## Fire It Up {#Fire_It_Up}

    workon tracker
    cd $PROJECT_DIR/tracker/instances/python-dev
    echo "export RU_INSTANCE=`pwd`" >> $VIRTUAL_ENV/bin/postactivate
    echo "export RU_HOST=$TRACKER_HOST" >> $VIRTUAL_ENV/bin/postactivate
    echo "export RU_PORT=$TRACKER_PORT" >> $VIRTUAL_ENV/bin/postactivate
    echo '"alias start-roundup=$VIRTUAL_ENV/bin/roundup-server -n $RU_HOST -p $RU_PORT python-dev=$RU_INSTANCE"' >> $VIRTUAL_ENV/bin/postactivate
    echo '"alias admin-roundup=$VIRTUAL_ENV/bin/roundup-admin -i $RU_INSTANCE"' >> $VIRTUAL_ENV/bin/postactivate
    start-roundup # and point your browser to localhost:9999

## Install Rietveld {#Install_Rietveld}

This part isn\'t working all the way, and is likely incorrect/missing pieces.

    workon tracker
    cd $PROJECT_DIR/tracker/instances/python-dev/rietveld
    make all
    cd $PROJECT_DIR/tracker/instances/python-dev/detectors
    ../scripts/initrietveld
::::
