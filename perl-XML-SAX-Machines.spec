#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	SAX-Machines
Summary:	XML::SAX::Machines Perl module
Summary(pl):	Modu³ Perla XML::SAX::Machines
Name:		perl-XML-SAX-Machines
Version:	0.36
Release:	1
License:	Artistic, GPL or BSD
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-SAX >= 0.05
BuildRequires:	perl(XML::SAX::Base) >= 1.02
BuildRequires:	perl-XML-SAX-Writer >= 0.39
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-XML-SAX >= 0.05
Requires:	perl(XML::SAX::Base) >= 1.02
Requires:	perl-XML-SAX-Writer >= 0.39
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX::Machines is a collection of APIs that allow complex SAX
machines to be constructed without a huge amount of extra typing.

%description -l pl
XML::SAX::Machines to zestaw API pozwalaj±cy na konstruowanie
z³o¿onych konstrukcji SAX bez du¿ej ilo¶ci nadmiarowego kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_sitelib}/XML/Filter/*.pm
%{perl_sitelib}/XML/SAX/*.pm
%{perl_sitelib}/XML/SAX/Machines
%{_mandir}/man3/*
