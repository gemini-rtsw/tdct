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
Release: 4%{?dist}
License: Proprietary
Group: Applications/Engineering
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix: %{_prefix}
BuildRequires: java-1.8.0-openjdk
Requires: java-1.8.0-openjdk java-1.8.0-openjdk-headless


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
* Tue Dec 30 2025 Matt Rippa <matt.rippa@noirlab.edu> 2.18.6-4
- SYSCO-745: Add TDCT eapply20 support
- create unstable/2024q4 release
- create unstable/2024q3 release :
- setting git push options to be able to build on my local pipeline
- creating release unstable/2024q2 - also for testing gem-ci on hbfade
- update gem-ci because of nsf-noirlab/gemini/rtsw/gem-ci#60
- create unstable/2024q1 release
- make master the HEAD again, only small changes regarding gem-ci will be
  merged
- updated to gem-ci submodule to point to master branch
- edit BASE_CONTAINER to rockylinux8
- update gem-ci for fixed create-config.sh script
- updated gem-ci to newest version for pipeline testing
- create unstable/fkraemer-gemci-test-other release for gem-ci tests
- create unstable/2023q2 and update gem-ci to unstable/2023q2
- created unstable/2023q1-tr2 branch, updated gem-ci to point to
  unstable/2023q1
- Ran patch for tdct name issue
- update gem-ci to unstable/2022q4
- upgraded gem-ci for new tito builder and pipeline
- Prep for unstable/2022q1: git checkout stable/2021q4; git pull -ff-only; git
  checkout unstable/2022q1; gem-init-project-f -b stable/2021q4
- Update gem-ci for latest fix
- Updated to latest gem-ci and set to gem-ci/stable/2021q4

* Tue Dec 30 2025 Matt Rippa <matt.rippa@noirlab.edu>
- SYSCO-745: Add TDCT eapply20 support
- create unstable/2024q4 release
- create unstable/2024q3 release :
- setting git push options to be able to build on my local pipeline
- creating release unstable/2024q2 - also for testing gem-ci on hbfade
- update gem-ci because of nsf-noirlab/gemini/rtsw/gem-ci#60
- create unstable/2024q1 release
- make master the HEAD again, only small changes regarding gem-ci will be
  merged
- updated to gem-ci submodule to point to master branch
- edit BASE_CONTAINER to rockylinux8
- update gem-ci for fixed create-config.sh script
- updated gem-ci to newest version for pipeline testing
- create unstable/fkraemer-gemci-test-other release for gem-ci tests
- create unstable/2023q2 and update gem-ci to unstable/2023q2
- created unstable/2023q1-tr2 branch, updated gem-ci to point to
  unstable/2023q1
- Ran patch for tdct name issue
- update gem-ci to unstable/2022q4
- upgraded gem-ci for new tito builder and pipeline
- Prep for unstable/2022q1: git checkout stable/2021q4; git pull -ff-only; git
  checkout unstable/2022q1; gem-init-project-f -b stable/2021q4
- Update gem-ci for latest fix
- Updated to latest gem-ci and set to gem-ci/stable/2021q4


