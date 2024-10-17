%global upstreamver 1r2p2

Name:           gap-table-of-marks
Version:        %(echo %upstreamver | sed -r "s/r|p/./g")
Release:        4.0%{?dist}
Summary:        GAP Table of Marks package


License:        GPLv2+
URL:            https://schmidt.nuigalway.ie/tomlib/
Source0:        http://schmidt.nuigalway.ie/tomlib/tomlib%{upstreamver}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
Requires:       gap-core
Provides:       gap-pkg-tomlib = %{version}-%{release}

%description
This package provides access to several hundred tables of marks of
almost simple groups and their maximal subgroups.

%prep
%setup -q -n tomlib

# Remove spurious executable bits
chmod a-x doc/tomlib.xml

# Compress large tables of marks
gzip --best data/*.tom

%build
# Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT%{_gap_dir}/pkg
cd ..
cp -a tomlib $RPM_BUILD_ROOT%{_gap_dir}/pkg
rm -f $RPM_BUILD_ROOT%{_gap_dir}/pkg/tomlib/README

%posttrans
    %{_bindir}/update-gap-workspace

%postun
    %{_bindir}/update-gap-workspace

%files
%doc README
%{_gap_dir}/pkg/tomlib/

%changelog
* Fri Nov 15 2013 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- New upstream release

* Mon Oct 21 2013 Jerry James <loganjerry@gmail.com> - 1.2.3-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Jerry James <loganjerry@gmail.com> - 1.2.2-3
- Rebuild for GAP 4.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan  3 2012 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- Initial RPM
