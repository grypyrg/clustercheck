Summary:     Percona Cluster Check
Name:        percona-clustercheck
Version:        1.1
Release:        1
License:        none
Source:         %{name}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-build
Requires:	python-twisted-web,MySQL-python
Group:          System/Base

%description
This package provides a python percona cluster health check interface

%prep
%setup -n %{name}

%build
# this section is empty as we're not actually building anything

%install
# create directories where the files will be located
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/usr/sbin

# put the files in to the relevant directories.
install -m 755 percona-clustercheck.init $RPM_BUILD_ROOT/etc/init.d/percona-clustercheck
install -m 755 percona-clustercheck.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/percona-clustercheck
install -m 755 clustercheck.py $RPM_BUILD_ROOT/usr/sbin

%post
# the post section is where you can run commands after the rpm is installed.
/sbin/chkconfig percona-clustercheck on

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

%files
%defattr(-,root,root)
/etc/init.d/percona-clustercheck
/usr/sbin/clustercheck.py
%config /etc/sysconfig/percona-clustercheck

%changelog
* Wed Sep 15 2015 Kenny Gryp <gryp@dakin.be>
- 1.0 r1 bug fix @lefred where wrong state is returned, updated package spec

* Tue Jan 13 2015 Kenny Gryp <gryp@dakin.be>
- 1.0 r2 Centos 7 Requires python-twisted-web

* Wed May 21 2014  Todd Merritt <tmerritt@email.arizona.edu>
- 1.0 r1 First rpm build
