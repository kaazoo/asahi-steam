Name:           steam
Version:        0
Release:        1%{?dist}
Summary:        Steam wrapper for Fedora Asahi Remix

License:        MIT
URL:            https://pagure.io/fedora-asahi/steam
Source0:        shim.py
Source1:        LICENSE
Source2:        README.md

BuildArch:      noarch

BuildRequires:  coreutils

Requires:       bash
Requires:       fex-emu
Requires:       grep
Requires:       krun
Requires:       python3
Requires:       xwininfo

Requires:       python3dist(pyqt6)
Requires:       python3dist(pexpect)
Requires:       python3dist(requests)
Requires:       python3dist(pyxdg)

%description
This package provides a wrapper to download, install and run Steam on Fedora
Asahi Remix.

%prep
%autosetup -c -T

cp -p %SOURCE1 %SOURCE2 .

%build
# Nothing to do here

%install
install -Dpm0755 %SOURCE0 %{buildroot}%{_bindir}/steam

%files
%license LICENSE
%doc README.md
%{_bindir}/steam

%changelog
* Wed Sep 25 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-1
- Initial version
