Summary:	BitTorrent client written in the C++.
Summary(pl):	Klient BitTorrent napisany w C++.
Name:		ctorrent
Version:	1.3.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://voxel.dl.sourceforge.net/sourceforge/ctorrent/%{name}-%{version}.tar.gz
# Source0-md5:  1bc787df91285a9cec8509617c3152d6
URL:		http://ctorrent.sourceforge.net/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CTorrent is built as a console program, which means that it doesn't
require any graphical components (such as an X server) on the machine
you are running it on, you can even run it remotely through a terminal
if you wish. There are quite a few people who run "console only"
servers and want to use them to download files in the background.
CTorrent can help you do exactly this, assuming you are downloading
from the BitTorrent network.

%description -l pl
CTorrent jest programem dla konsoli, co oznacza ¿e nie wymaga ¿adnych
komponentów graficznych (takich jak serwer X) na maszynie, na której
go uruchamiasz, mo¿esz go uruchomiæ nawet zdalnie je¶li chcesz. Jest
stosunkowo ludzi, którzy u¿ywaj± programów tylko konsolowych i chc±
u¿ywaæ ich do ¶ci±gania plików w tle. CTorrent dok³adnie w tym ci
pomo¿e, zak³adaj±c ze u¿ywasz sieci BitTorrent.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ctorrent
