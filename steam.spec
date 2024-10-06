Name:           steam
Version:        0
Release:        6%{?dist}
Summary:        Steam wrapper for Fedora Asahi Remix

License:        MIT
URL:            https://pagure.io/fedora-asahi/steam
Source0:        shim.py
Source1:        LICENSE
Source2:        README.md
Source3:        steam.desktop
Source4:        steam.svg
Source5:        io.pagure.fedora_asahi.steam.metainfo.xml

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       bash
Requires:       dbus-x11
Requires:       fex-emu
Requires:       grep
Requires:       hicolor-icon-theme
Requires:       lsb_release
Requires:       muvm
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
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %SOURCE3
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ \
  %SOURCE4
install -Dpm0644 -t %{buildroot}%{_metainfodir}/ %SOURCE5

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.pagure.fedora_asahi.steam.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/steam
%{_datadir}/applications/steam.desktop
%{_datadir}/icons/hicolor/scalable/apps/steam.svg
%{_metainfodir}/io.pagure.fedora_asahi.steam.metainfo.xml

%changelog
* Sun Oct 6 2024 Alyssa Rosenzweig <alyssa@rosenzweig.io> - 0-6
- Fix obnoxious font size

* Fri Oct 4 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-5
- Add missing dependencies

* Tue Oct 1 2024 Alyssa Rosenzweig <alyssa@rosenzweig.io> - 0-4
- Rename krun to muvm

* Sun Sep 29 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-3
- Install the icon in the right place

* Thu Sep 26 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-2
- Add desktop launcher, icon and metadata

* Wed Sep 25 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-1
- Initial version
