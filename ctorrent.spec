Summary:	BitTorrent client written in the C++
Summary(pl):	Klient BitTorrenta napisany w C++
Name:		ctorrent
Version:	1.3.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://voxel.dl.sourceforge.net/sourceforge/ctorrent/%{name}-%{version}.tar.gz
# Source0-md5:	224ab814d1a71e90dc916d026b7696c4
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
CTorrent jest programem dla konsoli, co oznacza �e nie wymaga �adnych
komponent�w graficznych (takich jak serwer X) na maszynie, na kt�rej
bedzie uruchamiany, mo�na go uruchomi� nawet zdalnie je�li zajdzie
taka potrzeba. Jest stosunkowo niewielu ludzi, kt�rzy u�ywaj�
program�w przeznaczonych dla konsoli i chc� u�ywa� ich do �ci�gania
plik�w w tle. CTorrent pomaga dok�adnie w tym zadaniu, zak�adaj�c i�
u�ywa si� sieci BitTorrent.

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
%doc AUTHORS
%attr(755,root,root) %{_bindir}/ctorrent
