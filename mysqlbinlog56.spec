%define mysql_version 5.6.8
%define mysql_release rc
%define _unpackaged_files_terminate_build 0

Name:           mysqlbinlog
Version:        %{mysql_version}
Release:        %{mysql_release}%{?dist}
Summary:        Dumps a MySQL binary log in a format usable for viewing or for piping to the mysql command line   client.

Group:          Development/Tools
License:        GNU GPL v2
URL:            https://launchpad.net/mysql
Source0:        mysql-%{mysql_version}-%{mysql_release}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  gcc-c++, make, cmake, ncurses-devel
Requires:       glibc, libstdc++

%description
Dumps a MySQL binary log in a format usable for viewing or for piping to
the mysql command line client.

%prep
%setup -q -n mysql-%{mysql_version}-%{mysql_release}

%build
%cmake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/mysqlbinlog $RPM_BUILD_ROOT%{_bindir}/mysqlbinlog56

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%exclude %{_prefix}/data
%exclude %{_prefix}/docs
%exclude %{_prefix}/include
%exclude %{_prefix}/lib
%exclude %{_prefix}/man
%exclude %{_prefix}/mysql-test
%exclude %{_prefix}/scripts
%exclude %{_prefix}/share
%exclude %{_prefix}/sql-bench
%exclude %{_prefix}/support-files/
%exclude %{_prefix}/COPYING
%exclude %{_prefix}/INSTALL-BINARY
%exclude %{_prefix}/README
%exclude %{_bindir}/innochecksum
%exclude %{_bindir}/msql2mysql
%exclude %{_bindir}/my_print_defaults
%exclude %{_bindir}/myisam*
%exclude %{_bindir}/mysql
%exclude %{_bindir}/mysql_*
%exclude %{_bindir}/mysqlaccess*
%exclude %{_bindir}/mysqladmin
%exclude %{_bindir}/mysqlbug
%exclude %{_bindir}/mysqlcheck
%exclude %{_bindir}/mysqld*
%exclude %{_bindir}/mysqldump*
%exclude %{_bindir}/mysqlhotcopy
%exclude %{_bindir}/mysqlimport
%exclude %{_bindir}/mysqlshow
%exclude %{_bindir}/mysqlslap
%exclude %{_bindir}/mysqltest*
%exclude %{_bindir}/perror
%exclude %{_bindir}/replace
%exclude %{_bindir}/resolve*
%{_bindir}/mysqlbinlog56
[ec2-user@yog SPECS]$ cat  mysqlbinlog56.spec
%define mysql_version 5.6.8
%define mysql_release rc
%define _unpackaged_files_terminate_build 0

Name:           mysqlbinlog
Version:        %{mysql_version}
Release:        %{mysql_release}%{?dist}
Summary:        Dumps a MySQL binary log in a format usable for viewing or for piping to the mysql command line client.

Group:          Development/Tools
License:        GNU GPL v2
URL:            https://launchpad.net/mysql
Source0:        mysql-%{mysql_version}-%{mysql_release}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  gcc-c++, make, cmake, ncurses-devel
Requires:       glibc, libstdc++

%description
Dumps a MySQL binary log in a format usable for viewing or for piping to
the mysql command line client.

%prep
%setup -q -n mysql-%{mysql_version}-%{mysql_release}

%build
%cmake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/mysqlbinlog $RPM_BUILD_ROOT%{_bindir}/mysqlbinlog56

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%exclude %{_prefix}/data
%exclude %{_prefix}/docs
%exclude %{_prefix}/include
%exclude %{_prefix}/lib
%exclude %{_prefix}/man
%exclude %{_prefix}/mysql-test
%exclude %{_prefix}/scripts
%exclude %{_prefix}/share
%exclude %{_prefix}/sql-bench
%exclude %{_prefix}/support-files/
%exclude %{_prefix}/COPYING
%exclude %{_prefix}/INSTALL-BINARY
%exclude %{_prefix}/README
%exclude %{_bindir}/innochecksum
%exclude %{_bindir}/msql2mysql
%exclude %{_bindir}/my_print_defaults
%exclude %{_bindir}/myisam*
%exclude %{_bindir}/mysql
%exclude %{_bindir}/mysql_*
%exclude %{_bindir}/mysqlaccess*
%exclude %{_bindir}/mysqladmin
%exclude %{_bindir}/mysqlbug
%exclude %{_bindir}/mysqlcheck
%exclude %{_bindir}/mysqld*
%exclude %{_bindir}/mysqldump*
%exclude %{_bindir}/mysqlhotcopy
%exclude %{_bindir}/mysqlimport
%exclude %{_bindir}/mysqlshow
%exclude %{_bindir}/mysqlslap
%exclude %{_bindir}/mysqltest*
%exclude %{_bindir}/perror
%exclude %{_bindir}/replace
%exclude %{_bindir}/resolve*
%{_bindir}/mysqlbinlog56
