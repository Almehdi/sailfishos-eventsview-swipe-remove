Name:       sailfishos-eventsview-swipe-remove

# >> macros
BuildArch: armv7hl
# << macros

Summary:    Eventsview notifications remove swipe
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   lipstick-jolla-home-qt5 = 0.24.41.4-10.75.1.jolla

%description
Eventsview patch adding swipe right to remove notification action.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-eventsview-swipe-remove
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-eventsview-swipe-remove
mkdir -p %{buildroot}/usr/share/jolla-settings/pages/sailfishos-eventsview-swipe-remove
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-eventsview-swipe-remove || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-eventsview-swipe-remove || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-eventsview-swipe-remove
# >> files
# << files
