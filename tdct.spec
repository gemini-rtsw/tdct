%define _prefix /gem_base/epics/extensions/src
%define gemopt opt
%define name tdct
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

Summary: tdct for editing schematics for EPICS
Name: %{name}
Version: 2.18.6
Release: 2%{?dist}
License: Proprietary
Group: Applications/Engineering
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix: %{_prefix}
BuildRequires: java-1.8.0-openjdk
Requires: java-1.8.0-openjdk


%description
EPICS is a set of Open Source software tools, Vlibraries and applications developed collaboratively and used worldwide to create distributed soft real-time control systems for scientific instruments such as a particle accelerators, telescopes and other large scientific experiments. TDCT is used to edit and create schematics describing databases for EPICS.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_prefix}
mkdir -p %{buildroot}/gem_base/etc

cp -r %{name}_dist-%{version} %{buildroot}/%{_prefix}/%{name}
cp -r sym %{buildroot}/%{_prefix}/%{name}/
cp -r library %{buildroot}/%{_prefix}/%{name}/
cp etc/tdct.* %{buildroot}/gem_base/etc/

%post

%postun

%clean
## Usually you won't do much more here than
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /%{_prefix}/%{name}
/%{_prefix}/%{name}/*
/gem_base/etc/tdct.*


%changelog

