#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	SAX-Machines
Summary:	XML::SAX::Machines Perl module
Summary(cs):	Modul XML::SAX::Machines pro Perl
Summary(da):	Perlmodul XML::SAX::Machines
Summary(de):	XML::SAX::Machines Perl Modul
Summary(es):	Módulo de Perl XML::SAX::Machines
Summary(fr):	Module Perl XML::SAX::Machines
Summary(it):	Modulo di Perl XML::SAX::Machines
Summary(ja):	XML::SAX::Machines Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	XML::SAX::Machines ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul XML::SAX::Machines
Summary(pl):	Modu³ Perla XML::SAX::Machines
Summary(pt):	Módulo de Perl XML::SAX::Machines
Summary(pt_BR):	Módulo Perl XML::SAX::Machines
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl XML::SAX::Machines
Summary(sv):	XML::SAX::Machines Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl XML::SAX::Machines
Summary(zh_CN):	XML::SAX::Machines Perl Ä£¿é
Name:		perl-XML-SAX-Machines
Version:	0.4
Release:	2
Epoch:		1
License:	Artistic, GPL or BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4ce6704ff5cd71b17dcaf296fb170c7
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-XML-SAX >= 0.05
BuildRequires:	perl(XML::SAX::Base) >= 1.02
# doc say 0.4100001, so maybe too much, but safer
BuildRequires:	perl-XML-SAX-Writer >= 0.42
BuildRequires:	rpm-perlprov >= 4.1-13
%endif
Requires:	perl-XML-SAX >= 0.05
Requires:	perl(XML::SAX::Base) >= 1.02
# as above...
Requires:	perl-XML-SAX-Writer >= 0.42
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLSITELIB=$RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/XML/Filter/*.pm
%{perl_vendorlib}/XML/SAX/*.pm
%{perl_vendorlib}/XML/SAX/Machines
%{_mandir}/man3/*
