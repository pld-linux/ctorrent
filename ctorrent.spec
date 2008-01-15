Summary:	Enhanced CTorrent - BitTorrent client written in the C++
Summary(pl.UTF-8):	Enhanced CTorrent - Klient BitTorrenta napisany w C++
Name:		ctorrent
Version:	3.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.rahul.net/dholmes/ctorrent/ctorrent-dnh%{version}.tar.gz
# Source0-md5:	23b37cd7b558ad6a27974b311499bab6
Patch0:		%{name}-incomplete.patch
Patch1:		%{name}-m4.patch
URL:		http://www.rahul.net/dholmes/ctorrent/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
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

%description -l pl.UTF-8
CTorrent jest programem dla konsoli, co oznacza że nie wymaga żadnych
komponentów graficznych (takich jak serwer X) na maszynie, na której
będzie uruchamiany, można go uruchomić nawet zdalnie jeśli zajdzie
taka potrzeba. Jest sporo osób, które używają serwerów tylko 
z konsolą i chcą używać ich do ściągania plików w tle. 
CTorrent pomaga dokładnie w tym zadaniu, zakładając iż
używa się sieci BitTorrent.

%prep
%setup -q -n %{name}-dnh%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="-I/usr/include/openssl"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README UserGuide README-DNH.TXT ChangeLog
%attr(755,root,root) %{_bindir}/ctorrent
