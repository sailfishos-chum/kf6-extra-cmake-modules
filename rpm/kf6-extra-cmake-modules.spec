Name:    kf6-extra-cmake-modules
Summary: Additional modules for CMake build system
Version: 6.6.0
Release: 0%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://api.kde.org/ecm/
Source0: %{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires: kf6-rpm-macros
BuildRequires: make
BuildRequires: qt6-qtbase-devel
Requires: qt6-qtbase-devel
Recommends: appstream
Provides:      extra-cmake-modules

%description
Additional modules for CMake build system needed by KDE Frameworks.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 \
  -DBUILD_MAN_DOCS:BOOL=OFF \
  -DBUILD_HTML_DOCS:BOOL=OFF \
  -DBUILD_QTHELP_DOCS:BOOL=OFF \
  -DBUILD_TESTING:BOOL=OFF \
  %{?sphinx_build}
%cmake_build

%install
%cmake_install

%files
%doc README.rst
%license LICENSES/*.txt
%{_datadir}/ECM/
