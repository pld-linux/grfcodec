Summary:	Programs to modify Transport Tycoon Deluxe's GRF files
Summary(pl.UTF-8):	Narzędzia do modyfikacji plików GRX gry Transport Tycoon Deluxe
Name:		grfcodec
Version:	6.0.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://binaries.openttd.org/extra/grfcodec/%{version}/%{name}-%{version}-source.tar.xz
# Source0-md5:	02f3c89dfbc4804bb69b48bf8f4d5350
Patch0:		%{name}-version.patch
URL:		http://www.ttdpatch.net/grfcodec/
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	upx
BuildRequires:	xz
Obsoletes:	nforenum
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF and NFO
files.

%description -l pl.UTF-8
Zestaw narzędzi do modyfikacji plików GRX oraz NFO gry Transport
Tycoon Deluxe.

%prep
%setup -q
%patch0 -p1

# drop -O2 flag from FLAGS
%{__sed} -i 's,-O2,,' Makefile

# set prefix to proper one
%{__sed} -i 's,%{_prefix}/local,%{_prefix},' Makefile.bundle

%build
%{__make} \
	CXX=%{__cxx} \
	CXXFLAGS="%{rpmcxxflags}" \
	LDOPT="%{rpmldflags}" \
	V="1"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt changelog.txt
%attr(755,root,root) %{_bindir}/grfcodec
%attr(755,root,root) %{_bindir}/grfdiff
%attr(755,root,root) %{_bindir}/grfid
%attr(755,root,root) %{_bindir}/grfmerge
%attr(755,root,root) %{_bindir}/grfstrip
%attr(755,root,root) %{_bindir}/nforenum
%{_mandir}/man1/*.1*
