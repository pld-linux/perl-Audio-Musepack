#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Audio
%define	pnam	Musepack
Summary:	An OO interface to Musepack file information and APE tag fields, implemented in pure Perl
Summary(pl.UTF-8):	Czysto perlowy interfejs obiektowy do informacji o plikach Musepack i znaczników APE
Name:		perl-Audio-Musepack
Version:	0.7
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a22b8426cae9f7c5006d5ee8fd780d5a
URL:		http://search.cpan.org/dist/Audio-Musepack/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MP3-Info >= 1.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module returns a hash containing basic information about a
Musepack file, as well as tag information contained in the Musepack
file's APE tags.

%description -l pl.UTF-8
Ten moduł zwraca hasza zawierającego podstawowe informacje o pliku
Musepack, a także informacje o znacznikach APE zawartych w pliku
Musepack.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/*.pm
%{_mandir}/man3/*
