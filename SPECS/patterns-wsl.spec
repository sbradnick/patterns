#
# spec file for package patterns-wsl
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           patterns-wsl
Version:        20210712
Release:        0
Summary:        Patterns for Installation (Windows Subsystem for Linux, WSL)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the WSL pattern.

##########

%package wsl
%pattern_development
Summary:        WSL
Group:          Metapackages
Provides:       pattern() = wsl
Provides:       pattern-icon() = pattern-wsl
Provides:       pattern-order() = 3420
Provides:       pattern-visible()

Requires:       bash
#Requires:       rubygems
Recommends:     adwaita-icon-theme
Recommends:     fish
Recommends:     gnome-icon-theme
Recommends:     noto-sans-fonts
Recommends:     powerline-fonts
Recommends:     zsh
#Suggests:       ruby-doc-html
#Suggests:       ruby-doc-ri
#Suggests:       ruby-examples
#Suggests:       rubygem-mysql
#Suggests:       rubygem-racc
#Suggests:       rubygem-ruby-fcgi
#Suggests:       ruby-test-suite
#Suggests:       ruby-tk

%description wsl
Tools / libraries for using WSL.

%files wsl
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/wsl.txt
