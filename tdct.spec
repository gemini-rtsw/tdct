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
Release: 1%{?dist}
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
* Wed Aug 25 2021 ignacio arriagada <ignacio.arriagada@noirlab.edu> 2.18.6-1
- Changed spec file to have the right dependencies
- Changed spec files to use version properly
- Added new files of version 2.18.6 and removed old ones
- deleted unnecessary files and directories
- Included new changes in main dir
- Added files from latest release 2.18.4
- Renamed folder with latest version number

* Tue Aug 03 2021 Felix Kraemer <fkraemer@gemini.edu> 2.18.4-4
- initialized CI scripts

* Tue Jul 27 2021 Ignacio Arriagada <iarriagada@gemini.edu>
- Included new changes in main dir
- Added files from latest release 2.18.4
- Renamed folder with latest version number

* Thu Oct 08 2020 fkraemer <fkraemer@gemini.edu> 2.18.2-2
- applied new version/release scheme 
- applied tito configuration for new yum
  repositories

* Wed Aug 05 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.18.2.202008050532cf31419
- Release tag enriched with hour and minute (%%H%%M) to be able to build
  several RPMs a day without messing up the repo (fkraemer@gemini.edu)

* Wed Jul 29 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.18.2.20200729b97fd86
- moved edb.def to the right place (fkraemer@gemini.edu)

* Tue Jul 28 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.18.2.20200728f7e68d2
- fixed missing tdct.* in %%files section of specfile (fkraemer@gemini.edu)

* Tue Jul 28 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.18.2.202007284f1cbf6
- some restructuring of files and replace tdct-2.17.5 with tdct 2.18.2
  (fkraemer@gemini.edu)
- back (fkraemer@gemini.edu)
- replaces java with headless java (fkraemer@gemini.edu)

* Sun Jul 26 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.17.5.20200726dd2d1ae
- added some missing Gemini record symbols (kraemer@asmara.leibniz-kis.de)

* Fri Jul 24 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.17.5.20200724aa60df6
- another fix to specfile (fkraemer@gemini.edu)

* Fri Jul 24 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.17.5.2020072491e30d8
- another try to fix (fkraemer@gemini.edu)

* Fri Jul 24 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.17.5.20200724054ec6a
- fix in specfile (fkraemer@gemini.edu)

* Fri Jul 24 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-2.17.5.20200724bf51198
- new package built with tito

