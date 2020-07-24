%define _prefix /gem_base/epics/extensions/src
%define gemopt opt
%define version 3.15.8
%define name tdct
%define release 2.17.5
%define repository gemdev
%define debug_package %{nil}
%define arch %(uname -m)
%define checkout %(git log --pretty=format:'%h' -n 1) 

#These global defines are added to prevent stripping
# symbols on vxWorks cross-compiled code
# Getting 'strip' to work is probably only needed for
# building a related debug sub-package
#
# But this prevents all the strip warnings
# mrippa 20120202
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Summary: tdct for editing schemtaics for EPICS
Name: %{name}
Version: %{version}
Release: %release.%(date +"%Y%m%d")%{checkout}%{?dist}
License: Proprietary
Group: Applications/Engineering
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix: %{_prefix}
BuildRequires: epics-base-devel java-1.8.0-openjdk
Requires: epics-base-devel java-1.8.0-openjdk


%description
EPICS is a set of Open Source software tools, Vlibraries and applications developed collaboratively and used worldwide to create distributed soft real-time control systems for scientific instruments such as a particle accelerators, telescopes and other large scientific experiments. TDCT is used to edit and create schematics describing databases for EPICS.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}
cp -r tdct-%{release} $RPM_BUILD_ROOT/%{_prefix}/%{name}

%post

%postun

%clean
## Usually you won't do much more here than
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /%{_prefix}/%{name}
/%{_prefix}/%{name}/*



%changelog
