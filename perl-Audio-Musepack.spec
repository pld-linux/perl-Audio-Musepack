#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	Musepack
Summary:	An object-oriented interface to Musepack file information and APE tag fields, implemented entirely in Perl.
#Summary(pl.UTF-8):	
Name:		perl-Audio-Musepack
Version:	0.7
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a22b8426cae9f7c5006d5ee8fd780d5a
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Audio-Musepack/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MP3-Info >= 1.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module returns a hash containing basic information about a Musepack
file, as well as tag information contained in the Musepack file's APE tags.
See Audio::APETags for more information about the tags.

The information returned by Audio::Musepack->info is keyed by:

	streamVersion
	channels
	totalFrames
	profile
	sampleFreq
	lastValidSamples
	encoder

Information stored in the main hash that relates to the file itself or is
calculated from some of the information fields is keyed by:

	trackLengthMinutes      : minutes field of track length
	trackLengthSeconds      : seconds field of track length
	trackLengthFrames       : frames field of track length (base 75)
	trackTotalLengthSeconds : total length of track in fractional seconds
	bitRate                 : average bits per second of file
	fileSize                : file size, in bytes
	filename                : filename with path



# %description -l pl.UTF-8
# TODO

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
