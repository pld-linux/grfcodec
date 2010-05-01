%define		rev	2306
Summary:	Programs to modify Transport Tycoon Deluxe's GRF files
Summary(pl.UTF-8):	Narzędzia do modyfikacji plików GRX gry Transport Tycoon Deluxe
Name:		grfcodec
Version:	0.9.10
Release:	0.%{rev}.1
License:	GPL v2+
Group:		Applications
Source0:	http://binaries.openttd.org/extra/grfcodec/%{version}/%{name}-r%{rev}-source.tar.bz2
# Source0-md5:	16de60c05fba2aa4a5c2b22d4e0eff42
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-destdir.patch
URL:		http://www.ttdpatch.net/grfcodec/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	upx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.

%description -l pl.UTF-8
Zestaw narzędzi do modyfikacji plików GRX gry Transport Tycoon Deluxe.

%prep
%setup -q -n %{name}-r%{rev}
%patch0 -p1
%patch1 -p1

VER=$(awk '/VER /{print $3}' version.def)
if [ "$VER" != "%{version}" ]; then
	: Current version is $VER, not %{version}
	exit 1
fi

%build
%{__make} \
	SVNVERSION="echo %{rev}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGAPP="%{rpmcxxflags}" \
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
%doc Changelog todo.txt
%attr(755,root,root) %{_bindir}/grf*
