Summary:	BitTorrent client written in the C++
Summary(pl):	Klient BitTorrenta napisany w C++
Name:		ctorrent
%define	_base_version 1.3.4
%define	_dnh_version dnh2
Version:	%{_base_version}_%{_dnh_version}
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ctorrent/%{name}-%{_base_version}.tar.bz2
# Source0-md5:	823010ec78215d476537c9eba9381cdd
Patch0:		http://www.rahul.net/dholmes/ctorrent/patchset-ctorrent-%{_base_version}-%{_dnh_version}.diff
#URL:		http://ctorrent.sourceforge.net/
URL:		http://www.rahul.net/dholmes/ctorrent/
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

%description -l pl
CTorrent jest programem dla konsoli, co oznacza ¿e nie wymaga ¿adnych
komponentów graficznych (takich jak serwer X) na maszynie, na której
bêdzie uruchamiany, mo¿na go uruchomiæ nawet zdalnie je¶li zajdzie
taka potrzeba. Jest sporo osób, które u¿ywaj± serwerów tylko 
z konsol± i chc± u¿ywaæ ich do ¶ci±gania plików w tle. 
CTorrent pomaga dok³adnie w tym zadaniu, zak³adaj±c i¿
u¿ywa siê sieci BitTorrent.

%prep
%setup -q -n %{name}-%{_base_version}
%patch0 -p0

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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ctorrent
