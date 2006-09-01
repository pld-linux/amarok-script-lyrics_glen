%define		scriptname	lyrics_glen
Summary:	amaroK lyrics script by glen
Name:		amarok-script-glen
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	lyrics_glen.tar.bz2
# Source0-md5:	8b42a91c90f3a675a9d73019a030f23e
BuildRequires:	sed >= 4.0
Requires:	amarok
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts

%description
This package contains lyrc lyrics wrapper written by glen.

%prep
%setup -q -n %{scriptname}
%{__sed} -i -e '1s,#!/usr/bin/env ruby,#!%{_bindir}/ruby,' *.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp -a . $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_scriptdir}/%{scriptname}
%{_scriptdir}/%{scriptname}/README
%{_scriptdir}/%{scriptname}/COPYING
%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.rb
%{_scriptdir}/%{scriptname}/*.spec
